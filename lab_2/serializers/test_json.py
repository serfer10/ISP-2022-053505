from json_serializer import JsonSerializer

def mul(first, second):
    """Function to check."""
    return first * second


def test_load():
    """Dump and load's file"""
    serializer = JsonSerializer()
    serializer.dump(serializer,'data_json')
    serializer = serializer.load('data_json')
    print(serializer)
    print(JsonSerializer())


def test_fun():
    """Function dumps and loads correct."""
    serializer = JsonSerializer()
    serialized = serializer.dumps(mul)
    res = serializer.loads(mul)
    print(res)

test_fun()