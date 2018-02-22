# q6_compute_sum.py

def sum_digits(n):
    num = str(n)
    digitSum = 0
    for i in num:
        digitSum += int(i)
    return digitSum
print(sum_digits(875))