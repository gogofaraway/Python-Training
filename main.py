#Intorduce your education insitutie to your potential customers"
message = ("Welcome to Happy Life School! ")
print(message)

#How old is your child?
age = input("1. How old is your child?")
print(age)
#Are you planning to enroll in any special programs? a. Art b. Chess c. Drama d. Math
program = input ("2. Are you planning to enroll for any after school programs? \n a) Art. b) Chess. c)Drama. d)Math [a/b/c/d]? :")
if program == "a":
      print("Art.")
elif program == "b":
      print("Chess.")
elif program == "c":
      print("Drama")
elif program == "d":
      print("Math")

#Are you planning to enroll in any sport? a. Dance b. Golf c. Soccer d. Tennis e. Basketball
sport= input("3. Are you planning to join any of the sport tems? \n a) Dance b) Golf c) Soccer d) Tennis e) Basketball [a/b/c/d/e]? :")
if sport == "a":
     print("Dance")
if sport == "b":
     print("Golf")
if sport == "c":
     print("Tennis")
if sport == "e":
     print("Basketball")

#Are you planning to enrooll in the lunch program?
lunch = input("4. Are you planning to sign up for lunch program? \n a) Yes b) No [a/b]? :")
if lunch == "a":
   print("Yes")
if lunch == "b":
  print("No")
#Are you planning to take school bus?
bus = input("5. Are you planning to take school bus? \n a) Yes b) No [a/b]? :")
if bus == "a":
  print("Yes")
if bus == "b":
  print("No")
