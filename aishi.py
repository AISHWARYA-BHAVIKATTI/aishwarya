print("Hello World")

age=18
if age>=18:
    print("you are eligible to vote")

num=8
if num%2==0:
    print("even number")
else:
    print("odd number")

marks=82
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
else:
    print("grade D")

for i in range(1, 6):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

    for i in range(1, 4):
        for j in range(1, 4):
            print(i, j)

numbers=[1,2,3]
numbers.append(4)
print(numbers)
list1=[1,2]
list2=[3,4]
list1.extend(list2)
print(list1)
fruits = ["apple", "banana"]
fruits.insert(1,"cherry")
print(fruits)
colors = ["red", "green", "blue"]
colors.remove("blue")
print(colors)
nums=[10,20,30,40,50]
nums.pop(1)
print(nums)
data=[1,2,3 ]
data.clear()
print(data)
names=["john","jane","jhope","jony"]
print(names.index("jony"))
marks=[90,80,90,70]
print(marks.count(90))
nums=[4,1,3,2]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
a=[1,2,3]
b=a.copy()
print(b)
items=["pens","book","bag"]
print(len(items))