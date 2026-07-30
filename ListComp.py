#without list comprehension

numbers=[1,2,3,4,5,6]
squares=[]

for i in numbers:
    squares.append(i**2);
print(squares)
#--------------------------------------
#with list comprehension
numbers=[1,2,3,4,5,6]
squares=[num ** 2 for num in numbers];
print(squares)

#------------------------------------
names = ["john", "alice", "bob"]

upper_names = [name.upper() for name in names]

print(upper_names)
 #------------------------------
numbers = range(1, 11)
evens = [n for n in numbers if n % 2 == 0]
print(evens)
#---------------------------------------
numbers = range(1, 11)
odds = [n for n in numbers if n % 2 != 0]
print(odds)

#---------------------------------------------
numbers = [1, 2, 3, 4, 5]

result = [f"Even:{n}" if n % 2 == 0 else f"Odd:{n}" for n in numbers]

print(result)
#--------------------------------------------------