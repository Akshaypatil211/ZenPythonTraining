#for loop demo
#example
fruits=["Apple","Banana","Orange"]
for i in fruits:
    print(i);

for index,fruit in  enumerate(fruits):
    print(f"{index}:{fruit}")
print(fruits[2])

#example 2
total=0

for num in range(1,6):
    total+=num
print(f"Sum:{total}")
#------------------------------------------------------------------------
#while loop

count=1
while count <=5:
    print(count)
    count+=1;

#break-------------------------------------------------------------------------

total=0
print("break test")
for num in range(1,11):
    total+=num
    if total >15:
        print(f"num:{num}")
        break;
print(f"total:{total}")
#contiune-------------------------------------------
print("Contiune test")

for i in range(1,6):
    if i == 3:
        continue;
    print(i)