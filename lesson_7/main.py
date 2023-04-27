# Task 1

# __getattr__-n kancvhvuma erp vor inchvor attribut enq get anum, __getattribute__-el en jamanak erpvor chi gtnum attributy


# Task 2

# private attributneri aravelutyuny ena vor karanq ogtagorcenq menak classneri mech, bayc nayev tuyla talis kanchel classic durs.


# Task 3

from typing import Literal

class God:
  def __init__(self, first_name: str, count_of_hands: int, super_power: str):
    self.first_name = first_name
    self.count_of_hands = count_of_hands
    self.super_power = super_power

  def clap(self):
    if self.count_of_hands >= 2:
      self._voice_after_clap()

  def _voice_after_clap(self):
    return 'ճլտ'

  def _get_access_modifiers(self, modifier: Literal['public', 'private', 'protected']):
    is_current_modifier = {
      'public': lambda name: name[0] != '_',
      'protected': lambda name: name[0] == '_' and name[1] != '_',
      'private': lambda name: name[0:2] == '__',
    }
    props = []
    for current_class in self.__class__.mro():
      if current_class == object:
        continue

      for key, value in current_class.__dict__.items():
        if is_current_modifier[modifier](key):
          props.append({key: value})

    return props


class Zeus(God):
  age = 200000
  _weight = '500kg'
  __height = '2 metr'

  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def sayHi(self):
    return 'Hi!'

  def _sayBye(self):
    return 'Bye!'

  def __jump(self):
    return 'Jump Jump Jump!'


class Herkules(Zeus):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def get_public(self):
    return self._get_access_modifiers('public')

  def get_protected(self):
    return self._get_access_modifiers('protected')

  def get_private(self):
    return self._get_access_modifiers('private')


hercules = Herkules(**{'first_name': 'herco', 'count_of_hands': 2, 'super_power': 'moshni'})

print(hercules.get_public())
print(hercules.get_protected())
print(hercules.get_private())


# Research
# 	1.	__slots__ attribute:
# __slots__-ov voroshum enq te inch attributnera unenalu mer instance-y, u azatvum enq mnacac default attributneric,
# npataky ena vor optimizacnenq memory usage-y, aysinqn ete unenalu enq tvyal class-ic shat instance-ner karanq __slots__-ov optimizacnenq.

# 	2.	property() function:
#    property-i mijocov getter, setter, deleter enq talis property-in