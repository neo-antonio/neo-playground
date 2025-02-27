password = input("Input a new password here: ")
security_question = input("Input backup recovery password: ").lower()

def password_query():
  global password
  global check_security_question

  count_attempt = 0
  
  while count_attempt < 3:
    
    if input("Please input password: ") == password:
      print("Access granted!")
      print("Welcome to the program!")
      break
    count_attempt += 1
    print(f"Wrong password, please try again. Attempt {count_attempt}/3")
    
    if count_attempt == 3:
      print("You have exceeded the allowed number of attempts.\nPlease answer the security question.\nYou only have 1 attempt.\n")
      check_security_question = input("Input backup recovery password: ").lower()
      global security_question
    
      if check_security_question == security_question:
        count_attempt = 0
        print("Password recovery activated.")
        password = input("Change your password: ")
        security_question = input("Change your backup recovery password: ").lower()
        password_query()
        return

      else:
        print("Incorrect answer. Exiting the program")
        break



