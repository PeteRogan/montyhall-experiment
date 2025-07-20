# montyhall-experiment
Python program to confirm the validity of the Monty Hall problem result

The Monty Hall problem is a brain teaser that goes as follows:

Imagine yourself at a game show. There are 3 doors: behind one door there is a car and behind the other two are goats.
The host asks you to choose one door and you get to keep what ever is behind that door. You pick a door, but the host says, that he will help you out in the following way:
he will remove one of the remaining doors which contains a goat and will give you the option to either stick with your original decision or to choose the other door that is left.
Should you stick with the first decision or change your mind?

As it turns out you are better off switching to the other door. This result is, however, counter-intuitive as it might seem that there is still 1/3 chance of there being a car behind that door.
This Python program simulates the game show to verify empirically that, despite being counter intuitive, it is till true that there is a 2/3 probability of you getting the car if you decide to switch. It runs a given scenario (keep or switch) a given number of times and tells how many runs ended up with a win. One is then able to confirm that if you choose to keep then approximately 1/3 of the runs are wins but if you choose switch then approximately 2/3 of the runs are wins.

Usage:
1. Run MontyHallExperiment.py
2. Enter number of runs
3. Enter which scenario to run
