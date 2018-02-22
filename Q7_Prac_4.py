#  q7_find_largest.py

def find_largest(alist):
    if len(alist) == 1:
        return alist
    elif len(alist) == 0:
        print("No list available.")
    else:
        return max(alist)
    
alist = [5, 1, 8, 7, 2]
print(find_largest(alist))