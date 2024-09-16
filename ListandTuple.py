
#this is a new feature
#string are inmutable in python and lists are mutable
marks = [12,34,55.6,78,99,"student"]
print(marks)
marks[5] = "student1"
print(marks)  # lists are mutable, now marks[5] value is changed, but this is not possible in case of stringss
print(len(marks))
print(marks[1])
print (marks[1:4]) #sub lists or list slicing

marks1 = [12,34,55.6,78,99,23]
marks1.sort()
print(marks1)
marks1.sort(reverse=True)

marks1.append("22") # appending the list
print(marks1)
marks1.reverse
print(marks1)
marks1.insert(2,45) ## insert at partifcuar indes
print (marks1)
marks1.remove(34) # remove first occurence
print(marks1)
marks1.pop(2) # remove at particual position
print(marks1)

# tuple works like list, its a built in data type, and tuple is inmutable, not like list becuase lists are mutable, tuples are fixed, no add or remove elements, process is same, it's just that we use paranthesis
tup = (1,2,3)
print(type(tup))
# tup(0)= 5 - cannot use this because cannot assign to tuples like list

tup1 = () # can create empty tuple
tup1= (1,) # can create single value tuple, but use , in the last otherwise python will consider it like a normal integer assignment
print(tup[1:2])
print(tup.index(2))  # find the index of 2 number
print(tup.count(2))





