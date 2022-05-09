from abc import abstractmethod

class Serializer:
    """Interface"""
    @abstractmethod
    def dumps(self, item: any) -> str:
        """Serialize object"""

    @abstractmethod
    def loads(self, string: str) -> any:
        """Deserialize object"""

    def dump(self, item: any, filename: str):
        """Serialize object and write to file."""
        with open(filename, 'w', encoding='utf8') as file:
            file.write(self.dumps(item))

    def load(self, filename: str):
        """Read from file object."""
        with open(filename, 'r', encoding='utf8') as file:
            string = file.read()
        return self.loads(string)