def get_text_number(text):
    word_count = 0
    book_text_list = text.split()
    for word in book_text_list:
        word_count += 1
    return word_count
def get_letter_count(word):
    letters={}
    for xyz in word:
        abc = xyz.lower()
        if abc in letters:
            letters[abc] +=1
        else:
            letters[abc] =1
    return letters
def new_dic(letters):
    listdic = []
    for key,value in letters.items():
        if key.isalpha():
            listdic.append((key,value))
    return listdic
def sort_on(dic):
    return dic[1]