# Task 1

class Animal:

  # Task 5
  """
  This is Animal class. ... ...
  """

  # 1.1

  def __init__(self, eyes: str, hands: int, lags: int, color: str, running_speed: str = "45(km/h)"):
    self.eyes = eyes
    self.hands = hands
    self.lags = lags
    self.color = color
    self.running_speed = running_speed

  # 1.2

  def get_voice(self):
    return 'Dzayn em hanum'

  # 1.3

  def get_running_speed(self):
    return f'Vazum em {self.running_speed} aragutyamb.'

  # Task 4
  def __str__(self):
    return f'Animal {self.color}'



# Task 2

class Cat(Animal):
  # Task 5
  """
  This is Cat class. ... ...
  """


  def __int__(self, **cat_data):
    super().__int__(**cat_data)

  # 2.1
  def get_voice(self):
    return 'mlavelu ' + super().get_voice()

  # 2.2

  def start(self):
    self.get_voice()
    super().get_running_speed()
    return self

  # Task 4
  def __str__(self):
    return f'{self.__class__.name} {self.color}'


# Task 3
class Lion(Cat):
  # Task 5

  """
  This is Lion class. ... ...
  """

  def __int__(self, **lion_data):
    super().__int__(**lion_data)

  def eat_human(self):
    return 'Hamov er'

  # Task 4
  def __str__(self):
    return 'Lion class'


lion = Lion(**{'eyes': 'kanach', 'hands': 2, 'lags': 2, 'color': 'yellow', 'running_speed': '60(km/h)'})

# Task 5
print(Lion.__bases__)
print(issubclass(Lion, Cat))

# Research
# 1. __doc__ attribute
# cuyca talis class-i documentation-@

# 2. __bases__ attribute
# bases ov stanum enq tuple-i mej en classnery voric jaragnvuma current@

# 3. issubclass() function
# stanuma 2 argument stugum en arachiny sub classa erkrordi hamar te che, veradarcnuma True kam False

