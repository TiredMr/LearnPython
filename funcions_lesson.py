def add_three(num1, num2, num3):
    sum_three = num1 + num2 + num3
    return sum_three
    
def greetings(language):
    if language == 'Spanish':
        greetings = 'Hola'
        
    elif language == 'English':
        greetings = 'Hello'
        
    elif language == 'French':
        greetings = 'Bonjour'
    
    print(greetings)
        
def main():
    sun_output = add_three(2,4,6)
    print(sun_output)
    greetings('English')
    

if __name__ == "__main__":
    main()


