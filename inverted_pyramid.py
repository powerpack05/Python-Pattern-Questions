'''
*********
 *******
  *****
   ***
    *
'''

def inverted_full_pyramid(number):

    number = number if (number % 2) == 1 else (number - 1)
    
    for asterik in range(number,0,-2):
        print(' '*((number-asterik))+"* "*(asterik))

inverted_full_pyramid(int(input("Enter the number:\n")))
