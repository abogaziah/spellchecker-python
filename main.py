import difflib

                                                    # read dic.txt into a list.
text_file= open("Dic.txt","r" )
dict = text_file.read().splitlines()
text_file.close()

                                                    # get input and save it list of words.
phrase=input("type a phrase")
words=phrase.split()

count=0                                             #counter for iterations


for word in words:                                  #loop over phrase words
    word=word.lower()                               #check for being lowecase to have identical ASCII code

    def find(dict, word):                           #find input in dictionary , using binary search.
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




    if find(dict,word)== False:                        #taking actions in case it wasn't found
        print(word, "is wrong")

        replace= difflib.get_close_matches(word,dict,3)         #genrates a 3 elemnts list with best mathces
        choice=0
        while True:                                             #make user choose what he ment or skip
            print("did you mean:")
            print(1,replace[0])
            print(2,replace[1])
            print(3,replace[2])
            print(4,"ignor")
            choice=int(input())
            if choice==1 or choice==2 or choice==2 or choice==3 or choice==4 :
                break
        if choice!=4:
           words[count]=replace[choice-1]
    count+=1



for word in words:                                              #print out the new phrase
    print(word, end=" ")