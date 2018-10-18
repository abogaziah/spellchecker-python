import difflib

                                                    # read dic.txt into a list.
text_file= open("Dic.txt","r" )
dict = text_file.read().splitlines()
text_file.close()

                                                    # get input and save it in lowercase.
word=input("type a word")
word=word.lower()

                                                    # find input in dictionary list the list, using binary search.
def find(dict, word):
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

print(find(dict,word))


if find(dict,word)== False:
    replace= difflib.get_close_matches(word,dict,3)
    choice=0
    while True:
        print("did you mean:")
        print(1,replace[0])
        print(2,replace[1])
        print(3, replace[2])
        choice=int(input())
        if choice==1 or choice==2 or choice==2 or choice==3:
            break
    print(replace[choice-1])

