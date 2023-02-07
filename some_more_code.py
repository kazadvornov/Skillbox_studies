my_dict = {9:1, 8:2, 7:3, 6:4, 5:55}
my_sum = 0
for key, value in my_dict.items():
	my_sum += key * value
print(my_sum)