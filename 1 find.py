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
