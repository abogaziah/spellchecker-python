def action(replace):
    choice = 0

    while True:
        if len(replace)==0:
            print("no close matches.")
            break
        else:
            print("did you mean:")
            for i in range(len(replace)): print(i + 1, replace[i])

            choice = int(input())
            if choice > 0 and choice < len(replace)+1: break

    return replace[choice - 1]