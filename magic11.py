# This is my first project that I've created on my journey to becomming a Software Engineer. Enjoy!

import random

name = ""
question = ""
answer = ""

random_number = random.randint(1, 11)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "The answer is easy... YES!"
elif random_number == 11:
  answer = "It's a yes in my book."
else:
  answer = "Error"
if question == "":
  answer = "You must ask a question to have your fortune told."

if name == "":
  print("Question: " + question)
else:
  print(name + "asks: " + question)
print("Magic 11-ball's answer: " + answer)
