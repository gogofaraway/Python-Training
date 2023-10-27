print("Welcome to Quiz Time! You will answer a few True or False questions. Please ONLY enter the letter T or F when it's your turn to answer. Have fun!")
questions = ('Q1. There are seven planets in the solar system','Q2. Delaware was the first state', 'Q3. The Walt Disney Company was founded in 1910')
answers = ('T', 'F', 'T')

numberOfQuestions = len(questions)
right = 0
for index in range(numberOfQuestions):
  userAnswer = input(f"{questions[index]}")
  while userAnswer != 'T' and userAnswer != 'F':
    userAnswer = input(f"{questions[index]}")
  if(userAnswer == answers[index]):
   right += 1
print("You got 1 out of 3 correct! Thanks for playing!")