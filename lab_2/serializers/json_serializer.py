from email import parser
import parsing as par
from serializer import Serializer

class JsonSerializer(Serializer):
    def dumps(self, item):
        parser_util = par.Parser()
        """Serialize object of any type to json."""
        def to_str(item):
            if isinstance(item, dict):
                strings = []
                for key, value in item.items():
                    strings.append(f'{to_str(key)}:{to_str(value)},')
                return f"{{{''.join(strings)[:-1]}}}"
            if isinstance(item, str):
                string = item.translate(str.maketrans({
                    "\"":  r"\"",
                    "\\": r"\\",
                }))
                return f"\"{string}\""
            if item is None:
                return 'null'

            return str(item)

        return to_str(parser_util.serialize(item))

    def loads(self, string):
        parser_util = par.Parser()
        null = None
        return parser_util.deserialize(eval(string))