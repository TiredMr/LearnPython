lst1 = ['abc', 123, "def", 10.5, 62, ['g','h','i']]
lst2 = [0,1,2,3,4]
lst3 = ['I love sushi so much!', 'I also love curry!']

print(lst1[0]) # prints abc

print(lst1[4:6]) # prints [62, ['g','h','i']]

print(len(lst1)) # prints 6
print(len(lst2)) # prints 5
print(len(lst3)) # prints 2

lst1.append(99) # appends 99 at the end of the list

lst1.remove(62) # remove 62 from de list

lst1.pop() # removes ['g','h','i']
lst1.pop(0) # removes 'abc'