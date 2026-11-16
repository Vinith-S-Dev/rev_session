class Animal:
  def speak(self):
    return "..."
class Dog(Animal):
  def speak(self):
    return "woof"
for pet in [Dog(),Animal()]:
  print(pet.speak())
