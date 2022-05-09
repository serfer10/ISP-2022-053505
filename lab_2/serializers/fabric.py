"""Fabrics that can create serializer."""
from abc import abstractmethod
from .serializer import Serializer
from .json_serializer import JsonSerializer
from .yaml_serializer import YamlSerializer
from .toml_serializer import TomlSerializer

class SerializerFabric:
    """Fabric that can create serializer."""

    @staticmethod
    @abstractmethod
    def create_serializer() -> Serializer:
        """Create serializer."""

class JsonSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> Serializer:
        return JsonSerializer()


class YamlSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> Serializer:
        return YamlSerializer()


class TomlSerializerFabric(SerializerFabric):

    @staticmethod
    def create_serializer() -> Serializer:
        return TomlSerializer()