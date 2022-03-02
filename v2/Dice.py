import random

class Dice:
  def __init__(self, sides):
    self.self = self
    self.sides = sides
    self.value = 0
  
  def getValue(self) -> int:
      return self.value

  def roll(self) -> None:
      self.value = random.randint(1, 6) * 10 // 10
      return

  def __repr__(self):
    return f"{self.value}"