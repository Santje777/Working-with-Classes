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