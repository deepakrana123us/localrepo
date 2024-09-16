Student = {
"student name" : "David" ,
 "Subjects" : {
     "sub1" : "Physiscs",
     "sub2" : "Maths"

} 
}
print(Student)  # print main dictionary
print(Student["Subjects"])  # Print nested dictionary
print(Student["Subjects"]["sub1"])  # print only one value

#print(Student.keys())  # only print outer keys, won't return nested keys .. so will print student name & subjects
#print(list(Student.keys()))  # type cast in list
#print(len(list(Student.keys())))  # can use len to return no of keys
#print(list(Student.values()))  # return keys of dictionary
#print(list(Student.items()))  # return number of pairs

# both will return the keys, but if we input the invalid key name, first one will give error but the second one using get won't give error, we deal with lot of keys 
# and code or getting keys from external source, we might use get method beucae one the error come using the first one, rest of the things will not process or print
print(Student["Subjects"])
print(Student.get("Subjects"))

# updating city in the existing dictonary by creating a new key value pair

Student.update({"City": "Delhi", "age" : 16})
print(Student)  # print main dictionary


