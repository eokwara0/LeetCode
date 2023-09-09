class Solution:
    def searchInsert( self, nums :list, target: int):

        counter = 0
        list_length = len(nums)-1
        while counter <= list_length:
            if nums[counter] == target:
                return counter
            elif nums[list_length - counter ] == target:
                return list_length - counter
            elif target < nums[counter]:
                return counter
            elif target - nums[counter] == 1:
                    return counter + 1
            elif target > nums[list_length - counter]:
                    return (list_length - counter)+1
            counter = counter + 1
        return counter
        


if __name__ == "__main__":
    solution = Solution()
    index = solution.searchInsert([1], 0)
    print(index)