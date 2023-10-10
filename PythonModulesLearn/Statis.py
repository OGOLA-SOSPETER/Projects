import statistics

marks = [56,77,89,90,66,88]

avg = statistics.mean(marks)
med = statistics.median(marks)
medlow = statistics.median_low(marks)
medhigh = statistics.median_high(marks)
medgroup = statistics.median_grouped(marks,10)
geommean = statistics.geometric_mean(marks)


print(f'Median: {med}')
print(f'Average/Mean: {avg}')
print(f'Median Low: {medlow}')
print(f'Median High: {medhigh}')
print(f'grouped data = {medgroup}')
print(f'Geometric mean = {geommean}')

