def majority_element(seq, default=None):
    """Find which element in *seq* sequence is in the majority.

    Return *default* if no such element exists.

    Use Moore's linear time constant space majority vote algorithm
    """
    candidate = default
    count = 0
    for e in seq:
        if count != 0:
            count += 1 if candidate == e else -1
        else: # count == 0
            candidate = e
            count = 1

    # check the majority
    return candidate if seq.count(candidate) > len(seq) // 2 else default

lst = [34,15,34,34,34,34,15,15,34,34,22,15,15,15,15,34,15,34,15,15,34,15,34,15,34,22,22,15,34,15,34,15,34,15,34,22,34,22,34,34,34,34,34,22,15,34,34,34,15,34,15,15,22,34,15,15,34,34,34,22,34,15,15,34,34,34,15,22,22,22,15,34,34,22,34,34,22,34,15,22,34,34,15,22,34,34,34,34,22,22,15,34,34,22,34,34,34,22,34,22]
print(majority_element(lst))