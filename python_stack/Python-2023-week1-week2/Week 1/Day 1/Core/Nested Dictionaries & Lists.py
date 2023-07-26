x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)

# sports_directory['basketball'][1] = 'Bryant'
# print(sports_directory)

# sports_directory['soccer'][0] =  'Andres'
# print(sports_directory)

# z[0]['y'] = 30
# print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
#     for k in some_list:
#         print(f"first_name : {k['first_name']} , last_name : {k['last_name']}")
      
# iterateDictionary(students)

def iterateDictionary2(key, some_list):
    for k in some_list:
        print(k[key])      
iterateDictionary2('first_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'],
}

# my_keys = dojo.items()
# keys = list(my_keys)
# print(keys[0])
# my_val = list(keys[0])
# print(my_val)
# print(my_val[0])
# print(len(dojo1[0][1]))
# print(dojo1[0][1][0])

def printInfo(some_dict):
    dojo1 = list(dojo.items())
    for i in range(len(list(dojo.keys()))):
        x = list(dojo.keys())
        print(f"{len(dojo1[i][1])} {x[i]}")
        for y in range(len(dojo1[i][1])):
            print(dojo1[i][1][y])

# printInfo(dojo)

# for i in range(len(dojo)):
#     for k in dojo1:
#         my_keys = dojo.items()
#         keys = list(my_keys)
#         my_val = list(keys)
#         print(my_val[0][0])
        # for y in range(len(dojo[k])-1):
        #     print(dojo[k][y])
    # my_keys = dojo.items()
    # keys = list(my_keys)
    # print(keys)
    # my_val = list(keys[0])
    # print(my_val)
    # print(my_val[1][0])