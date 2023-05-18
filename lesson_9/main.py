# Task 1

import os

'''
__del__-@ destructora aysinqn instance-i lifesycle u kanchvuma instance-i jnjveluc arach ,
 aysinqn garbage-i collector i galuc arach, mi hat mecavari inqna ashxatum.

isk __delete__-@ kanchvuma attributy jnjeluc arach
'''


# Task 2.~

class FileError(Exception):
  def __init__(self, message='Qo tiru nany grkem!!'):
    self.message = message

  def __str__(self):
    return self.message


class SingleError(FileError):
  def __init__(self, line: int, file_name: str):
    self.message = f'We came a cross to error on {line} line in {file_name.lower()} file.'


class ManyErrors(FileError):
  def __init__(self, lines: int, file_name: str):
    self.message = f'We came a cross to error on {",".join(lines)} lines in {file_name.lower()} file.'


# Task 2

class FileDescriptor:
  def __get__(self, instance, owner):
    with open(f'{instance.__class__.__name__.lower()}.txt', 'a') as file:
      return file

  def __set__(self, instance, value):
    with open(f'{instance.__class__.__name__.lower()}.txt', 'w') as file:
      self._file = file

  def __delete__(self, instance):
    os.remove(f'{instance.__class__.__name__}.txt')


class ChildFileDescriptor:
  def __get__(self, instance, owner):
    with open(instance.file.name, 'r') as file:
      text = file.read()

      errors = list(filter(lambda value: 'error' in value, text.split('\n')))
      errors_count = len(errors)

      if errors_count == 1:
        error_line = errors[0][0]
        raise SingleError(**{'line': error_line, 'file_name': owner.__name__.lower()})

      elif errors_count > 1:
        error_lines = list(map(lambda value: value[0], errors))
        raise ManyErrors(**{'lines': error_lines, 'file_name': owner.__name__.lower()})

      return text

  def __set__(self, instance, value):
    with open(instance.file.name, 'w') as file:
      file.write(value)

  def __delete__(self, instance):
    os.remove(f'{instance.__class__.__name__}.txt')


class File:
  file = FileDescriptor()
  child_file = ChildFileDescriptor()


class Tesla(File):
  pass


class Lexus(File):
  pass


# tesla = Tesla()
# print(tesla.child_file)  # 1,Model_S,Sedan,Electric ...
# tesla.child_file = 'New text about tesla'
# print(tesla.child_file) # New text about tesla

# del tesla.child_file  # remove tesla.txt file

# lexus = Lexus()
# print(lexus.child_file)  # 1,Lexus_IS,Sedan,Gasoline ...
# lexus.child_file = 'New text about lexus'
# print(lexus.child_file)
# del lexus.child_file  # remove lexus.txt file

try:
  tesla = Tesla()
  tesla.child_file
except FileError as err:
  print(err, 'errrorrrrr')
