from DiamondTrap import King
from S1E7 import Baratheon, Lannister
from S1E9 import Character, Stark


# Joffrey = King("Joffrey")
# print(Joffrey.__dict__)
# Joffrey.set_eyes("blue")
# Joffrey.set_hairs("light")
# print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print(Joffrey.__dict__)

# $> python tester.py
# {'first_name': 'Joffrey', 'is_alive': True,
# 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
# blue
# light
# {'first_name': 'Joffrey', 'is_alive': True,
# 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
# $>

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
print(Joffrey.__doc__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.__dict__)
if (isinstance(Joffrey, King) and issubclass(King, Character) and
        issubclass(King, Lannister) and issubclass(King, Baratheon)):
    print("OK")
else:
    print("Something seems fishy, look at the code to see if the class\
          king is inherited from the previous exercises")
print(issubclass(King, Stark) is not True)
