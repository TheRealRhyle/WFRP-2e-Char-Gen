
import genchar

# class Character:
#     def __init__(self, name):
#         self.name = name

gc = genchar.build_random_char()
# c1 = Character(gc['name'])
for key in gc:
    print(key + ': ' + str(gc[key]))





"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"""