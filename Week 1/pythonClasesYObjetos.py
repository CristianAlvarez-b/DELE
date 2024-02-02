#Make a class called person
#Attributes: name, age, skill level(number between 1-10), winning_count
#Functions: setters and getters, add_skill(n), add_winning(),
#play_against(person)-> change winning_count and skill based on a probability
#of winning if the skill_level differences is maximum 2 the winning probability is 50% for each and if
# the differences is between 2-4 the higher skill wins 75% of the time
# and higher differences end with 100% winning

#Constructor choose a random name form 10 names given, and sets age, skill_level and winning_count randomly
#make a function to choose using sampling from a normal distribution
import random
import numpy as np

class Person:
    def __init__(self, name=None, age=None, skill_level=None, winning_count=None):
        self.names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]
        self.name = name if name is not None else random.choice(self.names)
        self.age = age if age is not None else random.randint(18, 50)
        self.skill_level = skill_level if skill_level is not None else self.choose_skill_level()
        self.winning_count = winning_count if winning_count is not None else random.randint(0, 10)

    def choose_skill_level(self):
        # Choose skill level using sampling from a normal distribution
        skill_level = int(np.random.normal(5, 2))
        return max(1, min(skill_level, 10))  # Ensure skill_level is between 1 and 10

    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_skill_level(self):
        return self.skill_level

    def set_skill_level(self, skill_level):
        self.skill_level = max(1, min(skill_level, 10))  # Ensure skill_level is between 1 and 10

    def get_winning_count(self):
        return self.winning_count

    def set_winning_count(self, winning_count):
        self.winning_count = winning_count

    def add_skill(self, n):
        self.skill_level = max(1, min(self.skill_level + n, 10))  # Ensure skill_level is between 1 and 10

    def add_winning(self):
        self.winning_count += 1

    def play_against(self, opponent):
        skill_diff = abs(self.skill_level - opponent.skill_level)
        if skill_diff <= 2:
            return random.choice([True, False])  # 50% chance of winning for each
        elif skill_diff <= 4:
            return random.choices([True, False], weights=[25, 75])[0]  # Higher skill wins 75% of the time
        else:
            return True  # Higher skill wins 100% of the time
#Create a list of 10 people and make them play in 20 iterations
people = []

# Create 10 people
for _ in range(10):
    person = Person()
    people.append(person)

# Make them play in 20 iterations
for _ in range(20):
    print("Iteration", _ + 1)
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            player1 = people[i]
            player2 = people[j]
            winner = player1.play_against(player2)
            if winner:
                player1.add_winning()
            else:
                player2.add_winning()

# Output the winning count for each person
for person in people:
    print(f"{person.get_name()} - Winning Count: {person.get_winning_count()}")