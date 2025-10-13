class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator >= denominator:
            quotient = numerator//denominator
            remainder = numerator % denominator
            if remainder == 0:
                return str(quotient)
            flag = False
            dec =''
            while flag==False:
                quo_dec = (remainder*10)//denominator
                remainder = (remainder*10)%denominator 
                dec = dec+str(quo_dec)
                if remainder == 0:
                    return str(quotient)+'.'+str(dec)
                else:
                    for i in range(0,len(dec)):
                        for j in range(i,len(dec)):
                            sub = dec[0:i]
                            if len(dec)%len(sub) == 0:
                                pat_len = len(dec)/len(sub) 
                                pat = pat_len * sub
                                if pat == dec:
                                    return str(quotient)+'.'+'('+str(sub)+')'
        else:
            quotient = 0
            flag = False
            dec =''
            remainder = numerator % denominator
            while flag==False:
                quo_dec = (remainder*10)//denominator
                remainder = (remainder*10)%denominator 
                dec = dec+ str(quo_dec)
                if remainder == 0:
                    return str(quotient)+'.'+str(dec)
                else:
                    for i in range(0,len(dec)):
                        for j in range(i+1,len(dec)):
                            sub = dec[0:j]
                            if len(dec)%len(sub) == 0:
                                pat_len = len(dec)//len(sub) 
                                pat = pat_len * sub
                                if pat == dec:
                                    return str(quotient)+'.'+'('+str(sub)+')'
