# 1. call vs new vs init
# 2. object vs type
class CallableClass:
  def __call__(self, *args, **kwargs):
    print("Calling the object")


obj = CallableClass()
obj()  # Outputs: "Calling the object"

'''
__call__-@ tuyla talis instance-@ kanchenq vorpes function aysinqn instance-@ vorpes function kanchelu hamar patasxanatuya,
__call__ magic methody
'''


class MyClass:
  def __new__(cls, *args, **kwargs):
    print("Creating a new instance")
    return super().__new__(cls)

  def __init__(self, *args, **kwargs):
    print("Initializing the instance")


obj = MyClass()  # Outputs: "Creating a new instance" followed by "Initializing the instance"

'''
  erp vor class-ic uzum enq instance stananq skzbic ashxatuma __new__ magic methody vory patasxanatuya nor object stexcelu hamar,
  aysinqn tvyal class-i __new__ methody kanchuma super-i __new__ methodin u tenc enqan kara barcrana minchev hasnenq root object-in
  , root object-i __new__ methody allocate-a anum taracq hishoxutyan mech , stexcuma nor object u talisa __init__-in vornel patasxanatuya,
  attributneri stexcman hamar
'''