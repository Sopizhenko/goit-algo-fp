import random

def monte_carlo_simulation(num_trials):
	results = {i: 0 for i in range(2, 13)}
	
	for _ in range(num_trials):
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		total = dice1 + dice2
		results[total] += 1
	
	probabilities = {key: value / num_trials * 100 for key, value in results.items()}
	
	return probabilities

def print_probabilities(probabilities):
	print("Сума\tІмовірність")
	for key, value in probabilities.items():
		print(f"{key}\t{value:.2f}% ({probabilities[key] / 100:.2f})")

# Кількість спроб для симуляції
num_trials = 100000

# Виконання симуляції
probabilities = monte_carlo_simulation(num_trials)

# Виведення результатів
print_probabilities(probabilities)

'''
Аналітичні значення ймовірностей суми двох кидків кубика:
Сума	Імовірність
2	2.78% (1/36)
3	5.56% (2/36)
4	8.33% (3/36)
5	11.11% (4/36)
6	13.89% (5/36)
7	16.67% (6/36)
8	13.89% (5/36)
9	11.11% (4/36)
10	8.33% (3/36)
11	5.56% (2/36)
12	2.78% (1/36)

Результати методу Монте-Карло досить близькі до аналітичних значень, із деякою варіацією через випадкову природу симуляції.
Чим більше num_trials, тим більше результати методу Монте-Карло будуть наближатися до аналітичних значень.
'''