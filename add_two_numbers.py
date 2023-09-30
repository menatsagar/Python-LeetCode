"""
You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit.
   Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def addTwoNumbers(self, l1,l2):
    prev = result = ListNode(None)
    carry   = 0
    while l1 or l2 or carry:
      if l1:
        carry+=l1.val
        l1 = l1.next
        
      if l2:
        carry += l2.val
        l2 = l2.next

      prev.next = ListNode(carry%10)
      prev  = prev.next
      carry //=10
    return f"{result.next.next.next.val}{result.next.next.val}{result.next.val}"
  
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()

result = solution.addTwoNumbers(l1, l2)

  
print(result)