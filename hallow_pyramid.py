'''
                *
              *   *
            *       *
          *           *
        *               *
      *                   *       
    *                       *     
  *                           *   
*   *   *   *   *   *   *   *   * 
'''

def hallow_pyramid(number_of_rows):

    for i in range(1, number_of_rows + 1):

        for j in range(1, 2 * number_of_rows):

            if (i + j == number_of_rows + 1) or (j - i == number_of_rows - 1) or (i == number_of_rows and j%2!=0):

                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

hallow_pyramid(9)

