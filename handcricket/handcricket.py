import random
Option = [1,2,3,4,5,6]
wicket = 0
run = 0
print("your chosen number is added with user number and their addition will get done if it is even you loss if it is odd u win the toss!!!1")
print("BEST OF LUCK!!!!")
print("-------------------------------------------------------------------------------------------------------------------------------------")
user1 = int(input("sellect a number from 1 to 6: "))
user2 = random.choice([1,2,3,4,5,6])
print(f'user2 has chosen {user2}')
print(f'user1 has chosen {user1}')
def bat():
    wicket = 0
    run = 0
    print("user1 has chosen to ball so user2 have to bat")
    times_of_play = random.choice([1,2,3,4,5,6])
    for i in range(times_of_play):
            run1 = random.choice([1,2,3,4,5,6])
            run2 = int(input("Enter your runs from 1 to 6: "))
            
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket = wicket + 1
            else:
                print(f'yeah u hit a {run1}')
                run = run + run1
    print(f'WICKETS: {wicket}')
    print(f'RUNS:  {run}')
    runs = run +1
    print("-----------------------------------------------------------------------")
    print("Now user2 have to bat and user1 will ball")
    print(f'user1 have to make {runs} ')
    run3 = 0
    wicket3 = 0
    for i in range(times_of_play):
            run1 = random.choice([1,2,3,4,5,6])
            run2 = int(input("Enter your runs from 1 to 6: "))
            
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket = wicket + 1
            else:
                print(f'yeah u hit a {run1}')
                run3 = run3 + run1
    if(run3>run1):
            print(f'YEAH!!!! USER1 HAD MADE {run3}')
            print("USER1 HAS WON THE MATCH!!!!!!!!!!")
            
    elif(run3==run1):
            print("MATCH HAS TIED!!")
    else:
            print("USER2 HAS WON THHE MATCH!!!!!!!!!!")
    
    
    
def bat2():
    wicket = 0
    run = 0
    print("user2 has chosen to ball so user1 have to bat")
    times_of_play = (int(input("How many tiimes do u want to play?: ")))
    for i in range(times_of_play):
            run1 = int(input("Enter your runs from 1 to 6: "))
            run2 = random.choice([1,2,3,4,5,6])
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket = wicket + 1
            else:
                print(f'yeah u hit a {run1}')
                run = run + run1
    print(f'WICKETS: {wicket}')
    print(f'RUNS:  {run}')
    print("----------------------------------------------------------------------")
    print("Now user2 have to bat and user1 will ball")
    print(f'user2 have to make {runs} ')
    run3 = 0
    wicket3 = 0
    for i in range(times_of_play):
            run1 = random.choice([1,2,3,4,5,6])
            run2 = int(input("Enter your runs from 1 to 6: "))
            
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket3 = wicket3 + 1
            else:
                print(f'yeah u hit a {run1}')
                run3 = run3 + run1
    if(run3>run1):
            print(f'YEAH!!!! USER2 HAD MADE {run3}')
            print("USER2 HAS WON THE MATCH!!!!!!!!!!")
    elif(run3==run1):
            print("MATCH HAS TIED!!")
    else:
            print("USER1 HAS WON THHE MATCH!!!!!!!!!!")
    

if((user1 + user2)%2==0):
    print("USER1 won the toss")
    print("-------------------------------------------------------------------------")
    choose = input("BALL or BAT: ")
    if(choose=="BALL"):
        # print("user1 has chosen to ball so user2 have to bat")
        bat()
        
    elif(choose=="BAT"):
        print("user1 has chosen to baT so user2 have to baLL")
        times_of_play = (int(input("How many tiimes do u want to play?: ")))
        for i in range(times_of_play):
            run1 = int(input("Enter your runs from 1 to 6: "))
            run2 = random.choice([1,2,3,4,5,6])
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket = wicket + 1
            else:
                print(f'yeah u hit a {run1}')
                run = run + run1
        print(f'WICKETS: {wicket}')
        print(f'RUNS:  {run}')
        runs = run +1
        print("-----------------------------------------------------------------------")
        print("Now user2 have to bat and user1 will ball")
        print(f'user1 have to make {runs} ')
        run3 = 0
        wicket3 = 0
        for i in range(times_of_play):
            run1 = random.choice([1,2,3,4,5,6])
            run2 = int(input("Enter your runs from 1 to 6: "))
            
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket3 = wicket3 + 1
            else:
                print(f'yeah u hit a {run1}')
                run3 = run3 + run1
        if(run3>run1):
            print(f'YEAH!!!! USER2 HAD MADE {run3}')
            print("USER2 HAS WON THE MATCH!!!!!!!!!!")
        elif(run3==run1):
            print("MATCH HAS TIED!!")
        else:
            print("USER1 HAS WON THHE MATCH!!!!!!!!!!")
            
    else:
        print("Invalid choice")
    
          
    
else:
    print("USER2 won the toss")
    print("-------------------------------------------------------------------------")
    choose = random.choice(["BALL","BAT"])
    if(choose=="BALL"):
        #print("user2 has chosen to ball so user1 have to bat")
        bat2()
    elif(choose=="BAT"):
        print("user2 has chosen to baT so user1 have to baLL")
        times_of_play = random.choice([1,2,3,4,5,6])
        for i in range(times_of_play):
            run1 = int(input("Enter your runs from 1 to 6: "))
            run2 = random.choice([1,2,3,4,5,6])
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket = wicket + 1
            else:
                print(f'yeah u hit a {run1}')
                run = run + run1
        print(f'WICKETS: {wicket}')
        print(f'RUNS:  {run}')
        runs = run +1
        print("-----------------------------------------------------------------------")
        print("Now user2 have to ball and user1 will bat")
        print(f'user1 have to make {runs} ')
        run3 = 0
        wicket3 = 0
        for i in range(times_of_play):
            run1 = int(input("Enter your runs from 1 to 6: "))
            run2 = random.choice([1,2,3,4,5,6])
            if(run1 == run2):
                print("yeahh !!! its wicket")
                wicket3 = wicket3 + 1
            else:
                print(f'yeah u hit a {run1}')
                run3 = run3 + run1
        if(run3>run1):
            print(f'YEAH!!!! USER1 HAD MADE {run3}')
            print("USER1 HAS WON THE MATCH!!!!!!!!!!")
        elif(run3==run1):
            print("MATCH HAS TIED!!")
        else:
            print("USER2 HAS WON THHE MATCH!!!!!!!!!!")
    
        
            
    else:
        print("Invalid choice")
    
# print(f'WICKETS: {wicket}')
# print(f'RUNS:  {run}')


            
    
    