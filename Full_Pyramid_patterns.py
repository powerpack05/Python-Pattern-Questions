'''
Full Pyramid Patterns in Python using Loop

   *    
  * *   
 * * *  
* * * * 
'''

# Declaring  a function named full_pyramid



def full_pyramid(number):

    for pyramid in range(1,number+1):
        print((' ' * (number-(pyramid))) + ('* ' * pyramid))

full_pyramid(int(input('Enter the number:\n')))