from difflib import SequenceMatcher

def matches(word, possibilities, n=3, cutoff=0.6):
    result = []
    s = SequenceMatcher()
    s.set_seq2(word)
    for x in possibilities:
        s.set_seq1(x)
        if s.real_quick_ratio() >= cutoff and \
                s.quick_ratio() >= cutoff and \
                s.ratio() >= cutoff:
            result.append((s.ratio(), x))

    # Move the best scorers to head of list
    result.sort(key=lambda x: x[0], reverse=True)
    if len(result)>n:
        result=result[0:n]
    # Strip scores for the best n matches
    return [x for score, x in result]

def read_dict(dict_name):
    """"reads words from txt file into list"""
    text_file = open(dict_name, "r")
    dict = text_file.read().splitlines()
    text_file.close()
    return dict

def action(replace):
    """lets you decide to replace, skip or add the word to dictionary"""
    choice = 0
    while True:
        if len(replace) < 1:
            print("no close matches.")
            return None
        else:
            print("did you mean:")
            for i in range(len(replace)):
                print(i + 1, replace[i])
            choice = int(input())

        if choice>0 and choice<len(replace)+1:
            break

    return replace[choice - 1]

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


def main():
    word = input("type a word ")
    word.lower()
    dict=read_dict("dic.txt")
    if find(dict, word)== False:
        replace = matches(word, dict)
        print(action(replace))
    else: print(word)
if __name__ == '__main__':
    main()

