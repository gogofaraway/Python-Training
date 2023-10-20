#~Tales of UMBC ~
print("~Tales of UMBC~")
#(A Work of Fiction)
print("(A Work of Fiction)")
print("\n")
#You are a knight in the year 650 CE, and you're trying to become the most famous knight of them all.
print("You are a knight in the year 650 CE, and you're trying to become the most famous knight of them all.")
print("\n")
#You decide to go on an adventure at Castle UMBC to earn your glory!
print("You decide to go on an adventure at Castle UMBC to earn your glory!")
print("\n")
#You are outside the castle grounds, and see three different people asking for help. You could talk to:
print("You are outside the castle grounds, and see three different people asking for help. You could talk to:")
#A. The local blacksmith, who needs a rare sword
print("A. The local blacksmith, who needs a rare sword")
#B. The town's teacher, who has a question
print("B. The town's teacher, who has a question")
#C. The king, who needs a brave warrior
print("C. The king, who needs a brave warrior")
#Who will you talk to? Please select option A through C:
choice = input("Who will you talk to? Please select option A through C: \n [A/B/C]")
if choice == "A":
  print("\n")
  print("You meet with the town blacksmith, looking for a legendary sword.")
  print("They tell you that the legend is that the sword is frozen in ice waiting to be found.")
  print("you chosse to search for it:")
  print("A. In the Desert")
  print("In the Forest")
  print("In the Arctic")
  option = input("Please select option A through C: \n [A/B/C]")
  print("\n")
  if option == "A":
    print("You searched and searched for the rest of your life, but you never found it. It might've been a good idea to heed the blacksmith's advice and go to a cold place")
    print("~The End~")
  if option == "B":
    print("You searched and searched for the rest of your life, but you never found it. It might've been a good idea to heed the blacksmith's advice and go to a cold place")
    print("~The End~")
  if option == "C":
    print("After looking long and hard through the arctic, you've found it - the legendary sword of programmingh! The blacksmith is thrilled and rewards you with a suit of armor worthy of a hero!")
    print("~The End~")
if choice == "B":
  print("\n")
  print("You meet with the town teacher, who is asking you a questions")
  print("'I have to be honest with you, 'they say. 'I am not really qualified to teach and am struggling with this question' They gesture to a math equation that reads as follows:")
  print("y = 6 + 2 + 1")
  teacher = input("Please enter the solution to the problem:")
  print(teacher)
  correctAnswer = "9"
  if(teacher ==correctAnswer):
    print("'That makes perfect sense!'the teacher cries, and they award you with an honorary degree. You are forever known a one of the smartest in the land!'")
    print("~The End~")
  if(teacher != correctAnswer):
    print("You are not smart")
    print("~The End~")
if choice == "C":
  print("\n")
  print("You meet with the king of UMBC, looking for a brave warrior.")
  print("I need someone to conquer a nearby dragon to save the kingdon! There is no time, head east and be ready for battle!")
  print("\n")
  print("You head east and find the dragon. You ready yourself for battle. But in a twist, the dragon asks you to solve a riddle in exchange for your kingdon.")
  print("\n")
  print("'What two numbers, when added together, equal ten?'")
  print("\n")
  print("You ponder for a moment. There's multiple answers to this question, aren't there?")
  print("After thinking for a moment, you answer two numbers")
  a = input("Enter the first number:")
  b = input("Enter the second number:")
  a = int(a)
  b = int(b)
  c = a + b
  correctAnswer = 10
  if(c == correctAnswer):
   print(f"'Ah yes, {a} and {b} add up to {correctAnswer}!' the dragon explained")
   print("The dragon decides to leave your kindon alone, and the king declares you are the greatest hero in all the land!")
   print("~The End")
  if(c != correctAnswer):
   print("You are not great")
   print("~The End~")