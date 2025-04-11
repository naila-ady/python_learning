# a program to ask input thrice and add the all in list using append
# fruits=[]
# user_input1=input("enter ur favoutite fruit:")
# user_input2=input("enter ur favoutite fruit:")
# user_input3=input("enter ur favoutite fruit:")
# fruits.append(user_input1)
# fruits.append(user_input2)
# fruits.append(user_input3)
# print(fruits)
# shorter way
# fruitss=[]
# fruitss.append(input("enter ur favoutite fruit:"))
# fruitss.append(input("enter ur favoutite fruit:"))
# fruitss.append(input("enter ur favoutite fruit:"))
# print(fruitss)
# a program to check wether the list is palindrome or not (usse copy /reverse method)
# cars=["corolla","revo","bogati" ,"revo" ,"corolla"]
# copy_cars=cars.copy()
# print(copy_cars)
# copy_cars.reverse()
# if cars == copy_cars:
#     print(f"cars list is palindrome {copy_cars}")
    
# else:
#     print(f"cars list is not a plaindrome{copy_cars} ")
# transport=["aeroplane" , "bus","car","ship"]
# copy_transport=transport.copy()
# print(copy_transport)
# copy_transport.reverse()
# if transport == copy_transport:
#     print(f"transport list is a palindrome{copy_transport}")
    
# else:
#     print(f"transport list is not a palindrome{copy_transport}")
# a program to convert the list in ascending order
grades=["C" ,"D","A","A","B","B","A"]
grades.sort()
print(grades)
# second way
sortedlist=sorted(grades)
print(sortedlist)
print(grades[1:4])#['A', 'A', 'B']
print(grades[ :4])#['A', 'A', 'A', 'B'] will start from index no 1 and end on 3
print(grades[1:])# will print whole length of list
#.pop will remove the element on 4th index
num=[23,34,45,56,56,67,23,45]
num.pop(4)
print(num)
#remove it will remove the first occurance of element
num.remove(45)
print(num)
#insert it will go to index3 and add"adnan"
num.insert(3,"adnan")
print(num)