lst = [3, 1, 2, 5, 4]
lst.sort()
n = len(lst)
median = (lst[n//2] + lst[-(n//2+1)]) / 2 if n % 2 == 0 else lst[n//2]
print("Median:", median)
