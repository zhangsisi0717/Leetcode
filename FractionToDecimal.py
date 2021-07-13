#https://leetcode.com/problems/fraction-to-recurring-decimal/
def fractionToDecimal(numerator: int, denominator: int) -> str:
    sign = ""
    if numerator * denominator < 0:
        numerator,denominator = abs(numerator),abs(denominator)
        sign = "-"

    mod_to_idx = dict()
    mod = numerator % denominator
    digit = int(numerator / denominator)
    isDecimal = False
    result = ""
    cur_idx,decimal_idx= None,None

    while(mod not in mod_to_idx and mod != 0):
        if not isDecimal:
            result += str(digit) + "."
            cur_idx,decimal_idx = len(result)-1,len(result)-1
            isDecimal = True
            mod_to_idx[mod] = -1
        else:
            result += str(digit)
            mod_to_idx[mod] = cur_idx
        digit = int((mod*10) / denominator)
        mod = (mod * 10) % denominator

        cur_idx +=1

    result += str(digit)
    if mod!=0:
        index = mod_to_idx[mod]
        if index== -1:
            result = result[:decimal_idx+1] + "(" + result[decimal_idx+1:] + ")"
        else:
            result = result[:index+1] + "(" + result[index+1:] + ")"
        return sign + result

    return sign + result



