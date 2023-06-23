from timeit import timeit

# converting number into roman numerals
    # 

class Solution:
    
    __symbol = { "I" : 1 , "IV": 4 , "V": 5 , "IX": 9 , "X": 10 , "XL": 40 , "L": 50 , "XC" : 90 , "C" : 100  , "CD" : 400 , "D" : 500 , "CM" : 900 , "M" : 1000 }
    __data = list(__symbol.keys())[::-1]
    
    
    def int_to_roman( self , num : int ) -> str:  # type: ignore
        key_ = ""
        if num <= 0:
            return ""
        else :
            for key in self.__data:
                if num % self.__symbol[key] < num  :
                    num -= self.__symbol[key]
                    key_ = key
                    return key_  + self.int_to_roman( num )

if __name__ == '__main__':
    for i in range(1,20,2):
        print(Solution().int_to_roman(i))