def count_words(text):
    list_words = text.split()
    return len(list_words)

def count_chars(text):
    lower_case_text = text.lower()
    chars_dict = {}
    for char in lower_case_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else: chars_dict[char] = 1
    return chars_dict

def sort_on(item): 
    return item["num"]

def sort_chars(chars_dict):  
    dict_list = []
    for char in chars_dict:
        paired_dict = {"char": char, "num": chars_dict[char]}
        dict_list.append(paired_dict)
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list


