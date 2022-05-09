import parsing as par
from serializer import Serializer
import yaml

class YamlSerializer(Serializer):

    def dumps(self, item):
        pars = par.Parser()
        return yaml.dump(pars.serialize(item), encode_none=())

    def loads(self, string):
        pars = par.Parser()
        return pars.deserialize(yaml.load(string))
