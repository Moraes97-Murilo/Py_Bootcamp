#just testing the while function
operations = ("+","-","*","/","1","2","3","4")
print("--- Welcome to my Awesome Calculator! ---")
flag = True
while flag:
    print("\nSelect the mathematical operation to be performed:\n")
    op = input("1) +\n2) -\n3) *\n4) /\n----> ")
    
    if op in operations:
        pass
    else:
        print("Awesome calculator can't run unknown operations.")
        continue
    a = float (input ("Type the first number: ")) 
    b = float (input ("Now, type second number: ")) 

    if op == "1" or op == "+":
        print(f"The result is {a+b} !")    
    elif op == "2" or op == "-":
        print(f"The result is {a-b} !")
    elif op == "3" or op == "*":
        print(f"The result is {a*b} !")  
    elif op == "4" or op == "/":
        print(f"The result is {a/b} !") 
    op = input("Type YES to run another operation or anything else to stop: ").upper()
    if op != "YES":
        flag = False
    else:
        pass
print("\nThanks for using Awesome Calculator.\n")