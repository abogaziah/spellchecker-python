import difflib
import bisect

def read_dict(dict_name):
    """"reads words from txt file into list"""
    text_file = open(dict_name, "r")
    dict = text_file.read().splitlines()
    text_file.close()
    return dict


def find(dict, word):
    """finds a word in a dictionary, using binary search"""
    l = 0
    r = len(dict) - 1
    while r>=l:
        mid=(r+l)//2

        if dict[mid]==word:
            return True
        elif dict[mid]<word:
            l=mid+1
        else:
            r=mid-1

    return False


def action(dict, word, words, count):
        """lets you decide to replace, skip or add the word to dictionary"""

        replace= difflib.get_close_matches(word,dict,3)         #genrates max of 3 elements list(called replace) with best matches
        choice=0
        while True:
            if len(replace)<1:                                  #the list replace is empty, no close matches found
                print("no close matches.")
                break
            else:
                print("did you mean:")
                for i in range(len(replace)):                   # for loop generates choice list based on number of matches found
                    print(i+1, replace[i])
                print(len(replace)+1, "skip")
                print(len(replace)+2, "add it to dictionary")
                print(len(replace) + 3, "other (you'll type it)")
                choice=int(input())

                if choice>0 and choice<7  :                     #won't exit the loop untill getting correct choice
                    break
        if choice== len(replace)+3:
            words[count - 1]=input("type it")
        elif choice== len(replace)+2:
            p_dic(words[count-1])                               #if user chooses to add the word. call p_dic()
        elif choice!=len(replace)+1 and choice!=0:
            words[count-1]=replace[choice-1]                    #if user chooses a correction, update the string


def p_dic(nw):
    """"adds a word to the personal dictionary file(p_dic.txt) """
    print(nw, "is added")
    dict=read_dict("p_dic.txt")                                 #loads the personal dictionary into a list

    bisect.insort(dict, nw)                                     #inserts the word in its correct place, to keep it sorted

    f= open("p_dic.txt","w")
    for word in dict:                                           #writes the list back to the txt file
        f.write("%s\n" % word)
    f.close

def main():
    dict=read_dict("Dic.txt")
    p_dict=read_dict("p_dic.txt")

    phrase = input("type a phrase")                             #takes input, saves it to list or strings
    words = phrase.split()
    count=0                                                     #words counter

    for word in words:                                          #itrates over words in the phrase, and checks them
        count+=1
        word=word.lower()                                       #lowecase the words so they have same ASCII as the dic

        if word[-1]=="."or word[-1]==",":                       #skips punctuation
            word= word[:-1]
        if word[-3:]=="n't" or word[-3:]=="'ve" or word[-3:]=="'re":
            word=word[:-3]
        if word[-2:]=="'s" or word[-2:]=="'d":
            word=word[:-2]

        if find(dict, word)==False and find(p_dict, word)==False:
            print(word, "is wrong")                             # if the word isn't found netiher in dict nor p.dict, call action
            action(dict, word, words, count)
    print("paragraph is", count, "words")
    for word in words:                                          #prints out the correct phrase
        print(word, end=" ")
if __name__ == '__main__':
    main()
