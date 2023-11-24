from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characther"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Characther class constructor"""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """Commit sepukku"""
        self.is_alive = False


class Stark(Character):
    """Stark class which uses character abstract class"""
    def __init__(self, name, is_alive=True):
        """Stark class constructor"""
        self.name = name
        self.is_alive = is_alive
