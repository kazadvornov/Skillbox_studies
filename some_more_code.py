my_dict = {10:90, 20:80, 30:70, 40:60, 550:50}
my_sum = 0
for key, value in my_dict.items():
	my_sum += key * value
print(my_sum)
