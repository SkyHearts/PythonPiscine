import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class with dataclass"""
    name: str = field(init=True)
    surname: str = field(init=True)
    id: str = field(init=False, default=generate_id())
    login: str = field(init=False)
    active: bool = field(init=False, default=True)

    def __post_init__(self):
        """Init after dataclass init"""
        self.login = self.name[0] + self.surname
