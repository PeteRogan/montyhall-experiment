# doors: 1 - car; 0 - goat
# scenario: 1 - keep, 2 - switch
import random

n_runs = int(input("Enter number or runs: "))
scenario = int(input("Enter scenario (1 or 2): "))
n_wins = 0

for i in range(n_runs):
    doors = [1, 0, 0]
    
    #Get first choice
    index1 = random.randint(0, 2)
    choice1 = doors[index1]
    
    #Remove first choice
    del doors[index1]
    
    #Remove one non-car
    if doors[0] == 0:
        del doors[0]
    else:
        del doors[1]
    
    #Implement scenario
    if scenario == 1:
        choice2 = choice1
    elif scenario == 2:
        choice2 = doors[0]
    
    #Determine if won
    if choice2 == 1:
        n_wins += 1
        
print("Number of wins: ", n_wins)
