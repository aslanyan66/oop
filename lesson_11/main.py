from decorators import sensitive_data_decorator, handle_error_decorator


# Task 1

@handle_error_decorator
@sensitive_data_decorator(11)
def get_sensitive_data():
  with open('passwords.txt') as passwords_file:
    result = []
    for line in enumerate(passwords_file):
      if line[0] == 0:
        continue

      [name, password] = line[1].strip().split(',')
      result.append({name: password})
  return result


user_passwords = get_sensitive_data()
print(user_passwords)

# Research
# 1.	class-ով decorator-ի պարամետր:

# classneri hamar nuynpes karanq decorator sarqneq, karanq class-ov henc decorator sarqenq u veradarcnenq nor class wrapper ,
# current classi hamar, kam karanq function decorator sarqenq u eli ceradarcnenq wrapper class