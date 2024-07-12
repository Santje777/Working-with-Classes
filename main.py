class User:
  """Defines a User class"""

  def __init__(self):
    """Initializes a new user"""
    print("Hello from the User class")


matt = User()
emilie =  User()
maria = User()

class Dog:
  def __init__(self, name, age):
    """Initiaze the dog"""
    self.name = name
    self.age = age
    self.healthy = True

  def say_hello(self):
    """Say hello with the dog name"""
    print(f"Hello, I'm a dog named {self.name}")
    print(f"I'm {self.age} years old")

  def get_older(self):
    self.age = self.age + 1

  def rename(self, new_name):
    self.name = new_name

  def is_sick(self):
    self.healthy = False

  def is_healthy(self):
    self.healthy = True


snoopy = Dog("Snoopy", 2)
snoopy.say_hello()
snoopy.get_older()
snoopy.rename("Jimmy")
snoopy.say_hello()
snoopy.is_sick()
print(snoopy.healthy)

class Dog:
  """Define a dog"""
  def __init__(self, name, age = 0):
    """ Initiaze a dog with name and age """
    self.name = name
    self.age = age

  def greet(self):
    """ Return a dog greeting """
    return f"Hello, I'm a {self.casual_name()} named {self.name}"


  def casual_name(self):
    """ Determine the dog name based on the age"""
    if self.age < 2:
      return "puppy"
    elif self.age < 10:
      return "grown up dog"
    else:
      return "old dog"


snoopy = Dog("Snoopy")
print(snoopy.greet())


from dog import Dog
from cat import Cat

snoopy = Dog("Snoopy")
print(snoopy.greet())

jimmy = Cat("Jimmy")
print(jimmy.greet())