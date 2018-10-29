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