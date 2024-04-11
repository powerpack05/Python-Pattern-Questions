'''
    1
   123
  12345
 1234567
123456789
'''

def numbers_pattern(number):

    for i in range(1,number+1):

        print(" "*(number-i),end=" ")

        for j in range(1,i+1):

            print(j,end=" ")

        print()

numbers_pattern(5)