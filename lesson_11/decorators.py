from datetime import datetime

# Task 3

def handle_error_decorator(func):
  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as message:
      with open('log.txt', 'a') as log_file:
        log_file.write(f'{message} {datetime.now()}\n')

  return wrapper

# Task 2

def sensitive_data_decorator(size):
  def decorator(func):
    def wrapper():
      sensitive_data = func()
      if size > len(sensitive_data):
        raise ValueError('Size is greater than Sensitive Data Length!')
      return sensitive_data

    return wrapper

  return decorator