secret_answer = "cartage"
answer = ""
count = 0 
limit = 3 
lose = False
while secret_answer != answer and not lose : 
    if count < limit:
         answer = input("what is capital of tunsia?")
         count += 1
    else:
        lose = True
                  
if lose: 
    print("you lose")
else : 
    print ("You win")