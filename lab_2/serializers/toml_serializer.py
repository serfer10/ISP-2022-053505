import qtoml
import parsing as par
from serializer import Serializer


class TomlSerializer(Serializer):

    def dumps(self, item):
        pars = par.Parser()
        return qtoml.dumps(pars.serialize(item), encode_none=())

    def loads(self, string):
        pars = par.Parser()
        return pars.deserialize(qtoml.loads(string))
