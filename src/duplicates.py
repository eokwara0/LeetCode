import collections
from timeit import timeit

class Solution:
    def containsDuplicate( self , nums: list[int]) -> bool :
        
        counts = collections.Counter( nums )
        for value in counts.values():
            if value > 1:
                return True 
                
        return False 
    
        
    
    
    
    
    
if __name__ == "__main__":
    print(timeit( lambda : Solution().containsDuplicate( [1,2,3,4 ]) , number=1))