#  created in 2021 by LSCP
#  testing simple python 
print("Hello, my name is Athen bot, I will test your general knowlege on a topic of your choosing")
print("what is your name?")
name = input()
print("what a nice name you have, " + name)
print("What year were you born in?")
born_year = int(input())
print("I can't remeber one thing, could you please tell me what year are we in again?")
current_year = int(input())
age = current_year - born_year  
print("Oh, you are ",age, ", corect?(please awnser yes or no)")  
awnser_1 =input()
if awnser_1 == "yes":{   
      print("good")}
elif awnser_1 == "no":
      age_2 = age - 1
      print("Oh, so you must be ",age_2)
else: 
      print("Sorry, that is an invalid awnser. Try again")

print("Do you want to take a geography quiz?(please enter yes or no)")
awnser_2 = input()
if awnser_2  == "yes" or awnser_2 == "Yes":
      geography_score = 0
      print("Let's have a small geography quiz then(please choose the letter of your awnser)")
      print("Is Africa")
      print("A: a country")
      print("B: a continet")
      awnser1_quiz_1 = input()
      if awnser1_quiz_1 == "B" or awnser1_quiz_1=="b":
            print("that is correct")
            geography_score += 1
      else:
            print("That is incorrect, Africa is a continent")
      print("Where is Zimabue located?(please choose the letter of your awnser)")
      print("A: Africa")
      print("B: Asia")
      print("C: America")
      awnser2_quiz_1 = input()
      if awnser2_quiz_1 == "A" or awnser2_quiz_1=="a":
            print("You are correct")
            geography_score += 1
      else:
            print("Your awnser is incorrect, Zimbabue is located in Africa")
      print("Wich of the Koreas is considered the 'bad' one?(please choose the letter of your awnser)")
      print("A: South")         
      print("B: North")
      awnser3_quiz_1 = input()
      if awnser3_quiz_1 == "B" or awnser3_quiz_1=="b":
            print("That is correct")
            geography_score += 1
      else:
            print("That is incorrect, the correct awnser is B: North")
      print("How many states are there in the USA?(please choose the letter of your awnser)")
      print("A:10")
      print("B:20")
      print("C:30")
      print("D:40")
      print("E:50")
      awnser4_quiz_1 = input()
      if awnser4_quiz_1 == "E" or awnser4_quiz_1=="e":
            print("That is correct")
            geography_score += 1
      else: 
            print("That is incorrect")
      print("congratulatoins, your total score in geography is",geography_score)
else:
      pass
print("do you want to take a history quiz?(please enter yes or no)")
awnser_3 = input()
if awnser_3 == ("yes"):
      history_score = 0
      print("What country was Alexander, the great emperor of?(please choose the letter of your awnser)")
      print("A: Greece")
      print("B: Egypt")
      print("C: England")
      print("D: France")
      print("E: Macedonya")
      awnser1_quiz_2 = input()
      if awnser1_quiz_2 == ("E") or awnser1_quiz_2==("e"):
            print("that is correct")
            history_score += 1
      else:
            print("That is incorrect, the awnser is E:Macedonya")
      print("Who was in control of the USSR during WW2?(please choose the letter of your awnser)")
      print("A:Hitler")
      print("B:Kennedy")
      print("C:Wistorn Churchyl")
      print("D:Joseph Stalin")
      awnser2_quiz_2 = input()
      if awnser2_quiz_2 == ("D") or awnser2_quiz_2==("d"):
            print("You are correct")
            history_score += 1
      else:
            print("Your awnser is incorrect, the correct awnser is D:Joseph Stalin")
      print("What country colonized Congo?(please choose the letter of your awnser)")
      print("A: England")
      print("B: France")
      print("C: Belgium")
      print("D: Spain")
      print("E: Portugal")
      awnser3_quiz_2 = input()
      if awnser3_quiz_2 == ("C") or awnser3_quiz_2==("c"):
            print("That is correct")
            history_score += 1
      else:
            print("Your awnser is in incorrect, the correct awnser is C:Belguimm")
      print("Congratulations, your total score in geography is",history_score)
print("Congratulations, you got " +(str)(geography_score + history_score) + " out of 7 avaiable questions right") # (str)(x) transforma "x em strig e permite que a frase seja escrita"
print("That is all I can do for now, hope you liked it, I hope to see you once again :)")
import time
time.sleep(5)