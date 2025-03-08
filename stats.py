
def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_char_instances(text):
    word_dict = {}
    for char in text.lower():
        if char not in word_dict:
            word_dict[char]=1
        else:
            word_dict[char]+=1

    return word_dict

def sort_on(dict: dict):
    return dict["value"]

def format_dict(base_dict):
    sort_list = []
    for c in base_dict:
        sort_list.append({
            "char": c,
            "value": base_dict[c]
        })
    sort_list.sort(reverse=True,key=sort_on) 
    return sort_list