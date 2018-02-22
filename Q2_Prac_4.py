# q2_sum_series2.py

def sum_ggseries2(i):
    
    if i == 1:
        return 1 / 3
    else:
        return i / (2 * (i) + 1) + sum_ggseries2(i - 1)
        
n = int(input("Enter number: "))
print("{0:.2f}".format(sum_ggseries2(n)))