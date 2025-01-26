# Lambda Syntax: lambda [arguments]: [expression] 

# Regular function 

def square(x): 

    return x ** 2 

# Lambda function 

square_lambda = lambda x: x ** 2

 
# Lambda function to add two numbers 

add = lambda a, b: a + b 

print(add(3, 5))  # Output: 8 

  

# Lambda function to print a name 

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Alice"))  # Output: Hello, Alice! 


# Using map()

numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) # map () applies this lambda to each element.
  
print(squared)  # Output: [1, 4, 9, 16, 25] 



# Using filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # filter() uses lambda to keep only the even numbers from the original list

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 



# Using sorted()

students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 

sorted_students = sorted(students, key=lambda x: x[2]) 
# In this case, the lambda function lambda x: x[2] is used as the key for sorting.
# It tells the sorted() function to use the third element (index 2) of each tuple for comparison. 
# As a result, the list of students is sorted based on their age (the third element in each tuple).

print(sorted_students) 

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 








