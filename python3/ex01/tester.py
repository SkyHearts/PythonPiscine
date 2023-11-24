from S1E7 import Baratheon, Lannister


# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# # print(Robert.__str__())
# # print(Robert)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# Jaine = Lannister.create_lannister("Jaine", True)
# n = Jaine.first_name
# print(f"Name : {n, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


# $> python tester.py
# {'first_name': 'Robert', 'is_alive': True,
# 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
# <bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
# <bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
# True
# False
# Representing the Baratheon family.
# ---
# {'first_name': 'Cersei', 'is_alive': True,
# 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
# <bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
# True
# ---
# Name : ('Jaine', 'Lannister'), Alive : True
# $>

Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.__repr__)
print(Cersei.is_alive)
print(Cersei.__doc__)
print("---")
Twyin = Lannister.create_lannister("Tywin", True)
Twyin.die()
n = Twyin.first_name
print(f"Name : {n, type(Twyin).__name__}, Alive : {Twyin.is_alive}")
