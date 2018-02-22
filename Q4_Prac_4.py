# q4_print_reverse.py

def reverse_int(n):
    
    if len(n) == 1:
        return n
    else:
        return n[-1]+reverse_int(n[:-1])
    
x = input("Enter number for reversal: ")
print(reverse_int(x))