'''
Tutorial 2 - Lists, Tuples, Sets, Dictionaries, For Loops, While Loops
github.com/codrkai

'''

'''
    Lists are user ordered
    Lists allows duplicate item names
'''
# Lists will print out in the exact order that it's set below
# since lists are in the order defined below, it then has indexes and allows
# us to locate each item easily using the index
avengersLst = ['iron man', 'spiderman', 'capt america', 'hulk']

# will append to the end of the list
avengersLst.append('black panther')

# adding multiple items to the end of the list
# will add duplicates, ie. hulk will show up twice in the list
avengersLst.extend(['black panther', 'dr. strange', 'hulk'])

# we can insert at any location in the list by supplying an index number
avengersLst.insert(3, 'black panther')

# removes an item from the list by using an index number
# if a index number is not provided, it will then return the last item
avengersLst.pop(1)

# changes the order of the list in reverse
avengersLst.reverse()

# sorts the list
avengersLst.sort()

# prints the list
print(avengersLst)


'''
    Sets are random ordered
    Sets will not have duplicate item names
'''
avengersSet = {'iron man', 'spiderman', 'capt america', 'hulk'}

# adds an item to the set
avengersSet.add('black panther')

# adds multiple items to the set
# will not add duplicates, ie. hulk will only show once in the set
avengersSet.update({'ant man','the wasp','doctor strange', 'hulk'})

# randomly removes an item from the set
avengersSet.pop()

# remove a specific item from the set
# will raise an error if the item does not exist!
avengersSet.remove('black panther')

# remove an item from the set, but will not raise an error
avengersSet.discard('spider')

# removes from the set matching keywors and will update the set
# this will modify and update the actual set!
avengersSet.difference_update({'hulk', 'black panther'})

#prints the set
print(avengersSet)

# removes from the set anything matching the keywords provided
# will NOT modify the set!
z = avengersSet.difference({'hulk', 'black panther'})

# returns matches from both list
z = avengersSet.intersection({'hulk', 'spiderman', 'black panther'})

# returns results of both sets combined
z = avengersSet.union({'hulk', 'black panther'})

#print the results above
print(z)


'''
    Dictionaries are user ordered, changeable, indexed
    Key/value pairs
'''

avengersDict = {
    'name':'hulk',
    'powers':['smash','angry','high jump']
}

# update the dictionary value where key is called "name"
avengersDict['name'] = 'capt america'

# update where the key is called "powers"
avengersDict.update({'powers':'americas ass'})

# remove a key/value item
avengersDict.pop('powers')

# remove a key/value item
del avengersDict['powers']

# removing an item from the dict that doesn't exist will raise an error
avengersDict.pop('pow') # error

# check to see if the item exists in the dictionary
if 'powers' in avengersDict:
    avengersDict.pop('powers')

# print the dictionary
print(avengersDict)

# get a value from the dict using the key name
x = avengersDict.get("name")

# get all key names from the dict
x = avengersDict.keys()

# get all values from the dict
x = avengersDict.values()

# get all key/value pairs from the dict, aka items.
x = avengersDict.items()

print(x)

'''
    Tuples are user ordered and unchangeable
    can't add or remove items!
''' 

avengersTpl = ('iron man', 'spider man', 'hulk')

# error! cannot add to list
avengersTpl[1] = 'Bucky'

# will return item at index 1, which is "spider man"
x = avengersTpl[1]

print(x)


'''
    Other Stuff
'''

# to easily declare a list, tuple, set, or dict
lst = list(('iron man', 'spiderman'))
tpl = tuple(('iron man', 'spiderman'))
myset = set(('iron man', 'spiderman'))
mydict = dict(('iron man', 'spiderman'))

# deletes the entire set
del avengersSet

# deletes the item "spider man"
del avengersDict['spider man']

# clears the list, set, or dict
# guess what you can't clear? Tuples!
avengersLst.clear()
avengersSet.clear()
avengersDict.clear()

'''
    Loops
'''

# for loop
y = ['spiderman', 'hulk']
#y = {'spiderman', 'hulk'} # set
#y = ('spiderman', 'hulk') # tuple

# will loop through the list and prints out each item
for x in y:
    print(x)
    
y = {
    'name': 'hulk',
    'powers': ['smash','angry','jump']
}

# these functions are for dictionaries
# it will return the keys, values, or both key/value pairs
# .keys(), .values(), .items()
for a in y.keys():
    print(a) # will print all keys in the dict

# will print all values in the dict
# if the value is a string, it will iterate through each character!
# if the value is a list, it will display each word from the list
for a in y.values():
    for b in a:
        print(b)

# this will check if the dictionary value is a list, tuple, or set, 
# and then will print out each item from that.
# it will skip over single string words
for a in y.values():
    if isinstance(a, (list, tuple, set)):
        for b in a:
            print(b)


# while loop

# remember to increment i for it to move forward
# other wise it will loop forever!
i = 1
y = 5
while i < y:
    print(i)
    i += 1
    if i == 2:
        break

# a simple list
y = ['iron man', 'spiderman']

# will print out each item from the simple list above
i = 0
x = len(y) # lenght is 2
while i < x:
    print(y[i])
    i += 1


'''
github.com/codrkai
'''