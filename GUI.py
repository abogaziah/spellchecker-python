import difflib
from tkinter import *



'''GUI'''

root = Tk()

entry_word = StringVar()
user_entry = Entry(root, textvariable = entry_word )
user_entry.grid (row = 0 , column = 0 )


label_1 = Label(root)
label_1.grid(row = 3)

label_2 = Label(root , fg ='green')
label_2.grid(row = 10)

global var
var = IntVar()
suggestionslist = Listbox(root , height = 5, selectmode = SINGLE)
suggestionslist.grid(row = 4)




'''GUI End'''

with open('Dic.txt', 'r') as reading_dictionary:
    words_list = reading_dictionary.read().split()               # returns a list to save the dictionary words in



def Select(event) :
    selection_index = suggestionslist.curselection()             #returns a tuple of the index of selected element
    word = suggestionslist.get(selection_index[0])               #returns the value of the given index
    label_2['text'] += (word + ' ')
    var.set(1)


suggestionslist.bind ("<Double-Button-1>", Select)



def lowercase (word) :                                          #function that returns the word in lowercase
    newword = ''
    for character in word :
        if ord(character) in range (65,91):
            character = chr(ord(character)+32)
        newword += character
    return newword


def search (key) :                                               #binary search function
    first = 0
    last = len(words_list)-1
    while first <= last :
        mid = (first + last)//2
        if words_list[mid] == key :
            return True
        elif key < words_list[mid] :
            last = mid - 1
        else :
            first = mid + 1
    return False



def button_function() :                                                                             #function to get the word the user entered from the entry
    label_2['text'] =''
    phrase = entry_word.get().split()
    for word in phrase :
        word = lowercase(word)

        if search(word) == False:
            label_1['fg'] = 'red'
            label_1['text'] = ('%s is wrong Did you mean ... \n' %word)
            matching_ratio = []
            for element in words_list:
                matching_ratio.append(difflib.SequenceMatcher(None, word, element).ratio())
            suggestions = [x for (ratio, x) in sorted(zip(matching_ratio, words_list))]                 # (ratio,x) is a tuple of the matching ratio and the word
            i = 0
            for sug in suggestions[:-6:-1]:
                suggestionslist.insert(i,sug)
                i += 1
            suggestionslist.wait_variable(var)
            suggestionslist.delete(0,4)

        else :
            label_1['text'] = ''
            label_2['text'] += (word + ' ')

    label_1['text'] = 'Done'


'''GUI'''

search_button = Button (root , text = 'Search' ,command = button_function)
search_button.grid(row = 1, column = 0 )

button_2 = Button(root , text = 'ignore')
button_2.grid(row=9, column=0)

root.mainloop()

'''GUI End'''



