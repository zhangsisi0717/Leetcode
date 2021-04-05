def numberToWords(num): ##https://leetcode.com/problems/integer-to-english-words/submissions/
    number = {"0":("","Ten"),"1":("One","Eleven"),"2":("Two","Twelve","Twenty",),"3":("Three","Thirteen","Thirty"), "4":("Four","Fourteen","Forty"),"5":("Five","Fifteen","Fifty"),"6":("Six","Sixteen","Sixty"),"7":("Seven","Seventeen","Seventy"),"8":("Eight","Eighteen","Eighty"),"9":("Nine","Nineteen","Ninety"),"10":("Ten","")}
    unit = {2:"Thousand",1:"Million",0:"Billion"}

    def genWords(sub):
        if len(sub)==1:
            return number[sub][0]
        if len(sub) ==2:
            if int(sub[0]) > 1 and int(sub[1]) ==0:
                return number[sub[0]][2]
            elif int(sub[0]) > 1 and int(sub[1]) !=0:
                return number[sub[0]][2] + " " + number[sub[1]][0]
            elif int(sub[0]) == 1 :
                return number[sub[1]][1]
        if len(sub) ==3:
            if genWords(str(int(sub[1:]))):
                return number[sub[0]][0] + " "+ "Hundred "+ genWords(str(int(sub[1:])))
            else:
                return number[sub[0]][0] + " "+ "Hundred"

    strNum = str(num)
    sub1,sub2,sub3,sub4="","","",""
    if len(strNum)<=3:
        return genWords(strNum)
    if len(strNum)>3:
        sub1 = genWords(str(int(strNum[-3:])))

    if len(strNum)<=6:
        sub2 = genWords(str(int(strNum[:-3])))
    elif len(strNum)>6:
        sub2 = genWords(str(int(strNum[-6:-3])))
        if len(strNum)<=9:
            sub3 = genWords(str(int(strNum[:-6])))
        else:
            sub3 = genWords(str(int(strNum[-9:-6])))
            sub4 = genWords(str(int(strNum[:-9])))

    all = (sub4,sub3,sub2,sub1)
    result=""
    for i in range(4):
        if all[i] and i<3:
            if result:
                result = result + " " + all[i] + " "+ unit[i]
            else:
                result = result + all[i] + " "+ unit[i]
        if all[i] and i==3:
            if result:
                result = result + " " + all[i]
            else:
                result = result + all[i]
    return result


numberToWords(400000006)
numberToWords(1000)

















genWords("110")

a="11"
genWords("0"+a)
