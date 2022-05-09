import types
from inspect import getmodule
import sys
import importlib
import builtins
import __main__
from types import FunctionType,  CodeType , NoneType
type
class Parser():
    """Parsing object"""
    def serialize(self,obj) -> any:
        """Serialize obj to `dict[str, Any]`."""
        if isinstance(obj, int | str | NoneType):
            return obj

        if isinstance(obj, tuple):
            result = {}
            for index, element in enumerate(obj):
                result[index] = self.serialize(element)
            return {"tuple": result}
        
        if isinstance(obj, list):
            result = {}
            for index, element in enumerate(obj):
                result[index] = self.serialize(element)
            return {"list": result}

        if isinstance(obj, dict):
            return {"dict": obj}
        if isinstance(obj, bytes):
            return {"bytes": obj.hex()} #(test!)

        if isinstance(obj, CodeType):
            result = {}
            pub_attributes = list(
                filter(lambda obj: not obj.startswith('_'), dir(obj)))
            for attr in pub_attributes:
                result[attr] = self.serialize(obj.__getattribute__(attr))
            return {"code": result}
    
        if isinstance(obj, FunctionType):
            return {"func": self.serialize(obj.__code__)}
    
        if isinstance(obj, type):
            attribs = dict(obj.__dict__)
            for key,value in attribs.items():
                attribs[key] = self.serialize(value)
            attribs['__annotations__'] = None
            return {"sub_type": {"name": obj.__name__, "attribs": attribs}}

        if (getmodule(type(obj)).__name__ in sys.builtin_module_names or
            getmodule(type(obj)).__name__ == 'importlib._bootstrap' or
                getmodule(type(obj)).__name__ == '_sitebuiltins'):
            return None
        """When classes and objects"""
        obj_dict = self.serialize(obj.__dict__)
        obj_type = self.serialize(type(obj)) # one exception when isinstance(type) (check!)
        return {"object": {"obj_type": obj_type, "obj_dict": obj_dict}}


    def deserialize(self,obj: dict[str, any]) -> any:
        if not isinstance(obj, dict):
            return obj

        for (key, value) in obj.items():
            
            if key == 'tuple':
                if value is None:
                    return ()
                return tuple(self.deserialize(element) for element in value.values())
            if key == 'list':
                return [self.deserialize(element) for element in value.values()]
            if key == 'dict':
                return value
            if key == 'bytes':
                return bytes.fromhex(value)

            if isinstance(value, int | float | str):
                return value

            if key == 'sub_type':
                globals().update(__main__.__dict__)

                obj_type = getattr(__main__, value['name'], None)
                serialized = self.serialize(obj_type)

                if(serialized is None
                or isinstance(serialized, dict)
                and serialized['sub_type'] != value):
                    attribs = value['attribs']
                    for i in attribs.keys():
                        attribs[i] = self.deserialize(attribs[i])

                    obj_type = type(
                        value['name'],
                        (object, ),
                        attribs
                    )

                return obj_type

            if key == 'func':

                f_code = self.deserialize(value)

                def func():
                    pass
                func.__code__ = f_code
                return func

            if key == 'code':
                code_names = self.deserialize(value["co_names"])

                for name in code_names:
                    if builtins.__dict__.get(name, 42) == 42:
                        try:
                            builtins.__dict__[name] = importlib.import_module(name)
                        except ModuleNotFoundError:
                            builtins.__dict__[name] = 42

                return types.CodeType(
                    self.deserialize(value["co_argcount"]),
                    self.deserialize(value["co_posonlyargcount"]),
                    self.deserialize(value["co_kwonlyargcount"]),
                    self.deserialize(value["co_nlocals"]),
                    self.deserialize(value["co_stacksize"]),
                    self.deserialize(value["co_flags"]),
                    self.deserialize(value["co_code"]),
                    self.deserialize(value["co_consts"]),
                    code_names,
                    self.deserialize(value["co_varnames"]),
                    "deserialized",  # deserialize(value["co_filename"])),
                    self.deserialize(value["co_name"]),
                    self.deserialize(value["co_firstlineno"]),
                    self.deserialize(value["co_lnotab"]),
                    self.deserialize(value["co_freevars"]),
                    self.deserialize(value["co_cellvars"])
                )

            if key == 'object':
                obj_type = self.deserialize(value['obj_type'])
                obj_dict = self.deserialize(value['obj_dict'])

                try:
                    obj = object.__new__(obj_type)
                    obj.__dict__ = obj_dict
                    for (obj_key, obj_value) in obj_dict.items():
                        setattr(obj, obj_key, obj_value)
                except TypeError:
                    obj = None
                return obj

        return None