'''
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 

'''

def aplhabets_pattern(number):

    n = 65
    for i in range(1,number+1):
        print(" "*(number-i),end=" ")
        for j in range(1,i+1):

            print(chr(n+(j-1)),end=" ")
        print()

aplhabets_pattern(5)
    