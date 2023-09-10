
class Solution:

    def lengthOfLastWord(self,s:str) -> int:
        data = s.split(' ')
        data = list(filter(lambda x : x != "" , data))
        print(data)
        return len(data[-1])
    

if __name__ == "__main__":
    print(Solution().lengthOfLastWord('    fly me   to   the moon   '))