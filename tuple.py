my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0]) # prints 'abc'

print(my_tuple[3:5]) # prints (456, 789)

print(len(my_tuple)) # prints 6

#======================================================

my_tuple1 = (65, 2, 88, 101,25)
max(my_tuple1) # returns 101
min(my_tuple1) # returns 2

my_tuple2 = ('orange', 'blue', 'red', 'green')
max(my_tuple2) # return 'red'
min(my_tuple2) # return 'blue'

my_tuple3 = ('abc', 234, 567, 'def')
max(my_tuple3) # throws an error!
min(my_tuple3) # throws an error!

#======================================================

my_tuple4 = ('abc', 234, 567, 'def')
my_tuple4.index('abc') # returns 0
my_tuple4.index(567) # returns 2

my_tuple5 = ('abc', 'abc', 2, 3, 4)
my_tuple5.count('abc') # returns 2
my_tuple5.count(3) # returns 1