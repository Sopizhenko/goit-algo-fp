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