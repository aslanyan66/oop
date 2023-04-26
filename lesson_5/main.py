import re

# Task 1
'''
  karch asac oop-i principa vory tuyla talis Type-erin jarangvel iraric u darcnel aveli parz mer logikan,
  azatelov codei duplicationneric. Aysinqn inheritance-i jamanak mi objecty mekic kara lini aravel kam lracnox.
'''


# Task 2

'''
  Abstaction-y oop-i principa vory iranic entadruma vercnel irakan Objectic en bnutagrichnery voronq mer xndri lucman hamar
  imast unen. U shat karevora te um hamar enq Objectin abstractciayi entrakum aysinqn ova Observer-@.
  
  Aravelutyun@ ena vor iranic instance chenq stanum menak jarangvum enq u ira mech grac bolor bnutagrichnery petqa implement anenq.
'''


# Task 3

class FilterText:
  def __init__(self, text):
    self.text = text

  def __getitem__(self, index):
    return self.text.split(' ')[index]

  def __setitem__(self, index, value):
    text = self.text.split(' ')
    text[index] = value
    self.text = ' '.join(text)
    return self.text

  def __getattr__(self, key):
    if key == 'names':
      pattern = r'[A-Z]*[.][A-Za-z]+'
      return re.findall(pattern, self.text)
    elif key == 'dates':
      pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}'
      return re.findall(pattern, self.text)
    elif key == 'phone_numbers':
      pattern = r'\b\d{3}\-\d{3}\-\d{3}'
      return re.findall(pattern, self.text)


# 3.1
x = FilterText('055-445-789 E.Mask 124.06.2014 093-587-135 Nemo 1.09.1887 E.Auditore 24.17.2020 096-2288-987 R.Rocknrolla')

print(x.names)  # ['E.Mask', 'E.Auditore', 'R.Rocknrolla']
print(x.dates)  # ['1.09.1887', '24.17.2020']
print(x.phone_numbers)  # ['055-445-789', '093-587-135']

# 3.2
print(x[1])   # E.Mask
print(x[1:3]) # ['E.Mask', '124.06.2014']

# 3.3
x[0] = 'G.Ritchie'
print(x.text)  # G.Ritchie E.Mask 124.06.2014 093-587-135 Nemo 1.09.1887 E.Auditore 24.17.2020 096-2288-987 R.Rocknrolla


# Research
# 1. __bool__ method
# __bool__ nra hamara vor instanc-ic boolean arjeq stananq
# 2. __len__ method
# __len__-ov length karanq tanq mer instance-nerin
# 3. if գրելու դեպքում նախորդ method-ներից որին է տրվում առավելություն:
# misht stuguma skzbic __bool__ heto __len__

