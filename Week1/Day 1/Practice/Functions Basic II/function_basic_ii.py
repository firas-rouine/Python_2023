#Countdown
def Countdown(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list
print(Countdown(10)) 
#Print and Return
def print_and_return(list):
    print (list[0])
    return list[1]
print(print_and_return([1,2]))
#First Plus Length
def first_plus_length(list):
    sum=list[0]+len(list)
    return sum
print(first_plus_length([1,5,2,7,6,2]))
#Values Greater than Second 
def values_greater_than_second(list):
    list_great=[]
    if len(list)>2:
        for i in range(len(list)):
            if(list[i]>list[1]):
                list_great.append(list[i])
        return list_great
    else:
        False
print(values_greater_than_second([3,4,4,5,7,6]))
#This Length, That Value    
def length_and_value(a,b):
    list=[]
    for i in range (a):
        list.append(b)
    return list
print(length_and_value(8,5))
            
        