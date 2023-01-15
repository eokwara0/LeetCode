from typing import List


def d(arr : List[int]):
    arr[1] = 208304839048

def dime(arr : List[int]):
    arr[0] = 1000000000

def main(arr):
    dime(arr)
    d(arr)

if __name__ == '__main__':
    nums = [2,3,5,3]
    main(nums)

    print(nums)