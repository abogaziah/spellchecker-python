def action(dict, word, words, count):
        """lets you decide to replace, skip or add the word to dictionary"""

        replace= matches(word,dict)         #genrates max of 3 elements list(called replace) with best matches
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
                print(len(replace)+3, "other (you'll type it)")
                choice=int(input())

                if choice>0 and choice<len(replace)+4:                     #won't exit the loop untill getting correct choice
                    break
        if choice== len(replace)+3:
            words[count - 1]=input("type it")
        elif choice== len(replace)+2:
            p_dic(words[count-1])                               #if user chooses to add the word. call p_dic()
        elif choice!=len(replace)+1 and choice!=0:
            words[count-1]=replace[choice-1]                    #if user chooses a correction, update the string
7