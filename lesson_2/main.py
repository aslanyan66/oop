# Task 1.1

class Car:
  headlights_count = 4
  wheels_count = 4

  def __init__(self, horsepower: int, weight: int, engine_type: str):
    self.horsepower = horsepower
    self.weight = weight
    self.engine_type = engine_type

  # 1.2
  def get_max_speed(self):
    return int(self.horsepower / self.weight * 1500)

  # 1.3
  @classmethod
  def change_headlights_count(cls, count):
    cls.headlights_count = count

  # 1.4
  @staticmethod
  def change_wheels_count(val=4):
    Car.wheels_count = val


# Task 2

class Bus(Car):
  # 2.1
  def __init__(self, horsepower: int, weight: int, engine_type: str, max_seats: int, busy_seats: int = 0):
    super().__init__(**{'horsepower': horsepower, 'weight': weight, 'engine_type': engine_type})
    self.max_seats = max_seats
    self.busy_seats = busy_seats

  # 2.2
  def change_busy_seats(self, busy_seats):
    if busy_seats > self.max_seats:
      raise ValueError('Chi karox patahel xose ignasyo')
    self.busy_seats = busy_seats
    return self

  # 2.3
  def get_free_seats(self):
    return self.max_seats - self.busy_seats


bogdan = Bus(**{'horsepower': 1200, 'weight': 2000, 'engine_type': 'V12', 'max_seats': 25, 'busy_seats': 24})

# 2.4
print(bogdan.get_max_speed())

# Research

# Ինչ տարբերություն կա class-ի __dict__ attribute-ի և dir() function-ի միջեվ:

# __dict__-@ veradarcnuma tvyal object-i key value-ner@ dict-i mej, __dict__-@ menak objectneri hamara
# dir()-@ veradarncuma list vori mech current scopi methodneri, attributneri, popoxakanneri, function argumentneri =>
# sortavorvac anunnern en linum

