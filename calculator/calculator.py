import json
# This function adds two numbers
def add(x, y):
  return x + y

# This function subtracts two numbers
def subtract(x, y):
  return x - y

# This function multiplies two numbers
def multiply(x, y):
  return x * y

# This function divides two numbers
def divide(x, y):
  if (y == 0):
    raise ValueError('Cannot divide by Zero(0)')
  return x / y

#This function checks if the input is a number
def check_is_numeric (number):
  if (number.isnumeric()):
    return True
  return False


#Driver function
def lambda_handler (event, context):

    # Take input from the user
    choice = event['pathParameters']['choice']

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

      #Get the numbers from user
      first_num = event['pathParameters']['firstNumber']

      #Check is number
      if(check_is_numeric(first_num) == False):
        print("Invalid input")
        return {
          'statusCode': 400,
          'body': json.dumps({
            'message': 'Invalid input',
            'value': 'Bad input'
          })
        }

      else:
        num1 = float(first_num)

      second_num = event['pathParameters']['secondNumber']

      #Check is number
      if(check_is_numeric(first_num) == False):
        print("Invalid input")
        return {
          'statusCode': 400,
          'body': json.dumps({
            'message': 'Invalid input',
            'value': 'Bad input'
          })
        }
      
      else:
        num2 = float(second_num)
        
      if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
        return {
          'statusCode': 200,
          'body': json.dumps({
            'message': 'Addition operation',
            'value': add(num1, num2)
          })
        }

      elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
        return {
          'statusCode': 200,
          'body': json.dumps({
            'message': 'Subtraction operation',
            'value': subtract(num1, num2)
          })
        }

      elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
        return {
          'statusCode': 200,
          'body': json.dumps({
            'message': 'Multiplication operation',
            'value': multiply(num1, num2)
          })
        }

      elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
        return {
          'statusCode': 200,
          'body': json.dumps({
            'message': 'Division operation',
            'value': divide(num1, num2)
          })
        }

    else:
        print("Invalid Input")
        return {
          'statusCode': 400,
          'body': json.dumps({
            'message': 'Invalid operation',
            'value': 'Bad request'
          })
        }