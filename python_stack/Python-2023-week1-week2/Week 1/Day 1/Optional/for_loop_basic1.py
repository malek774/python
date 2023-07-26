print('Basic')
for i in range(151):
    print(i)

print('Multiples of Five')
i = 5
while i<1001 :
    print(i)
    i+=5

print('Counting, the Dojo Way')
for i in range(1,100):
    if(i % 5 == 0):
        print('Coding')
    if(i % 10 == 0):
        print('Coding Dojo')

print("Whoa. That Sucker's Huge")
sum = 0
for i in range(500000):
    sum += i

print(sum)

print('Countdown by Fours')
i = 2018
while (i<=2018) and (i>=0):
    print(i)
    i -= 4
    
print('Flexible Counter')
def flex_conter(lowNum,highNum,mult):
    for i in range(lowNum-1,highNum+1):
        if(i % mult == 0):
            print(i)

flex_conter(2,9,3)

