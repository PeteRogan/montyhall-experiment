# 1 - car; 0 - goat
# Scenario 1 - keep, scenario 2 - switch
import random

n_runs = int(input("Enter number or runs: "))
scenario = int(input("Enter scenario (1 or 2): "))
n_wins = 0

for i in range(n_runs):
    boxes = [1, 0, 0]
    
    #Get first choice
    index1 = random.randint(0, 2)
    choice1 = boxes[index1]
    
    #Remove first choice
    del boxes[index1]
    
    #Remove one non-car
    if boxes[0] == 0:
        del boxes[0]
    else:
        del boxes[1]
    
    #Implement scenario
    if scenario == 1:
        choice2 = choice1
    elif scenario == 2:
        choice2 = boxes[0]
    
    #Determine if won
    if choice2 == 1:
        n_wins += 1
        
print("Number of wins: ", n_wins)
