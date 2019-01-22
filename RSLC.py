# Ridiculously Simle Label Counter (RSLC) by Nick Lawrence, 2019
# Please feel free to use and modify this code as needed
# License: MIT 

import math

while True:
  # This takes in how many individual labels you need.
  number_needed = float(input("How many labels do you need? >> "))

  # There are 30 labels per sheet as of now, please feel free to modify as needed.
  labels_per_sheet = 30.00
  
  #This stores the sheet count by dividing labels needed by the labels per sheet and rounding up so you don't come up short.
  sheets_needed = math.ceil(number_needed / labels_per_sheet)
  
  # This tells the user how many sheets of labels they will need
  print(f">> You will need {sheets_needed} sheets.")

  # This asks the user if they would like to perform another calculation
  another_one = input("Would you like to do another one? [Y/n] >> ").capitalize()
  if another_one == 'N' or another_one == 'NO':
    print('Exiting program')
    # If No, break out of loop
    break
  else:
    # If anything else, continue.
    continue
