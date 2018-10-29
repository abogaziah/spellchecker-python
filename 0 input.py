word= input("type a word ")
word.lower()

def read_dict(dict_name):
    """reads words from txt file into list"""
    text_file = open(dict_name, "r")
    dict = text_file.read().splitlines()
    text_file.close()
    return dict
help(read_dict)