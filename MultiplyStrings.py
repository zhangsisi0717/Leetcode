##https://leetcode.com/problems/multiply-strings/
import copy
"""
multiply two strings:
1. implement multiple digit * one_digit
2. implement string sum method to add up all the multiplication results
"""
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0": return "0"
    def oneDigit(multiDig,oneDig):
        add = 0
        result=""
        for i in range(len(multiDig)-1,-1,-1):
            digit = (int(multiDig[i])*int(oneDig)+add) % 10
            add = (int(multiDig[i])*int(oneDig)+add) // 10
            result = str(digit) + result

        return str(add)+result if add>0 else result

    def sumTwo(num1,num2):
        i,j = len(num1)-1,len(num2)-1
        add,result = 0,""
        while(i>=0 or j>=0):
            num1_d = num1[i] if i>=0 else 0
            num2_d = num2[j] if j>=0 else 0
            digit = (int(num1_d) + int(num2_d) + add) % 10
            add = (int(num1_d) + int(num2_d) + add) // 10
            result = str(digit) + result
            i-=1
            j-=1
        return "1"+result if add>0 else result

    result = "0"
    for i in range(len(num2)-1,-1,-1):
        temp = oneDigit(num1,num2[i]) + (len(num2)-1-i)*"0"
        result = sumTwo(result,temp)

    return result