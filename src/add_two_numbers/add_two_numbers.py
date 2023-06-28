# Definition for singly-linked list.
from typing import *

# node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_of_numbers = f'{l1.val}'
        sum_of_numbers1 = f'{l2.val}'

        curr = l1.next
        curr2 = l2.next
        while curr != None:
            sum_of_numbers = sum_of_numbers + f'{curr.val}'
            curr = curr.next

        while curr2 != None:
            sum_of_numbers1 = sum_of_numbers1 + f'{curr2.val}'
            curr2 = curr2.next

        all_sum = int(sum_of_numbers[::-1]) + int(sum_of_numbers1[::-1])

        new_node = ListNode(all_sum % 10, None)
        all_sum = all_sum // 10

        if all_sum == 0:
            return new_node

        curr5 = new_node
        for i in range(len(str(all_sum))):

            while curr5.next != None:
                curr5 = curr5.next
            curr5.next = ListNode(all_sum % 10)
            all_sum = all_sum // 10

        return new_node


if __name__ == '__main__':
    first = ListNode(2, ListNode(4, ListNode(3)))
    second = ListNode(5, ListNode(6, ListNode(4)))

    sol = Solution()
    data = sol.addTwoNumbers(first, second)

    while data.next != None:
        print(data.val)
        data = data.next
    print(data.val)
