#set up
print("Welcome to Quiz Tim! You will answer a few True or False questions. Please ONLY enter the letter T or F when it's your turn to answer. Hvae fun!")
#list the questions
correct = 0
track = 0
questions=("Q1. There are seven planets in the solar system", "Q2. Delware was the first state", "Q3. The Walt Disnet Company was founded in 1910 ")
answers = ("F","T","F")
#ask question in each question
for question in questions:
  print (question)
#make sure all answers are either T or F
  answer = ""
  while(answer != "T" and answer != "F"):
    answer = input("Please enter 'T' for true  or 'F'for false")

#if answer is correc, give the user 1 point
  if(answer == answers[track]):
    correct +=1
  #move to the next one
  track +=1
#show the users the amount they got right verus the aount they answered 
print(f"You got {correct} out of {len(questions)} correct! Thanks for playing!")