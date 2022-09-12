#### Two Sum
    # Given an array of integers nums and an 
    # integer target, return indices of the two 
    # numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution:
    
    def twoSum ( self , nums: list[int] , target : int ):
        
        for a , b in enumerate( nums ):
            for ( c , d ) in enumerate( nums[ a + 1 : ] ) : 
                
                if d + b == target : 
                    return [ a , c + a + 1 ] 

