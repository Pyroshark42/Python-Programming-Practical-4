# q3_find_gcd.py

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return m % n

print(gcd(24, 16))
print(gcd(255, 25))