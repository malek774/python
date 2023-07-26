print('Countdown')
def Countdown(num):
    my_list = []
    for i in range(int(num)+1):
        my_list.append(i)
    
    print(my_list)
num = input('Enter a Number : ')
Countdown(num)

print('Print and Return')
def Print_and_Return(list):
    print(list[0])
    return list[1]

result = Print_and_Return([1,2])
print(result)

print('First Plus Length')
def First_Plus_Length(list):
    return list[0]+ len(list)

x = First_Plus_Length([1,2,3,4,5])
print(x)

print('Values Greater than Second')
def Values_Greater_than_Second(list):
    my_new_list = []
    if(len(list) == 0):
        return False
    for i in range(len(list)):
        if(list[i] > list[1]):
            my_new_list.append(list[i])
    
    return my_new_list

x = Values_Greater_than_Second([5,2,3,2,1,4])
print(x)

print('This Length, That Value')
def This_Length_That_Value(l,v):
    my_new_list = []
    for i in range(l):
        my_new_list.append(v)
    
    return my_new_list

x = This_Length_That_Value(4,7)
print(x)
