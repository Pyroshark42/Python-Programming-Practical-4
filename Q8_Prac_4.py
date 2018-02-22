# q8_find_uppercase.py

def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    if 65 <= ord(str[0]) <= 90:
        return find_num_uppercase(str[1:]) + 1
    else:
        return find_num_uppercase(str[1:])

string = input("Enter a sentence: ")
print("Number of uppercase is/are:",find_num_uppercase(string))