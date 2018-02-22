# q5_count_letter.py

def count_letter(word, char='e'):
    count = 0
    for c in word:
        if c == char:
            count += 1
    return count
    
print(count_letter("Welcome", 'e'))