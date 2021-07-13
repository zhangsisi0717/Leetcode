from collections import defaultdict
from collections import Counter
import copy
import numpy as np
def originalDigits(s: str) -> str:
    numbers = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    letter_to_number = defaultdict(list)
    for key in numbers.keys():
        for l in key:
            letter_to_number[l].append(key)

    counter = Counter(s)
    # order = [[len(letter_to_number[i]),i] for i in counter.keys()]  ##[number of numbers that letter can represent,letter]
    # order = sorted(order)
    candi_set =set()
    for letter in counter.keys(): ##candidates of this string
        for num in letter_to_number[letter]:
            isCandi = True
            for e in num:
                if e not in counter:
                    isCandi = False
                    break
            if isCandi:
                candi_set.add(num)

    def search(counter):
        if not counter: return []

        for key in counter:
            copy_counter = copy.deepcopy(counter)
            for candi in letter_to_number[key]:
                if candi in candi_set:
                    iscandi = True
                    for j in candi:
                        if j not in counter:
                            iscandi = False
                            break
                if iscandi:
                    for letter in candi:
                        copy_counter[letter] -=1
                        if copy_counter[letter] == 0:
                            copy_counter.pop(letter)

                    re = search(copy_counter)
                    if re != False:
                        return [candi] + re

        return False

    final = search(counter)
    return "".join(sorted([str(numbers[i]) for i in final]))


s = "fviefuroowoztneoer"
originalDigits(string)



numbers = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
test = {str(value):key for key,value in numbers.items()}
longnumber = "42342342342354739574982340928382173864726373462000003423948023984234234"
string = ""
for i in longnumber:
    string += test[i]









