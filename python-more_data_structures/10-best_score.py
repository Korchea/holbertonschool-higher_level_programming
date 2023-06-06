#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = next(iter(a_dictionary))
    for key, value in a_dictionary.items():
        if value > a_dictionary.get(best):
            best = key
    return best
