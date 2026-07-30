print("This is the simple calculator ")
#This is function for adding 2 numbers 
def add(x,y):
    return x+y
#This is function for subtracting 2 numbers 
def subtract(x,y):
    return x-y
#This is function for multiplying 2 numbers 
def multiply(x,y):
    return x*y
#This is function for dividing 2 numbers 
def divide(x,y):
    #we adding this for dividing by zero is not allowed in mathematices 
    if y==0:
         raise ValueError("Division by zero not allowed.")
    return x/y
#print(add(1,2))
#adding new 
def main():
    print("Simple Calculator")
    print("select the operation want to perform 1.Add 2.Subtarct 3.Multiply 4.Divide")
    #print("Enter the operation choice number:")
    ch=int(input("Enter the operation choice number"))
    if ch not in (1,2,3,4):
        print("Invaild choice please slect in 1,2,3 or 4 :")
        return
    num1=float(input("Enter the first number :"))
    num2=float(input("Enter the second number :"))

    if ch==1:
        result=add(num1,num2)
    elif ch==2:
            result=subtract(num1,num2)
    elif ch==3:
            result=multiply(num1,num2)
    elif ch==4:
            result=divide(num1,num2)
    print(result)

main()