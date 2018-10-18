def search (words,key) :                                        #binary search function
    first = 0
    last = len(words)-1
    while first <= last :
        mid = (first + last)//2
        if words[mid] == key :
            return True
        elif key < words[mid] :
            last = mid - 1
        else :
            first = mid + 1
    return False



with open('Dic.txt', 'r') as reading_dictionary:
    words_list = reading_dictionary.read().split()        # returns a list to save the words in

word = input().lower()

