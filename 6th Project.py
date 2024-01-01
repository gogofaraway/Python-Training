################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None

  return val
  
def letter_grade_from_number(grade):
  if 90<= grade:
    return 'A'
  elif 80<= grade < 90:
    return 'B'
  elif 70<= grade <80:
    return 'C'
  elif 60<= grade <70:
    return 'D'
  elif 50<= grade <60:
    return 'e'
  else:
    return 'F'
################ Main Program ################

Students = {}
displayMenu()
choice = input('Select an Option: ')

# Application Loop
while choice != '6':
  if choice == '1':
     name = input("Enter Student Name: ")
     Students[name] = []
  elif choice == '2':
   name = input("Enter Student Name: ")
   if name in Students:
    del Students[name]
    print(f'{name} removed')
   else:
     print(f'{name} is not in the gradebook!')
  elif choice == '3':
   name = input("Enter Student Name: ")
   if name in Students:
     grade = getNumberGradeFromUser()
     Students[name].append(grade)
   else:
     print(f'{name} is not in the gradebook!')
  elif choice == '4':
     name = input("Enter Student Name: ")
     if name in Students:
      for grade in Students[name]:
         print(grade)
     else:
       print(f'{name} is not in the gradebook!')
  elif choice == '5':
     name = input("Enter Student Name: ")
     if name in Students:
      gpa = sum(Students[name]) / len(Students[name])
      print(gpa)
      letter = letter_grade_from_number(gpa)
      print(f'{name} has a grade of {letter}')
     else:
       print(f'{name} is not in the gradebook!')
  # Prompt the user to select an option
  print()
  displayMenu()
  choice = input('Select an Option: ')
  
print('Gradebook is closed')
