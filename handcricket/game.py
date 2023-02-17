import random
times_of_play = (int(input("How many tiimes do u want to play?")))

user_points = 0
comp_points = 0
for i in range(times_of_play):
    user = input('Enter the input (R/P/S): ').upper()
    comp = random.choice(['R','P','S'])
    
    if (user== 'R' and comp == 'S') or (user== 'p' and comp == 'R') or (user== 'S' and comp == 'P'):
        print(f'user chose {user} and comp chose {comp}')
        print("USER WON!!!!!")
        user_points = user_points + 1
        
    elif(comp== 'R' and user == 'S')or (comp== 'p' and user == 'R') or (comp== 'S' and user == 'P'):
        print(f'user chose {user} and comp chose {comp}')
        print("COMP WON!!!!!")
        comp_points = comp_points + 1
        
    else:
        print(f'user chose {user} and comp chose {comp}')
        print("lolzz...its tieeee")
        
print(f'user points = {user_points}')

print(f'comp points = {comp_points}')