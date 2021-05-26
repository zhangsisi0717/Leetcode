#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/fu
#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/fu
def removeDuplicates(self, s: str, k: int) -> str:
    string = s
    change = True
    while(change):
        new_s = ""
        change = False
        prev = string[0]
        count = 1
        for i in range(1,len(string)):
            if string[i] == prev:
                count += 1
                if count == k:
                    count =0
                    change = True
                continue


            new_s += count*prev
            prev = string[i]
            count = 1

        new_s = new_s + count*prev
        string = new_s

    return new_s
