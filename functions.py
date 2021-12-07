"""
x = [ [5,2,3], [10,8,9] ] 

print(x[1][0])
x[1][0] = 15
print(x[1][0])
print(x)


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students[0]['last_name'])
students [0]['lastname'] = "Bryant"
print(students)


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory['basketball'])
sports_directory['soccer'][0] = "Andres"
print(sports_directory)


z = [ {'x': 10, 'y': 20} ]
print(z[0]['x'])
z[0]['y'] = 30
print(z)

    Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. DONE- RM
    Change the last_name of the first student from 'Jordan' to 'Bryant' DONE - RM
    In the sports_directory, change 'Messi' to 'Andres' DONE - RM
    Change the value 20 in z to 30 DONE- RM

"""
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
#     for i in some_list:
#         result = ""
#         for k,v in i.items():
#             result += f"{k} - {v}, "
#         print(result[0:-2])

# print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

# # Cannot figure out how to print without brackets. 
# When i write line 48 with {}{}, i get an error message. 


# iterateDictionary(students)

# Create a function iterateDictionary2(key_name, some_list)
#  that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) 

# def iterateDictionary2(key_name,some_list):
#     for i in some_list:
#         for k in i.keys():
#             if k == key_name:
#                 print(i[key_name])

# iterateDictionary2('first_name',students)
# iterateDictionary2('last_name',students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict.keys():
        print(f"{len(some_dict[i])} {i.upper()}")
        for x in some_dict[i]:
            print(x)
        print()

        
    # some_dict.keys



printInfo(dojo)


# printInfo(dojo)

'''
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
'''


