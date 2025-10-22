class Solution:
    def intToRoman(self, num: int) -> str:
        s= str(num)
        l = len(s)
        cup = num
        roman = ""
        while cup > 0:
            if l == 4:
                roman = cup//1000*"M" + roman
                cup = cup - cup//1000
                l = len(str(cup))
            elif l == 3 and cup >= 500:
                if (cup//900 == 1):
                    roman = "CM"+roman
                    cup = cup - cup//900
                    l = len(str(cup))
                else:
                    roman = cup//500*"D" + roman
                    cup = cup - cup//500
                    l = len(str(cup))
            elif l == 3 and cup > 100 and cup <500 :
                if (cup//400 == 1):
                    roman = "CD"+roman
                    cup = cup - cup//100
                    l = len(str(cup))
                else:
                    roman = cup//100*"C"+ roman
                    cup = cup - cup//100
                    l = len(str(cup))
            elif l == 2 and cup >= 50:
                if (cup//90 == 1):
                    roman = "XC"+roman
                    cup = cup - cup//90
                    l = len(str(cup))
                else:
                    roman = (cup//50)*"L" + roman
                    cup = cup - cup//50
                    l = len(str(cup))
            elif l ==2 and cup > 10 and cup <50:
                if (cup//40 == 1):
                    roman = "XL"+roman
                    cup = cup - cup//40
                    l = len(str(cup))
                else:
                    roman = cup//10*"X"+roman
                    l = len(str(cup))
            elif l == 1 and cup >= 5:
                if (cup//9 == 1):
                    roman = 'IX'+roman
                    cup = cup - cup//9
                    l = len(str(cup))
                else:
                    roman = cup//5*'V' + roman
                    cup = cup - cup//5
                    l = len(str(cup))
            elif l ==1 and cup >= 1 and cup <5:
                if (cup//4 == 1):
                    roman = 'IV'+roman
                    cup = cup - cup//4
                    l = len(str(cup))
                else:
                    roman = cup//1*'I'+roman
                    cup = cup - cup//1
                    l = len(str(cup))
        return roman
