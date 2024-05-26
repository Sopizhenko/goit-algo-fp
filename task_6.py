def greedy_algorithm(items, budget):
	# Сортуємо страви за відношенням калорійність / вартість
	sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
	
	selected_items = {}
	total_calories = 0
	total_cost = 0
	
	for item, properties in sorted_items:
		if total_cost + properties['cost'] <= budget:
			selected_items[item] = properties
			total_cost += properties['cost']
			total_calories += properties['calories']
	
	return selected_items, total_calories

def dynamic_programming(items, budget):
	# Створюємо матрицю для збереження результатів
	# Рядки - різні страви, стовпці - різні бюджети
	dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
	
	# Заповнюємо матрицю відповідно до алгоритму динамічного програмування
	for i, (item, properties) in enumerate(items.items(), start=1):
		for j in range(1, budget + 1):
			if properties['cost'] > j:
				dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - properties['cost']] + properties['calories'])
	
	# Відновлюємо набір страв, який дає максимальну калорійність
	selected_items = {}
	total_calories = dp[len(items)][budget]
	j = budget
	for i in range(len(items), 0, -1):
		if dp[i][j] != dp[i - 1][j]:
			item, properties = list(items.items())[i - 1]
			selected_items[item] = properties
			j -= properties['cost']
	
	return selected_items, total_calories

# Дані про страви
items = {
	"pizza": {"cost": 50, "calories": 300},
	"hamburger": {"cost": 40, "calories": 250},
	"hot-dog": {"cost": 30, "calories": 200},
	"pepsi": {"cost": 10, "calories": 100},
	"cola": {"cost": 15, "calories": 220},
	"potato": {"cost": 25, "calories": 350}
}

budget = 300

# Використання жадібного алгоритму
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected Items:", selected_items_greedy)
print("Total Calories:", total_calories_greedy)

print("\n")

# Використання алгоритму динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Dynamic Programming:")
print("Selected Items:", selected_items_dp)
print("Total Calories:", total_calories_dp)

