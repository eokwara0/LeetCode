

from timeit import timeit


class Solution:
    
    __symbol = { "I" : 1 , "IV": 4 , "V": 5 , "IX": 9 , "X": 10 , "XL": 40 , "L": 50 , "XC" : 90 , "C" : 100  , "CD" : 400 , "D" : 500 , "CM" : 900 , "M" : 1000 }
    __data = reversed(__symbol.keys())
    
    
    def int_to_roman( self , num : int ) -> str:  # type: ignore
        
        if num <= 0 : 
            return ""
        else:
            for key in self.__data:
                if num % self.__symbol[key] < num  :
                    num -= self.__symbol[key]
                    return key  + self.int_to_roman( num )
                
        
        
if __name__ == '__main__':
    print(timeit( lambda : Solution().int_to_roman( 1994 ) , number=1))