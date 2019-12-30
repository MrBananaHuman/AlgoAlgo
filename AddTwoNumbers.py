# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_num = 0
        val = 1
        stop_flag = False
        while(True):
            if stop_flag == True:
                break
            if l1.next == None:
                stop_flag = True
            first_num += l1.val * val
            val *= 10
            l1 = l1.next
        stop_flag = False
        second_num = 0
        val = 1
        while(True):
            if stop_flag == True:
                break
            if l2.next == None:
                stop_flag = True
            second_num += l2.val * val
            val *= 10
            l2 = l2.next
        added_num = str(first_num + second_num)
        result = ListNode(added_num[0])
        result.next = None
        for char in added_num[1:len(added_num)]:
            temp_listNode = ListNode(char)
            temp_listNode.next = result
            result = temp_listNode
        return result
