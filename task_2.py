import turtle

def draw_branch(branch_length, angle, level):
	if level == 0:
		return
	turtle.forward(branch_length)
	turtle.right(angle)
	draw_branch(0.7 * branch_length, angle, level-1)
	turtle.left(2 * angle)
	draw_branch(0.7 * branch_length, angle, level-1)
	turtle.right(angle)
	turtle.backward(branch_length)

def main():
	turtle.speed(0)
	turtle.bgcolor("white")
	turtle.left(90)
	turtle.penup()
	turtle.backward(45)
	turtle.pendown()
	level = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 10): "))
	draw_branch(100, 45, level)
	turtle.hideturtle()
	turtle.done()

if __name__ == "__main__":
	main()