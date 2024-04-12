'''
*********
 *******
  *****
   ***
    *
'''

def inverted_full_pyramid(number):

    for asterik in range(number,0,-2):
        print(' '*(number-(asterik))+"* "*(asterik))

inverted_full_pyramid(5)
