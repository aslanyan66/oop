from datetime import datetime
def decor_for_error(func):
    def wrapper():
        try:
            return func()
        except Exception as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f'{e} | {datetime.now()}\n')
    return wrapper

def decorator_for_sensitive_data(size):
    def wrapper(func):
        def wrap():
            long_size = func()
            if len(long_size) < size:
                raise Exception("error")
            return long_size

        return wrap

    return wrapper

# @decor_for_error
# @decorator_for_sensitive_data(15)
def get_sensitive_data():
  users = []
  with open("passwords.txt", "r") as f:
    for i, j in enumerate(f):
      if i == 0:
        continue
      else:
        users.append(j.strip().split(','))

  list_of_users = []

  for name, password in users:
    users_dict = {
        name: password
    }

    list_of_users.append(users_dict)

  return list_of_users


wraped_sensitive = decorator_for_sensitive_data(15)(get_sensitive_data)

decorated_sensitive_data = decor_for_error(wraped_sensitive)

decorated_sensitive_data()