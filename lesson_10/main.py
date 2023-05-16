from datetime import datetime

# Task 2

def authenticate(func):
  def wrapper(*args, **kwargs):
    try:
      func(*args, **kwargs)
    except Exception as error:
      with open('log.txt', 'a') as log_file:
        log_file.write(f'{error.args[0]}. {datetime.now()} \n')

  return wrapper


# Task 1

@authenticate
def Login(login, password):
  if login == 'admin' and password == login:
    return True

  raise Exception("Invalid User")

Login('adsvadb0','adbda')


class User:
  def __init__(self, login, password):
    self.login = login
    self.password = password

  def do_login(self):
    if self.login == 'admin' and self.password == 'admin':
      return True

    raise Exception("Invalid User")



  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is not None:
      with open('log.txt', 'a') as log_file:
        log_file.write(f'{exc_val.args[0]}. {datetime.now()} \n')



us = User('admin', 'admin')
us.do_login()

# Research
# 1.	Ինչպես կարող ենք Decorator-ին փոխանցել parameter-եր

# @decorator_wrapper(a,b)
# mi hat decoratori wrapper enq sarqum u kanchum enq voncor verevy kanchelem, decoratory stanuma func veradarcnuma func-i wrapper









