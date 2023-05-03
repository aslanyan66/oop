import os

# Task 3

class File:
  def get_file(self):
    with open(f'{self.__class__.__name__.lower()}.txt', 'a') as file:
      return file

  def set_file(self, path):
    with open(f'{path.lower()}.txt', 'w') as file:
      self._file = file

  @property
  def child_file(self):
    with open(self.file.name, 'r') as file:
      return file.read()

  @child_file.setter
  def child_file(self, text):
    with open(self.file.name, 'w') as file:
      file.write(text)

  @child_file.deleter
  def child_file(self):
    os.remove(f'{self.__class__.__name__}.txt')

  file = property(get_file, set_file)
  # child_file = property(get_child_file, set_child_file, del_child_file)


class Tesla(File):
  pass

class Lexus(File):
  pass

# tesla = Tesla()
# print(tesla.child_file)  # 1,Model_S,Sedan,Electric ...
# tesla.child_file = 'New text about tesla'
# print(tesla.child_file) # New text about tesla
#
# del tesla.child_file  # remove tesla.txt file



# lexus = Lexus()
# print(lexus.child_file)  # 1,Lexus_IS,Sedan,Gasoline ...
# lexus.child_file = 'New text about lexus'
# print(lexus.child_file)
# del lexus.child_file  # remove lexus.txt file


# Research
# 1.  file = open("new_file.txt")
# Ոնց կարանք ստանալ արդեն open արած ֆայլի անունը file object-ից("new_file.txt" string-ը վերը նշված օրինակից)
# file.name

# 2.  remove file
# os.remove('filename.txt')

# 3.  rename file name
# os.rename("old_filename.txt", "new_filename.txt")
