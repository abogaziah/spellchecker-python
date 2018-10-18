import bisect

def read_dict(dict_name):
    text_file = open(dict_name, "r")
    dict = text_file.read().splitlines()
    text_file.close()
    return dict


def p_dict(nw):
    dict=read_dict("p_dic.txt")
    bisect.insort(dict, nw)
    print(dict)

    f= open("p_dic.txt","w")
    for word in dict:
        f.write("%s\n" % word)
    f.close
def main():
    p_dict("ab")


if __name__ == '__main__':
    main()