# Question 1 Task 1
def add_numbers(a,b):
    return a + b
result = add_numbers(5,6)
print(result)

def mult_numbers(a,b):
    return a * b
result = mult_numbers(5,6)
print(result) 

def sub_numbers(a,b):
    return a - b
result = sub_numbers(5,6)
print(result) 

def div_numbers(a,b):
    return a/b 
result = div_numbers(5,6)
print(result)

# Question 1 Task 2
calculator = input("Choose an operation: add, subtract, multiply, divide ")
if calculator == "add":
    num1 = int(input("Input first integer: "))
    num2= int(input("Input second integer: "))
    solution = num1 + num2
    print(solution)
elif calculator == "subtract":
    num1 = int(input("Input first integer: "))
    num2= int(input("Input second integer: "))
    solution = num1 - num2
    print(solution)
elif calculator == "multiply":
    num1 = int(input("Input first integer: "))
    num2= int(input("Input second integer: "))
    solution = num1 * num2
    print(solution)
elif calculator == "divide":
    num1 = int(input("Input first integer: "))
    num2= int(input("Input second integer: "))
    solution = num1 / num2
    print(solution)

# Question 1 Task 3


calculator = input("Choose an operation: add, subtract, multiply, divide ")
if calculator == "divide":
    num1 = int(input("Input first integer: "))
    num2= int(input("Input second integer: "))
elif calculator == "divide":
        if num2 == 0:
            print("INVALID, cannot divide by zero")
        else:
            result = num1 / num2
        print(result)
        


# Question 2 Task 1 

cart = []
print("What ya need from da sto'? ")
while True:
        user_input= input("Tell us what youd like to add to your cart or say 'quit' to quit: ")
        if user_input == "quit":
                print("Thanks for shopping here")
                for item in cart:
                        print(item)
                break
        else:
                cart.append(user_input)
                print(f"Your cart so far {cart}")   


# Question 2 Task 2 & 3    

cart = []
print("What ya need from da sto'? ")
while True:
        user_input= input("Add to your cart say 'remove' to remove an item or say 'quit' to quit: ")
        if user_input == "quit":
                print("Thanks for shopping here")
                for item in cart:
            

                        print(item)
                break
        elif user_input == "remove":
                momma_said_no = input("What item would you like to remove?")
                if momma_said_no in cart:
                    cart.remove(momma_said_no)
                    print("Good choice")
                
            
                    
                
                print(cart)
                
                        
        else: 
                cart.append(user_input)
                print(f"Your cart so far {cart}") 



