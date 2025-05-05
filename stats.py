def num_words(text):
    t = text.split()
    return len(t)

def character_amount(amount):
    characters = {}
    amount = amount.lower()

    for a in amount: 
        if a in characters:
            characters[a] += 1 
        else:
            characters[a] = 1
   
    return characters

def sort_on(d):
    return d["num"]

def sort_character_counts(char_counts):
    sorted_list = []
    for ch in char_counts:
        sorted_list.append({"char": ch, "num": char_counts[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

