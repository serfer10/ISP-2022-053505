from sympy import im
import unittest
from serializers.json_serializer import JsonSerializer
from serializers.toml_serializer import TomlSerializer
from serializers.yaml_serializer import YamlSerializer

class Clerk():
            def __init__(self):
                age = 14
                name = "Oleg"
                number = [7,8,6,4,3,2]

def sum(one,two):
    return one + two
    
class JsonSerialzerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer_json = JsonSerializer()
        self.serializer_toml = TomlSerializer()
        self.serializer_yaml = YamlSerializer()
        
    
    def test_serialize_class_serialize_deserialize_json(self):
        expected_result = JsonSerializer
        test_instance = expected_result()
        result_ser = self.serializer_json.dumps(JsonSerializer)
        result_deser = self.serializer_json.loads(result_ser)
        result_instance = result_deser()
        self.assertEqual(type(result_instance),type(test_instance))
    
    
    def test_serialize_object_serialize_deserialize_with_file_json(self):
        person = Clerk()
        expected_result = person
        self.serializer_json.dump(person,'data_json')
        result_deser = self.serializer_json.load('data_json')
        self.assertEqual(type(result_deser),type(expected_result))
    
    def test_serialize_function_serialize_deserialize_json(self):
        expected_result = sum
        result_ser = self.serializer_json.dumps(sum)
        result_deser = self.serializer_json.loads(result_ser)
        self.assertEqual(type(result_deser),type(expected_result))
    
    def test_serialize_class_serialize_deserialize_toml(self):
        expected_result = TomlSerializer
        test_instance = expected_result()
        result_ser = self.serializer_toml.dumps(TomlSerializer)
        result_deser = self.serializer_toml.loads(result_ser)
        result_instance = result_deser()
        self.assertEqual(type(result_instance),type(test_instance))
    
    def test_serialize_object_serialize_deserialize_with_file_toml(self):
        person = Clerk()
        expected_result = person
        self.serializer_toml.dump(person,'data_toml')
        result_deser = self.serializer_toml.load('data_toml')
        self.assertEqual(type(result_deser),type(expected_result))
    
    def test_serialize_function_serialize_deserialize_toml(self):
        expected_result = sum
        result_ser = self.serializer_toml.dumps(sum)
        result_deser = self.serializer_toml.loads(result_ser)
        self.assertEqual(type(result_deser),type(expected_result))
    
    def test_serialize_class_serialize_deserialize_yaml(self):
        expected_result = TomlSerializer
        test_instance = expected_result()
        result_ser = self.serializer_yaml.dumps(TomlSerializer)
        result_deser = self.serializer_toml.loads(result_ser)
        result_instance = result_deser()
        self.assertEqual(type(result_instance),type(test_instance))
    
    def test_serialize_object_serialize_deserialize_with_file_yaml(self):
        person = Clerk()
        expected_result = person
        self.serializer_toml.dump(person,'data_yaml')
        result_deser = self.serializer_yaml.load('data_yaml')
        self.assertEqual(type(result_deser),type(expected_result))
    
    def test_serialize_function_serialize_deserialize_yaml(self):
        expected_result = sum
        result_ser = self.serializer_toml.dumps(sum)
        result_deser = self.serializer_yaml.loads(result_ser)
        self.assertEqual(type(result_deser),type(expected_result))

if __name__ == "__main__":
  unittest.main()