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

# ktpi list vori mech klinen parent classnery voric jarangvuma D class-y bayc ete unenq classner voronq unen nuyn cnoxy et cnoxy mi angam ktpi,
# isk methodner ashxatacnelucel mi angam et classi vrayov kancni


# Task 2

from abc import ABC, abstractmethod


class AbstractFile(ABC):
  english_alphabet = ['a', 'b', 'w', 'g', 'd', 'e', 'yo', 'j', 'z', 'i', 'ih', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's',
                      't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'shy', 'ii', 'e', 'yu', 'ya']
  russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                      'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я']

  alphabets = dict(zip(english_alphabet, russian_alphabet))
  alphabets.update(dict(zip(russian_alphabet, english_alphabet)))

  @abstractmethod
  def translate(self, text):
    pass

  def write(self, text, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
      file.write(f'{text}\n')


# 2.1

class EnglishFile(AbstractFile):

  # 2.2
  def translate(self, russian_text):
    english_text = ''

    for char in russian_text.strip().lower():
      if char == ' ':
        english_text += char
        continue
      english_text += self.alphabets[char]

    self.write(english_text)
    return english_text

  # 2.3
  def write(self, text, file_path = 'english_file.txt'):
    super().write(text, file_path)


class RussianFile(AbstractFile):

  # 2.4
  def translate(self, english_text):
    russian_text = ''

    for char in english_text.strip().lower():
      if char == ' ':
        russian_text += char
        continue
      russian_text += self.alphabets[char]

    self.write(russian_text)
    return russian_text

  # 2.4
  def write(self, text, file_path = 'russian_file.txt'):
    super().write(text, file_path)

# english_file = EnglishFile()
# russian_file = RussianFile()
#
# english_file.translate('писат')
# russian_file.translate('hello world')


# 2.5

# erkusneel karan mnan abstract , bayc karanq sarqenq mi hat parent class et erkusi hamar vory impliment kani et erku methody,
# heto jarangvenq parentic u use anenq et erku methody, konkret es depqi hamar

# Research
# 1. super() in multiple inheritance

# super darnum en parent classnery u MRO-i mijocov hertov frum enq classneri vrov
