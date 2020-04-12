import heapq
from typing import List
from collections import Counter
"""2020 04 mouth leetcode program"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 4/10
class MinStack:

    def  __init__(self):
        self.res = []

    def push(self, x):
        if not self.res:
            self.res.append( (x,x) )
        else:
            self.res.append( (x, min(x, self.res[-1][1])))

    def pop(self):
        if self.res:
            self.res.pop()
        else:
            return None

    def top(self):
        if self.res:
            return self.res[-1][0]

    def getMin(self):
        if self.res:
            return self.res[-1][1]


class solution:

    # 4/ 1Single Number
    def singleNumber(self, nums:List[int]):
        # #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == 1:
                return i
        # nums = sorted(nums)
        # for i in range(1,len(nums)-1,2):
        #     if len(nums) % 2 == 1:
        #         return nums[-1]
        #     else:
        #         if nums[i] != nums[i-1] :
        #             return nums[i]

    # 4/2  Happy Number
    def isHappy(self, n: int) -> bool:
        def standard(n):
            res, count = [], 0
            while n !=0:
                b = n%10
                res.append(b)
                n = n//10
            for i in res:
                count += i**2
            return count
        m = set()
        while n != 1:
            n = standard(n)
            if n in  m: return False
            else:       m.add(n)
        return True

    # 4/2
    def ishappy(self, n:int):
        all_number = set()
        while n !=1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in all_number:
                return False
            else:
                all_number.add(n)
        return True

    # 4/3
    def maxSubArray(self, nums: List[int]) -> int:
        # DP，找到当前最大值，全部最大值取当前最大值和之前最大值的最大值~
        if not nums: return 0
        cursum, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)
            maxsum = max(maxsum, cursum)
        return maxsum

    # 4/4
    def moveZeroes(self, nums:List[int]):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums

    # 4/5
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            cur = prices[i+1] - prices[i]
            if cur >0:
                profit += cur
        return profit

    # 4/6
    def groupAnagrams(self, strs:List[str]):
        if not strs:    return None
        dic = {}
        for s in strs:
            ch = "".join(sorted(s))
            if ch in dic:    dic[ch] += [s]
            else:           dic[ch] = [s]
        return dic.values()

    # 4/7
    def countElements(self, arr: List[int]) -> int:
        count, dic = 0, {}
        for i in arr:
            if i in dic:    dic[i] += 1
            else:           dic[i] = 1
        arr1 = set(arr)
        for i in arr1:
            if i+1 in dic:
                count += dic[i]
        return count

    # 4/8
    def middleNode(self, head: ListNode) -> ListNode:
        fast =  low = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low

    # 4/9
    def backspaceCompare(self, S: str, T: str) -> bool:
        def handle(s:str, res):
            if not s: return ""
            for ch in s:
                if res and ch == '#':   res.pop()
                if ch != '#':           res.append(ch)
            return "".join(res)
        res1, res2 = [], []
        res1 = handle(S, res1)
        res2 = handle(T, res2)
        print(res1,res2)
        return res1 == res2

    # 4/10
    # 4/11
    def diameterOfBinaryTree(self, root) -> int:
        # DFS search return the depth sum of left tree and right tree
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

    # 4/12
    def lastStoneWeight(self,stones):
        # h = [-x for x in stones]
        # heapq.heapify(h)
        # while len(h) > 1 and h[0] != 0:
        #     heapq.heappush(h, heapq.heappop(h)-heapq.heappop(h))
        # return -h[0]
        for i in range(len(stones)-1):
            stones.sort()
            a = stones.pop() - stones.pop()
            stones.append(a)
        return stones[0]


if __name__ == '__main__':
    s = solution()
    # nums =  [2,2,1]
    # n = 19
    # nums = [0,1,0,3,12]
    # print(s.isHappy(n),  s.ishappy(n))
    # print(s.moveZeroes(nums))
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [7,1,5,3,6,4]
    # nums2 = [1,2,3,4,5]
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # print(s.groupAnagrams(strs))
    # arr = [1, 1, 3, 3, 5, 5, 7, 7]
    # S = "y#fo##f"
    # T = "y#f#o##f"
    # ans = s.backspaceCompare(S,T)
    # print(ans)
    # obj = MinStack()
    # obj.push(3)
    # obj.push(2)
    # obj.push(-1)
    # # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    # print(param_3,param_4)
    n = [2,7,4,1,8,1]
    print(s.lastStoneWeight(n))