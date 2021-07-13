from collections import defaultdict
from collections import  Counter
s  = "owoztneoerfviefuro"
"""
step 1: letter_to_candidate dict() for thi string
step 2: sort the letters by number of candidates (we want to try letters with less candidates first)
step 3: dfs to search for result
"""
def originalDigits(s: str) -> str:
    numbers = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    letter_to_number = defaultdict(set)
    for key in numbers.keys():
        for l in key:
            letter_to_number[l].add(key)

    counter = Counter(s)
    candi_dict = defaultdict(set)
    for letter in counter.keys(): ##candidates of this string
        for num in letter_to_number[letter]:
            isCandi = True
            for e in num:
                if e not in counter:
                    isCandi = False
                    break
            if isCandi:
                candi_dict[letter].add(num)
    order_candi = sorted([[len(candi_dict[i]),i] for i in candi_dict.keys()])
    def search(counter):
        non_zero=0
        for occurence, key in order_candi:
            if counter[key]>0:
                non_zero +=1
                for candi in candi_dict[key]:
                    iscandi = True
                    for j in candi:
                        if counter[j]<=0:
                            iscandi = False
                            break
                    if iscandi:
                        for letter in candi:
                            counter[letter] -=1
                        re = search(counter)
                        if re != False:
                            return [candi] + re

                        for letter in candi:
                            counter[letter] +=1

        return [] if non_zero == 0 else False

    final = search(counter)
    return "".join(sorted([str(numbers[i]) for i in final]))

s  = "owoztneoerfviefuroowoztneoerfviefuro"
originalDigits(s)
