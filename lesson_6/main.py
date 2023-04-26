# Task 1

# kaxvac te inch type-i object enq ogtagorcum, nuyn operatory tarber gorcoxutyunnera anum, aysinqn operators overloading-a ashxatum
# u objecti methody kara unena tarber derer kaxvac iran ekac argumentneric, et jamanakel karanq ashaxatcnenq function overloading@


# Task 2
class TeslaMotors:
  names = ['Model S', 'Roadster', 'Model 3', 'Cybertruck', 'Model Y', 'Model X']
  body_types = ['Sedan', 'Coupe', 'Sedan', 'Truck', 'SUVS', 'SUVS']
  engine_types = ['Electric', 'Electric', 'Electric', 'Electric', 'Electric']
  start = 0
  end = len(names)

  def __init__(self, main_iter='names'):
    self.main_iter = main_iter

  def __iter__(self):
    return iter(getattr(self, self.main_iter))

  def __next__(self):
    if self.start < self.end:
      self.start += 1
      return self[self.end]
    self.start = 0
    return StopIteration

  def set_iter_by(self, key):
    self.main_iter = key

  def __contains__(self, item):
    try:
      getattr(self, self.main_iter).index(item)
      return True
    except ValueError:
      return False


tesla = TeslaMotors()


for item in tesla:
  print(item)

tesla.set_iter_by('body_types')
print('------------------')

for item in tesla:
  print(item)


print('Model S' in tesla)


# Research
#	1. __call__ method:
# __call__ methodov hnaravorutyun enq talis instance-in iran function-i nman kanchelu u voroshum enq te inch lini et jamanak
#	2. <, >, operators
# __lt__-n less thanna kashxati poqri nshani jamanak, __gt__n kashxati meci nshani jamanak.. aysinqn tuyla talis voroshenq te
# instancenerin hamemateluc meci kam poqri nshanov inch pahaladzev unen tvyal instancenery