from datetime import datetime


class Car:
  def __init__(self, model: str, brand: str, color: str, year: int | str, started: bool):
    self.brand = brand
    self.model = model
    self.color = color
    self.year = year
    self.started = started

  def start(self):
    self.started = True
    return 'br br br start'

  def stop(self):
    self.started = False
    return self

  # 2.2
  def get_descr(self):
    return f'{self.brand} {self.model}'

  # 2.3
  def get_age(self):
    current_year = int(datetime.now().year)
    return current_year - self.year

  # 2.4
  def set_color(self, color: str):
    self.color = color
    return self


audi = Car(**{'brand': 'audi', 'model': 'a4', 'color': 'red', 'year': 2016, 'started': False})
bmw = Car(**{'brand': 'bmw', 'model': 'x1', 'color': 'red', 'year': 2016, 'started': False})

# 2.1
audi.start()
bmw.start()

print(audi.__dict__)
print(bmw.__dict__)

audi.get_age()

# print(audi.__dict__)

# Research
# Ինչ են constructor-ը և destructor-ը և որ method-ների միջոցով են ռեալիզացված python-ում:

# erkusnel objecti life-cycle ner en , constructory ashxatuma objecti stexcveluc __init__ i mijocov
# destructor-nel ashxatuma objecti jnjveluc arach, aysinqn minchev garbage-i galy mer class-i meji __del__ methody
