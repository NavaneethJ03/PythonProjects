print ("Welcome to  my Computer  Quiz!!!")

playing = (str.lower(input("Do you want to  play ?")))
if playing != "yes":
    quit()

print("Okay ! Lets start playing !:)")
score = 0

ans = str.lower(input("What does CPU stand for ?"))
if ans == "central processing unit":
    print("Your Answer is  correct !")
    score +=1
else:
    print("Your answer is incorrect !!")
ans = str.lower(input("What does GPU stand for ?"))
if ans == "graphics processing unit":
    print("Your Answer is  correct !")
    score +=1
else:
    print("Your answer is incorrect !!")
ans = str.lower(input("What does RAM stand for ?"))
if ans == "random access memory":
    print("Your Answer is  correct !")
    score +=1
else:
    print("Your answer is incorrect !!")
ans = str.lower(input("What does API stand for ?"))
if ans == "application programming interface":
    print("Your Answer is  correct !")
    score +=1
else:
    print("Your answer is incorrect !!")
    
print(f"You Scored a score of {score} out of 5")
