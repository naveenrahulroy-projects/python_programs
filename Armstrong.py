num = 153
sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
print("Armstrong" if sum_of_cubes == num else "Not Armstrong")
