#project from 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu through Udemy 
logo = """
 _____________________
|  _________________  |
| | Jeff's first    | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |__calculator!____| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def  multiply(n1, n2):
  return n1 * n2
def devide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : devide
}
def calculator():
  print(logo)
  num1 = int(input("What's the first number?\n"))
  for item in operations:
    print (item)
    
  continuing=True
  while continuing:
    user_choice = input("pick an operation.\n")
    num2 = int(input("What's the next number?\n"))
    answer= operations[user_choice](n1 = num1, n2 = num2)
    print(f"{num1} {user_choice} {num2} = {answer}")
  
    if input("Would you like to continue using previous result? type n for 'no' and y for 'yes' \n").lower() == 'y':
      num1 = answer #this ensures that the continuation works as designed
    else:
      continuing = False
      calculator()
calculator()
