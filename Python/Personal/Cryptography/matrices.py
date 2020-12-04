
numbers = [[8, 5, 10], [21, 8, 21], [21, 12, 8]]
mult_by = [11, 20, 5]
total = 0
total_nums = []

for a, b, c in numbers:
    total += a * mult_by[0]
    total += b * mult_by[1]
    total += c * mult_by[2]
    print(str(total % 26))
    total = 0
    