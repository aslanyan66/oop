def Login(login, password):
  if login and password == "admin":
    return True
  else:
    raise Exception("Invalid User")

Login('k', 'admin')