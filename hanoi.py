def move(f, t):
	# print("move from {} to {}!".format(f, t))
	pass


total = 0
# b_1 = 0
# a_1 = 0
# b_2 = 0
# a_2 = 0
# increment = 1
#
# def hanoi(number, f, h, t):
# 	global total
# 	global b_1
# 	global a_1
# 	global b_2
# 	global a_2
# 	if number == 0:
# 		print("PASS", total, "number is ", number)
# 	else:
# 		print("BEFORE 1 hanoi", total, number)
# 		if number == increment:
# 			b_1 += 1
# 		hanoi(number-1, f, t, h)
# 		print("AFTER 1 hanoi", total, number)
# 		if number == increment:
# 			a_1 += 1
# 		total += 1
# 		move(f, t)
# 		print("BEFORE 2 hanoi", total, number)
# 		if number == increment:
# 			b_2 += 1
# 		hanoi(number-1, h, f, t)
# 		print("AFTER 2 hanoi", total, number)
# 		if number == increment:
# 			a_2 += 1
# 		print(total, number)


def hanoi_test(number, f, h, t):
	global total
	if number == 0:
		pass
	else:
		hanoi_test(number-1, f, t, h)
		# move(f, t)
		total += 1
		hanoi_test(number-1, h, f, t)


hanoi_test(25, "A", "B", "C")
print(total)

# print("b_1: {}\n a_1: {}\nb_2: {}\n a_2: {}".format(b_1, a_1, b_2, a_2))
