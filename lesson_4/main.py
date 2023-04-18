# Task 1
# class A(object):
#   def __init__(self):
#     print("A")
#
# class B(A):
#   def __init__(self):
#     print("B")
#
# class C(A):
#   def __init__(self):
#     print("C")
#
# class D(B, C):
#   def __init__(self):
#     print("D")
#
# print(D.mro())

# ktpi list vori mech klinen parent classnery voric jarangvuma D class-y bayc ete unenq classner voronq unenq nuyn cnoxy et cnoxy mi angam ktpi,
# isk methodner ashxatacnelucel bnakanabar mi angam et classi vrayov kancni


# Task 2

from abc import ABC, abstractmethod

class AbstractFile(ABC):
  english_alphabet = ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'j', 'z', 'i', 'iy', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'shy', 'i', 'e', 'yu', 'ya']
  russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я']

  alphabets = dict(zip(english_alphabet, russian_alphabet))

  @abstractmethod
  def translate(self):
    pass

  @abstractmethod
  def write(self):
    pass

# 2.1

class EnglishFile(AbstractFile):

  def write(self):
    print('write')

  def translate(self, russian_text):
    print('translate')


f = EnglishFile()

print(f.alphabets)