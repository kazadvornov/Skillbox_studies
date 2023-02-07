my_dict = {1:9, 2:8, 3:7, 4:6, 55:5}
my_sum = 0
for key, value in my_dict.items():
	my_sum += key * value
print(my_sum)