class Decodewyas:  # Decode Ways https://leetcode.com/problems/decode-ways/
    """
    numWaysF(size=n) = numWaysF(size=n-1) + numWaysF(size=n-2), if lastOne figures !=0 and lastTwo figures <=26
    """

    def numDecodings(self, s: str) -> int:
        def subStr(size, numDic):
            if size in numDic.keys():
                print(f'size : {size} in the dict')
                return numDic[size]

            print(numDic)
            if size == 1:
                numDic[size] = 1
                return 1
            elif size == 2 and int(s[1]) != 0:
                if int(s[:2]) <= 26:
                    numDic[size] = 2
                    return 2
                else:
                    numDic[size] = 1
                    return 1
            elif size == 2 and int(s[1]) == 0:
                if int(s[:2]) <= 26:
                    numDic[size] = 1
                    return 1
                else:
                    numDic[size] = 0
                    return 0

            sum1 = subStr(size - 1, numDic)
            sum2 = subStr(size - 2, numDic)
            lastTwo = s[size - 2:size]
            lastOne = int(s[size - 1:size])

            if lastOne == 0 and int(lastTwo[0]) == 0:
                numDic[size] = 0
                return 0
            elif lastOne == 0 and int(lastTwo[0]) != 0:
                if int(lastTwo[:]) <= 26:
                    numDic[size] = sum2
                    return sum2
                else:
                    numDic[size] = 0
                    return 0
            elif lastOne != 0 and int(lastTwo[0]) == 0:
                numDic[size] = sum1
                return sum1

            elif lastOne != 0 and int(lastTwo[0]) != 0:
                if int(lastTwo[:]) <= 26:
                    numDic[size] = sum1 + sum2
                    return sum1 + sum2
                else:
                    numDic[size] = sum1
                    return sum1

        if int(s[0]) == 0:
            return 0
        else:
            numDic = dict()
            return subStr(len(s), numDic)

# test case: "6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"=0
