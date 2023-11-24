from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the legitimate king"""
    def __init__(self, name, is_alive=True):
        """Init the inherited class first"""
        super().__init__(name, is_alive)

    def set_eyes(self, col: str):
        """set eye color"""
        self.eyes = col

    def set_hairs(self, col: str):
        """set hair color"""
        self.hairs = col

    def get_eyes(self):
        """get eye color"""
        return self.eyes

    def get_hairs(self):
        """get hair color"""
        return self.hairs
