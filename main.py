from typing import Optional, Iterator, List
from util import *

class Solution:
    #387. First Unique Character in a String
    def firstUniqChar(self, s: str) -> int:
        listOfCaracthers = dict()
        for index, i in enumerate(s):
            if i not in listOfCaracthers:
                listOfCaracthers[i] = {
                    "indexOfFirst": index,
                    "count": 1
                }
            else:
                listOfCaracthers[i]["count"] += 1
        for b in listOfCaracthers.values():
            if b["count"] == 1:
                return b["indexOfFirst"]
        return -1
    #538. Convert BST to Greater Tree
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def transverseBST(root: TreeNode | None) -> Iterator[TreeNode | None]:
            NoneRoot = root is not None
            if NoneRoot: yield from transverseBST(root.right)
            yield root
            if NoneRoot: yield from transverseBST(root.left)
        valueToSum = 0
        for i in transverseBST(root):
            if i is not None:
                i.val += valueToSum
                valueToSum = i.val
        return root
    # 1038. Binary Search Tree to Greater Sum Tree
    def bstToGst(self, root: TreeNode) -> TreeNode:
        return self.convertBST(root)
    #1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #challenge: not O(n^2)
        hmap = dict()
        for index, i in enumerate(nums):#O(n)
            if i not in hmap: #O(1) since it's a hashmap
                #current_i + future_i = target <=>target-current_i = future_i,
                #so this will record the index of current i to get when future_i appears
                hmap[target-i] = index
            else:
                #this i is now future_i
                return [hmap[i], index]
        return [-1, -1]
    #7. Revserse Integer
    def reverse(self, x: int, outsideRange=True) -> int:
        rev = 0
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False
        while x != 0:
            # region find the last digit of x
            lastDigit = x % 10
            # endregion
            # region add last digit to reversed x
            rev = rev * 10 + lastDigit
            # endregion
            # region remove last digit from x
            x //= 10
            # endregion9
        if outsideRange and rev > (2**31) - 1: return 0
        return -rev if neg else rev
    #9. Palindrome Number
    def isPalindrome(self,  x: int) -> bool:
        if x < 0: return False
        #Challenge: Could you solve it without converting the integer to a string?
        return x == self.reverse(x, False)
    #2. Add Two Numbers
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = ret = ListNode()
        oneMore, lastNumber = False, None
        while True:
            ret.val = l1.val + l2.val
            if oneMore: ret.val += 1
            if ret.val >= 10:
                ret.val -= 10
                oneMore = True
            else:
                oneMore = False
            l1, l2 = l1.next, l2.next
            if None in [l1, l2]:
                #one list reached the end
                break
            #both lists still have more numbers
            ret.next= ListNode()
            ret = ret.next
        notFinished = l2 if l1 is None else l1
        if notFinished is None:
            #both reached the end, which means they are of same size, which means only 1 can be aside
            if oneMore: ret.next = ListNode(1)
            return firstNode
        while True:
            if oneMore:
                ret.next = ListNode(notFinished.val + 1)
                if ret.next.val == 10:
                    ret.next.val = 0
                    ret.next.next = ListNode(1)
                else:
                    oneMore = False
            else:
                ret.next = ListNode(notFinished.val)
            if notFinished.next is None:
                return firstNode
            else:
                ret, notFinished = ret.next, notFinished.nextx
    #1338. Reduce Array Size to The Half
    def minSetSize(self, arr: List[int]) -> int: #TODO refazer q a lista está infinita
        halfArr = len(arr)//2
        if halfArr == 0: return halfArr
        class Node:
            def __init__(self, val, prev= None, next = None):
                self.val = val
                self.prev = prev
                self.next = next

        #first is biggest, last is smallest
        mapp: dict[int, Node] = dict()
        mapp[arr[0]] = lastNode = firstNode = Node(1)
        for i in arr[1:]:
            n = mapp.get(i)
            if n is None:
                #region new number found, so make n the last because uts the smallest
                n = Node(1, prev=lastNode)
                mapp[i] = n
                lastNode.next, lastNode = n, n
                #endregion
            else:
                #region get node of number previous seen and increment the seen times TODO wrong
                n.val += 1
                if n.val == 4:
                    pass
                #endregion
                #region bubble new priority number to right palce to have the queue ordered
                while n.prev is not None and n.prev.val < n.val:
                    #[A] <-> B <-> n <-> [D] TO [A] <-> n <-> B <-> [D]
                    B, D = n.prev, n.next
                    A = B.prev
                    if A is not None:
                        A.next = n
                    n.prev, n.next = A, B
                    B.prev, B.next = n, D
                    if D is not None:
                        D.prev = B
                #endregion
                if n.prev is None: firstNode = n
        ret = 0
        #TODO linnked list is on infinite loop
        while True:
            if firstNode.next is None:
                break
            if firstNode.next.val > firstNode.val:
                pass
        while True:

            ret += 1
            halfArr -= firstNode.val
            if halfArr <= 0: return ret
            firstNode = firstNode.next
    def minSetSizeLazy(self, arr: List[int]) -> int:
        mapp = dict()
        for i in set(arr):
            mapp[i] = arr.count(i)
        halfArr = len(arr) // 2
        s = sorted(mapp.values(), reverse=True)
        for index, i in enumerate(s):
            halfArr -= i
            if halfArr <= 0: return index+1
        return 0
if __name__ == "__main__":
    a = Solution()
    l = [3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(a.minSetSize([2,28,92,30,100,52,28,48,91,27,66,19,11,53,91,95,74,51,65,65,96,81,21,55,98,3,2,89,99,57,78,34,50,2,57,76,23,90,89,36,53,22,73,59,95,45]))
    print(14)