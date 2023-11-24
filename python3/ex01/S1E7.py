from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, is_alive=True):
        """Init parent class first before child class"""
        super().__init__(name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Set a string"""
        return 'Vector:' + str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """Set a string"""
        return 'Vector:' + str((self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, name, is_alive=True):
        """Init parent class first before child class"""
        super().__init__(name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def create_lannister(name, is_alive=True):
        """Create and return new Lannister"""
        new_lanister = Lannister(name, is_alive)
        return new_lanister

    def __str__(self):
        """Set a string"""
        return 'Vector:' + str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        """Set a string"""
        return 'Vector:' + str((self.family_name, self.eyes, self.hairs))
