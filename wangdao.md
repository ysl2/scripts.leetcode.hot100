# wangdao

## 第1章 绪论

### P5-正文1 斐波那契递归

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

### P5-正文 逆序查找

```python
class Solution:
    def reverseFind(self, nums: list, k: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == k:
                return i
        return -1
```

### P7-正文1 循环乘二

```python
class Solution:
    def doubleUntil(self, n: int) -> int:
        i = 1
        while i <= n:
            i *= 2
        return i
```

### P7-正文2 立方循环

```python
class Solution:
    def cubeCount(self, n: int) -> int:
        i = 0
        while i ** 3 <= n:
            i += 1
        return i
```

### P7-正文3 冒泡一趟比较

```python
class Solution:
    def bubbleLike(self, nums: list) -> list:
        for i in range(len(nums) - 1, 1, -1):
            for j in range(1, i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
```

### P7-正文4 递归阶乘

```python
class Solution:
    def fact(self, n: int) -> int:
        if n <= 1:
            return 1
        return n * self.fact(n - 1)
```

### P8-正文1 双重循环计数

```python
class Solution:
    def countLoop(self, n: int) -> int:
        cnt = 0
        k = 1
        while k <= n:
            for _ in range(n):
                cnt += 1
            k *= 2
        return cnt
```

### P8-正文2 累加到n

```python
class Solution:
    def addUntil(self, n: int) -> int:
        i = s = 0
        while s < n:
            i += 1
            s += i
        return i
```

### P8-正文3 求平方根下界

```python
class Solution:
    def sqrtFloor(self, n: int) -> int:
        x = 0
        while (x + 1) * (x + 1) <= n:
            x += 1
        return x
```

### P8-正文4 递增循环计数

```python
class Solution:
    def increasingCount(self, n: int) -> int:
        cnt = 0
        i = 1
        while i < n:
            cnt += i
            i *= 2
        return cnt
```

### P12-思维拓展 斐波那契迭代

```python
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
```

## 第2章 线性表

### P15-正文 顺序表存储约定

```python
class Solution:
    def makeSqList(self, max_size: int = 50) -> list:
        return []
```

### P16-正文1 顺序表初始化

```python
class Solution:
    def initList(self) -> list:
        return []
```

### P16-正文 动态顺序表初始化

```python
class Solution:
    def initSeqList(self, init_size: int = 100) -> list:
        return []
```

### P17-正文2 顺序表插入

```python
class Solution:
    def listInsert(self, nums: list, i: int, x: int) -> bool:
        if i < 0 or i > len(nums):
            return False
        nums.insert(i, x)
        return True
```

### P17-正文3 顺序表删除

```python
class Solution:
    def listDelete(self, nums: list, i: int):
        if i < 0 or i >= len(nums):
            return None
        return nums.pop(i)
```

### P18-正文4 顺序表按值查找

```python
class Solution:
    def locateElem(self, nums: list, x) -> int:
        for i, v in enumerate(nums):
            if v == x:
                return i
        return -1
```

### P22-T1 删除最小元素并用最后元素填补

```python
class Solution:
    def deleteMin(self, nums: list):
        if not nums:
            return None
        k = min(range(len(nums)), key=lambda i: nums[i])
        ans = nums[k]
        nums[k] = nums[-1]
        nums.pop()
        return ans
```

### P22-T2 逆置顺序表

```python
class Solution:
    def reverseList(self, nums: list) -> None:
        nums.reverse()
```

### P23-T3 删除有序表中所有x

```python
class Solution:
    def deleteX(self, nums: list, x: int) -> list:
        return [v for v in nums if v != x]
```

### P23-T4 删除有序表中s到t的元素

```python
class Solution:
    def deleteRange(self, nums: list, s: int, t: int) -> list:
        return [v for v in nums if not (s <= v <= t)]
```

### P23-T5 删除无序表中s到t的元素

```python
class Solution:
    def deleteRange(self, nums: list, s: int, t: int) -> list:
        return [v for v in nums if not (s <= v <= t)]
```

### P24-T6 删除有序表重复元素

```python
class Solution:
    def uniqueSorted(self, nums: list) -> list:
        res = []
        for x in nums:
            if not res or res[-1] != x:
                res.append(x)
        return res
```

### P25-T7 合并两个有序顺序表

```python
class Solution:
    def merge(self, a: list, b: list) -> list:
        i = j = 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        return res + a[i:] + b[j:]
```

### P25-T8 交换数组中两个线性表

```python
class Solution:
    def exchange(self, nums: list, m: int, n: int) -> list:
        nums[:] = nums[m:m + n] + nums[:m]
        return nums
```

### P26-T9 有序表查找并插入

```python
class Solution:
    def searchExchangeInsert(self, nums: list, x: int) -> list:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == x:
                if mid + 1 < len(nums):
                    nums[mid], nums[mid + 1] = nums[mid + 1], nums[mid]
                return nums
            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        nums.insert(left, x)
        return nums
```

### P26-T9 三个递增数组的公共元素

```python
class Solution:
    def commonOfThree(self, a: list, b: list, c: list) -> list:
        i = j = k = 0
        res = []
        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k]:
                res.append(a[i])
                i += 1
                j += 1
                k += 1
            else:
                m = max(a[i], b[j], c[k])
                if a[i] < m:
                    i += 1
                if b[j] < m:
                    j += 1
                if c[k] < m:
                    k += 1
        return res
```

### P27-T10 数组左循环移动p位

```python
class Solution:
    def rotateLeft(self, nums: list, p: int) -> list:
        p %= len(nums)
        nums[:] = nums[p:] + nums[:p]
        return nums
```

### P28-T11 两个等长升序序列的中位数

```python
class Solution:
    def medianOfTwoSorted(self, a: list, b: list):
        c = sorted(a + b)
        return c[(len(c) - 1) // 2]
```

### P29-T12 找主元素

```python
class Solution:
    def majorityElement(self, nums: list) -> int:
        cand, cnt = None, 0
        for x in nums:
            if cnt == 0:
                cand = x
            cnt += 1 if x == cand else -1
        return cand if nums.count(cand) > len(nums) // 2 else -1
```

### P30-T13 最小未出现正整数

```python
class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        s = set(nums)
        x = 1
        while x in s:
            x += 1
        return x
```

### P30-T14 三元组最小距离

```python
class Solution:
    def minDistance(self, a: list, b: list, c: list) -> int:
        i = j = k = 0
        res = float('inf')
        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]
            res = min(res, max(x, y, z) - min(x, y, z))
            if x == min(x, y, z):
                i += 1
            elif y == min(x, y, z):
                j += 1
            else:
                k += 1
        return res
```

### P30-T15 后缀最大最小乘积

```python
class Solution:
    def suffixProductMax(self, nums: list) -> list:
        res = [0] * len(nums)
        mx = mn = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])
            res[i] = nums[i] * (mx if nums[i] >= 0 else mn)
        return res
```

### P31-正文1 单链表初始化

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def initList(self):
        return None
```

### P32-正文2 求单链表表长

```python
class Solution:
    def length(self, head) -> int:
        res = 0
        while head:
            res += 1
            head = head.next
        return res
```

### P32-正文3 单链表按序号查找

```python
class Solution:
    def getElem(self, head, i: int):
        while head and i > 0:
            head = head.next
            i -= 1
        return head
```

### P32-正文4 单链表按值查找

```python
class Solution:
    def locateElem(self, head, x):
        while head and head.val != x:
            head = head.next
        return head
```

### P33-正文5 单链表插入结点

```python
class Solution:
    def insertAfter(self, p, x) -> bool:
        if not p:
            return False
        p.next = ListNode(x, p.next)
        return True
```

### P34-正文6 单链表删除结点

```python
class Solution:
    def deleteAfter(self, p):
        if not p or not p.next:
            return None
        x = p.next
        p.next = x.next
        return x.val
```

### P35-正文7 头插法建立单链表

```python
class Solution:
    def buildByHeadInsert(self, nums: list):
        head = None
        for x in nums:
            head = ListNode(x, head)
        return head
```

### P36-正文8 尾插法建立单链表

```python
class Solution:
    def buildByTailInsert(self, nums: list):
        dummy = p = ListNode()
        for x in nums:
            p.next = ListNode(x)
            p = p.next
        return dummy.next
```

### P36-正文9 双链表插入

```python
# Definition for doubly-linked list.
# class DNode:
#     def __init__(self, val=0, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next

class Solution:
    def insertAfter(self, p, x) -> bool:
        node = DNode(x, p, p.next)
        if p.next:
            p.next.prev = node
        p.next = node
        return True
```

### P37-正文10 双链表删除

```python
class Solution:
    def delete(self, p) -> bool:
        if not p:
            return False
        if p.prev:
            p.prev.next = p.next
        if p.next:
            p.next.prev = p.prev
        return True
```

### P38-正文 静态链表约定

```python
class Solution:
    def initStaticList(self, n: int) -> list:
        return [{'data': None, 'next': -1} for _ in range(n)]
```

### P50-T1 递归删除单链表中所有x

```python
class Solution:
    def deleteX(self, head, x):
        if not head:
            return None
        head.next = self.deleteX(head.next, x)
        return head.next if head.val == x else head
```

### P50-T2 带头结点删除所有x

```python
class Solution:
    def deleteX(self, head, x):
        dummy = ListNode(0, head)
        p = dummy
        while p.next:
            if p.next.val == x:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
```

### P51-T3 逆序输出单链表

```python
class Solution:
    def reversePrint(self, head) -> list:
        return self.reversePrint(head.next) + [head.val] if head else []
```

### P52-T4 删除最小值结点

```python
class Solution:
    def deleteMin(self, head):
        dummy = ListNode(0, head)
        pre = dummy
        p = dummy
        while p.next:
            if p.next.val < pre.next.val:
                pre = p
            p = p.next
        if pre.next:
            pre.next = pre.next.next
        return dummy.next
```

### P52-T5 单链表就地逆置

```python
class Solution:
    def reverseList(self, head):
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
```

### P53-T6 单链表递增排序

```python
class Solution:
    def sortList(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        dummy = p = ListNode()
        for x in sorted(vals):
            p.next = ListNode(x)
            p = p.next
        return dummy.next
```

### P53-T7 删除区间内结点

```python
class Solution:
    def deleteRange(self, head, s, t):
        dummy = ListNode(0, head)
        p = dummy
        while p.next:
            if s < p.next.val < t:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
```

### P54-T8 两个有序链表公共元素

```python
class Solution:
    def commonList(self, a, b):
        dummy = p = ListNode()
        while a and b:
            if a.val == b.val:
                p.next = ListNode(a.val)
                p = p.next
                a = a.next
                b = b.next
            elif a.val < b.val:
                a = a.next
            else:
                b = b.next
        return dummy.next
```

### P55-T9 合并两个递增链表为递减链表

```python
class Solution:
    def mergeDesc(self, a, b):
        head = None
        while a or b:
            if not b or (a and a.val <= b.val):
                x, a = a, a.next
            else:
                x, b = b, b.next
            x.next = head
            head = x
        return head
```

### P55-T10 拆分奇偶位置链表

```python
class Solution:
    def splitOddEven(self, head):
        a = pa = ListNode()
        b = pb = ListNode()
        i = 1
        while head:
            if i % 2:
                pa.next = head
                pa = pa.next
            else:
                pb.next = head
                pb = pb.next
            head = head.next
            i += 1
        pa.next = pb.next = None
        return a.next, b.next
```

### P56-T11 判断链表是否对称

```python
class Solution:
    def isPalindrome(self, head) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
```

### P56-T12 连接两个循环链表

```python
class Solution:
    def concatCycle(self, ha, hb):
        if not ha:
            return hb
        if not hb:
            return ha
        pa, pb = ha, hb
        while pa.next is not ha:
            pa = pa.next
        while pb.next is not hb:
            pb = pb.next
        pa.next = hb
        pb.next = ha
        return ha
```

### P57-T13 有序链表去重

```python
class Solution:
    def deleteDuplicates(self, head):
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
```

### P57-T15 循环右移链表k位

```python
class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next:
            return head
        n, tail = 1, head
        while tail.next:
            n += 1
            tail = tail.next
        k %= n
        if k == 0:
            return head
        tail.next = head
        for _ in range(n - k):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head
```

### P58-T14 找环入口

```python
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
```

### P58-T16 链表孪生和最大值

```python
class Solution:
    def pairSum(self, head) -> int:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return max(vals[i] + vals[-1 - i] for i in range(len(vals) // 2))
```

### P59-T15 删除绝对值重复结点

```python
class Solution:
    def deleteAbsDuplicate(self, head):
        seen = set()
        dummy = ListNode(0, head)
        p = dummy
        while p.next:
            x = abs(p.next.val)
            if x in seen:
                p.next = p.next.next
            else:
                seen.add(x)
                p = p.next
        return dummy.next
```

### P59-T17 查找倒数第k个结点

```python
class Solution:
    def kthFromEnd(self, head, k: int):
        fast = slow = head
        for _ in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
```

### P60-T16 链表重排

```python
class Solution:
    def reorderList(self, head):
        vals = []
        while head:
            vals.append(head)
            head = head.next
        i, j = 0, len(vals) - 1
        dummy = p = ListNode()
        while i <= j:
            p.next = vals[i]
            p = p.next
            i += 1
            if i <= j:
                p.next = vals[j]
                p = p.next
                j -= 1
        p.next = None
        return dummy.next
```

### P60-T18 查找两个链表的公共后缀起点

```python
class Solution:
    def getIntersectionNode(self, a, b):
        p, q = a, b
        while p is not q:
            p = p.next if p else b
            q = q.next if q else a
        return p
```

### P62-思维拓展 有序数组两数和

```python
class Solution:
    def twoSumSorted(self, nums: list, target: int) -> list:
        i, j = 0, len(nums) - 1
        res = []
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif s < target:
                i += 1
            else:
                j -= 1
        return res
```

## 第3章 栈、队列和数组

### P64-正文1 顺序栈基本操作

```python
class Stack(list):
    def push(self, x):
        self.append(x)

    def pop(self):
        return super().pop() if self else None

    def top(self):
        return self[-1] if self else None
```

### P66-正文2 共享栈

```python
class SharedStack:
    def __init__(self, n: int):
        self.a = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.top1 + 1 == self.top2:
            return False
        self.top1 += 1
        self.a[self.top1] = x
        return True

    def push2(self, x):
        if self.top1 + 1 == self.top2:
            return False
        self.top2 -= 1
        self.a[self.top2] = x
        return True
```

### P74-T1 判断I/O序列是否合法

```python
class Solution:
    def judgeIO(self, ops: str) -> bool:
        cnt = 0
        for c in ops:
            if c == 'I':
                cnt += 1
            elif c == 'O':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0
```

### P74-T2 链表前半入栈判回文

```python
class Solution:
    def linkedPalindrome(self, head) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
```

### P75-T3 共享栈完整操作

```python
class SharedStack:
    def __init__(self, n: int):
        self.a = [None] * n
        self.top = [-1, n]

    def push(self, i: int, x) -> bool:
        if self.top[0] + 1 == self.top[1]:
            return False
        if i == 0:
            self.top[0] += 1
            self.a[self.top[0]] = x
        else:
            self.top[1] -= 1
            self.a[self.top[1]] = x
        return True

    def pop(self, i: int):
        if i == 0:
            if self.top[0] == -1:
                return None
            x = self.a[self.top[0]]
            self.top[0] -= 1
            return x
        if self.top[1] == len(self.a):
            return None
        x = self.a[self.top[1]]
        self.top[1] += 1
        return x
```

### P77-正文3 循环队列

```python
class CircularQueue:
    def __init__(self, k: int):
        self.a = [None] * (k + 1)
        self.front = self.rear = 0

    def empty(self):
        return self.front == self.rear

    def full(self):
        return (self.rear + 1) % len(self.a) == self.front

    def push(self, x):
        if self.full():
            return False
        self.a[self.rear] = x
        self.rear = (self.rear + 1) % len(self.a)
        return True

    def pop(self):
        if self.empty():
            return None
        x = self.a[self.front]
        self.front = (self.front + 1) % len(self.a)
        return x
```

### P79-正文4 链式队列

```python
from collections import deque

class LinkQueue(deque):
    def enqueue(self, x):
        self.append(x)

    def dequeue(self):
        return self.popleft() if self else None
```

### P85-T1 用栈判断输入输出序列是否合法

```python
class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        st = []
        j = 0
        for x in pushed:
            st.append(x)
            while st and j < len(popped) and st[-1] == popped[j]:
                st.pop()
                j += 1
        return not st
```

### P86-T2 两个栈模拟队列

```python
class MyQueue:
    def __init__(self):
        self.a, self.b = [], []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop() if self.b else None
```

### P87-T3 队列逆置

```python
class Solution:
    def reverseQueue(self, q):
        st = []
        while q:
            st.append(q.popleft())
        while st:
            q.append(st.pop())
        return q
```

### P87-T1 带tag循环队列入队出队

```python
class TagQueue:
    def __init__(self, n: int):
        self.a = [None] * n
        self.front = self.rear = self.tag = 0

    def enqueue(self, x) -> bool:
        if self.front == self.rear and self.tag == 1:
            return False
        self.a[self.rear] = x
        self.rear = (self.rear + 1) % len(self.a)
        self.tag = 1
        return True

    def dequeue(self):
        if self.front == self.rear and self.tag == 0:
            return None
        x = self.a[self.front]
        self.front = (self.front + 1) % len(self.a)
        self.tag = 0
        return x
```

### P88-T2 队列逆置

```python
class Solution:
    def reverseQueue(self, q):
        st = []
        while q:
            st.append(q.popleft())
        while st:
            q.append(st.pop())
        return q
```

### P88-T3 两个栈实现队列

```python
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x) -> None:
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

    def empty(self) -> bool:
        return not self.s1 and not self.s2
```

### P90-正文5 括号匹配

```python
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in mp:
                if not st or st.pop() != mp[c]:
                    return False
            else:
                st.append(c)
        return not st
```

### P91-正文6 中缀转后缀

```python
class Solution:
    def infixToPostfix(self, tokens: list) -> list:
        pri = {'+': 1, '-': 1, '*': 2, '/': 2}
        st, res = [], []
        for x in tokens:
            if x not in pri and x not in '()':
                res.append(x)
            elif x == '(':
                st.append(x)
            elif x == ')':
                while st[-1] != '(':
                    res.append(st.pop())
                st.pop()
            else:
                while st and st[-1] != '(' and pri[st[-1]] >= pri[x]:
                    res.append(st.pop())
                st.append(x)
        return res + st[::-1]
```

### P92-正文7 后缀表达式求值

```python
class Solution:
    def evalPostfix(self, tokens: list) -> int:
        st = []
        for x in tokens:
            if x not in '+-*/':
                st.append(int(x))
            else:
                b, a = st.pop(), st.pop()
                if x == '+': st.append(a + b)
                if x == '-': st.append(a - b)
                if x == '*': st.append(a * b)
                if x == '/': st.append(int(a / b))
        return st[-1]
```

### P93-正文8 递归斐波那契

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

### P94-正文9 队列层次遍历

```python
from collections import deque

class Solution:
    def levelOrder(self, root) -> list:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
```

### P99-T1 循环队列tag判空判满

```python
class TagQueue:
    def __init__(self, k: int):
        self.a = [None] * k
        self.front = self.rear = self.tag = 0

    def empty(self):
        return self.front == self.rear and self.tag == 0

    def full(self):
        return self.front == self.rear and self.tag == 1
```

### P100-T2 栈和队列判断回文

```python
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = list(s)
        q = deque(s)
        while st:
            if st.pop() != q.popleft():
                return False
        return True
```

### P100-T1 括号匹配

```python
class Solution:
    def bracketsCheck(self, s: str) -> bool:
        st = []
        mp = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                st.append(c)
            elif c in mp and (not st or st.pop() != mp[c]):
                return False
        return not st
```

### P101-正文10 对称矩阵下标映射

```python
class Solution:
    def symmetricIndex(self, i: int, j: int) -> int:
        if i < j:
            i, j = j, i
        return i * (i + 1) // 2 + j
```

### P102-正文11 三角矩阵下标映射

```python
class Solution:
    def lowerTriIndex(self, i: int, j: int, n: int) -> int:
        return i * (i + 1) // 2 + j if i >= j else n * (n + 1) // 2
```

### P103-正文12 三对角矩阵下标映射

```python
class Solution:
    def triDiagonalIndex(self, i: int, j: int) -> int:
        return 2 * i + j if abs(i - j) <= 1 else -1
```

### P107-T1 括号匹配算法

```python
class Solution:
    def match(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            elif c == ')':
                if not st:
                    return False
                st.pop()
        return not st
```

### P108-T2 火车调度

```python
class Solution:
    def trainArrange(self, order: list, target: list) -> bool:
        st = []
        j = 0
        for x in order:
            st.append(x)
            while st and j < len(target) and st[-1] == target[j]:
                st.pop()
                j += 1
        return j == len(target)
```

## 第4章 串

### P111-正文1 简单模式匹配

```python
class Solution:
    def index(self, s: str, p: str) -> int:
        for i in range(len(s) - len(p) + 1):
            if s[i:i + len(p)] == p:
                return i
        return -1
```

### P116-正文2 求next数组

```python
class Solution:
    def getNext(self, p: str) -> list:
        nxt = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j and p[i] != p[j]:
                j = nxt[j - 1]
            if p[i] == p[j]:
                j += 1
            nxt[i] = j
        return nxt
```

### P117-正文3 KMP匹配

```python
class Solution:
    def kmp(self, s: str, p: str) -> int:
        if not p:
            return 0
        nxt = self.getNext(p)
        j = 0
        for i, c in enumerate(s):
            while j and c != p[j]:
                j = nxt[j - 1]
            if c == p[j]:
                j += 1
            if j == len(p):
                return i - j + 1
        return -1

    def getNext(self, p: str) -> list:
        nxt = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j and p[i] != p[j]:
                j = nxt[j - 1]
            if p[i] == p[j]:
                j += 1
            nxt[i] = j
        return nxt
```

### P118-正文4 求nextval数组

```python
class Solution:
    def getNextVal(self, p: str) -> list:
        nxt = self.getNext(p)
        val = nxt[:]
        for i in range(1, len(p)):
            if val[i] and p[i] == p[val[i] - 1]:
                val[i] = val[val[i] - 1]
        return val

    def getNext(self, p: str) -> list:
        nxt = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j and p[i] != p[j]:
                j = nxt[j - 1]
            if p[i] == p[j]:
                j += 1
            nxt[i] = j
        return nxt
```

### P119-T1 判断主串模式串字符集关系

```python
class Solution:
    def isSubAlphabet(self, s: str, p: str) -> bool:
        return set(p) <= set(s)
```

### P120-T2 KMP求指定模式位置

```python
class Solution:
    def find(self, s: str, p: str) -> int:
        return s.find(p)
```

## 第5章 树与二叉树

### P139-T1 顺序存储二叉树最近公共祖先

```python
class Solution:
    def commonAncestor(self, tree: list, i: int, j: int):
        while i != j:
            if i > j:
                i //= 2
            else:
                j //= 2
        return tree[i] if 0 <= i < len(tree) else None
```

### P141-正文1 二叉树先序遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root) -> list:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

### P141-正文2 二叉树中序遍历

```python
class Solution:
    def inorderTraversal(self, root) -> list:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

### P141-正文3 二叉树后序遍历

```python
class Solution:
    def postorderTraversal(self, root) -> list:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

### P142-正文4 二叉树非递归中序遍历

```python
class Solution:
    def inorderTraversal(self, root) -> list:
        st, res = [], []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right
        return res
```

### P142-正文5 二叉树层序遍历

```python
from collections import deque

class Solution:
    def levelOrder(self, root) -> list:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
```

### P145-正文 中序线索化

```python
class Solution:
    def inorderThread(self, root):
        pre = None
        def dfs(node):
            nonlocal pre
            if not node:
                return
            dfs(node.left)
            if not node.left:
                node.left = pre
                node.ltag = 1
            if pre and not pre.right:
                pre.right = node
                pre.rtag = 1
            pre = node
            dfs(node.right)
        dfs(root)
        return root
```

### P146-正文 线索二叉树中序遍历

```python
class Solution:
    def threadedInorder(self, root) -> list:
        res = []
        def leftmost(node):
            while node and getattr(node, 'ltag', 0) == 0 and node.left:
                node = node.left
            return node
        p = leftmost(root)
        while p:
            res.append(p.val)
            p = leftmost(p.right) if getattr(p, 'rtag', 0) == 0 else p.right
        return res
```

### P158-T1 统计二叉树叶子结点

```python
class Solution:
    def countLeaves(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.countLeaves(root.left) + self.countLeaves(root.right)
```

### P158-T1 二叉树高度层序算法

```python
from collections import deque

class Solution:
    def heightByLevel(self, root) -> int:
        if not root:
            return 0
        q = deque([root])
        h = 0
        while q:
            h += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return h
```

### P159-T2 求二叉树高度

```python
class Solution:
    def height(self, root) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
```

### P159-T2 判断完全二叉树

```python
from collections import deque

class Solution:
    def isCompleteTree(self, root) -> bool:
        q = deque([root])
        seen_none = False
        while q:
            node = q.popleft()
            if not node:
                seen_none = True
            else:
                if seen_none:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
```

### P160-T3 统计度为2的结点

```python
class Solution:
    def countDegreeTwo(self, root) -> int:
        if not root:
            return 0
        cur = 1 if root.left and root.right else 0
        return cur + self.countDegreeTwo(root.left) + self.countDegreeTwo(root.right)
```

### P160-T4 二叉树左右交换

```python
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

### P160-T7 求先序第k个结点

```python
class Solution:
    def kthPreorder(self, root, k: int):
        arr = self.preorder(root)
        return arr[k - 1] if 1 <= k <= len(arr) else None

    def preorder(self, root):
        return [] if not root else [root] + self.preorder(root.left) + self.preorder(root.right)
```

### P160-T3 统计双分支结点

```python
class Solution:
    def countTwoChildren(self, root) -> int:
        if not root:
            return 0
        return int(root.left is not None and root.right is not None) + self.countTwoChildren(root.left) + self.countTwoChildren(root.right)
```

### P160-T4 交换二叉树左右子树

```python
class Solution:
    def swapChildren(self, root):
        if root:
            root.left, root.right = self.swapChildren(root.right), self.swapChildren(root.left)
        return root
```

### P160-T5 先序第k个结点

```python
class Solution:
    def preorderKth(self, root, k: int):
        arr = []
        def dfs(node):
            if node:
                arr.append(node)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return arr[k - 1] if 1 <= k <= len(arr) else None
```

### P161-T8 删除以x为根的子树

```python
class Solution:
    def deleteSubtree(self, root, x):
        if not root:
            return None
        if root.val == x:
            return None
        root.left = self.deleteSubtree(root.left, x)
        root.right = self.deleteSubtree(root.right, x)
        return root
```

### P161-T6 删除以x为根的子树

```python
class Solution:
    def deleteXTree(self, root, x):
        if not root or root.val == x:
            return None
        root.left = self.deleteXTree(root.left, x)
        root.right = self.deleteXTree(root.right, x)
        return root
```

### P162-T6 非递归后序遍历

```python
class Solution:
    def postorderTraversal(self, root) -> list:
        st, res = [root], []
        while st:
            node = st.pop()
            if node:
                res.append(node.val)
                st.append(node.left)
                st.append(node.right)
        return res[::-1]
```

### P162-T9 打印x结点的所有祖先

```python
class Solution:
    def ancestors(self, root, x) -> list:
        path = []
        def dfs(node):
            if not node:
                return False
            if node.val == x or dfs(node.left) or dfs(node.right):
                path.append(node.val)
                return True
            return False
        dfs(root)
        return path[1:]
```

### P162-T10 最近公共祖先

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
```

### P162-T7 查找结点祖先

```python
class Solution:
    def ancestors(self, root, x) -> list:
        path = []
        def dfs(node):
            if not node:
                return False
            if node.val == x or dfs(node.left) or dfs(node.right):
                path.append(node.val)
                return True
            return False
        dfs(root)
        return path[1:]
```

### P162-T8 二叉树最近公共祖先

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
```

### P163-T11 求二叉树宽度

```python
from collections import deque

class Solution:
    def width(self, root) -> int:
        if not root:
            return 0
        q = deque([root])
        res = 0
        while q:
            res = max(res, len(q))
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
```

### P163-T9 二叉树最大宽度

```python
from collections import deque

class Solution:
    def widthOfTree(self, root) -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 0
        while q:
            ans = max(ans, len(q))
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
```

### P164-T12 先序中序构造二叉树

```python
class Solution:
    def buildTree(self, preorder: list, inorder: list):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root
```

### P164-T10 满二叉树先序转后序

```python
class Solution:
    def preToPost(self, pre: list) -> list:
        if not pre:
            return []
        half = (len(pre) - 1) // 2
        return self.preToPost(pre[1:1 + half]) + self.preToPost(pre[1 + half:]) + [pre[0]]
```

### P165-T5 判断两棵二叉树相似

```python
class Solution:
    def isSimilar(self, a, b) -> bool:
        if not a or not b:
            return a is b
        return self.isSimilar(a.left, b.left) and self.isSimilar(a.right, b.right)
```

### P165-T11 叶结点连成单链表

```python
class Solution:
    def leavesList(self, root) -> list:
        if not root:
            return []
        if not root.left and not root.right:
            return [root]
        return self.leavesList(root.left) + self.leavesList(root.right)
```

### P165-T12 判断两棵树相似

```python
class Solution:
    def similar(self, a, b) -> bool:
        if not a or not b:
            return a is b
        return self.similar(a.left, b.left) and self.similar(a.right, b.right)
```

### P166-T13 哈夫曼树WPL递归

```python
class Solution:
    def wpl(self, root, depth: int = 0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.weight * depth
        return self.wpl(root.left, depth + 1) + self.wpl(root.right, depth + 1)
```

### P166-T1 哈夫曼树带权路径长度

```python
from heapq import heapify, heappop, heappush

class Solution:
    def huffmanWPL(self, weights: list) -> int:
        heapify(weights)
        res = 0
        while len(weights) > 1:
            x = heappop(weights) + heappop(weights)
            res += x
            heappush(weights, x)
        return res
```

### P167-T14 表达式树转中缀式

```python
class Solution:
    def expression(self, root) -> str:
        if not root:
            return ''
        if not root.left and not root.right:
            return str(root.val)
        return '(' + self.expression(root.left) + str(root.val) + self.expression(root.right) + ')'
```

### P167-T15 顺序存储判断BST

```python
class Solution:
    def isBSTArray(self, tree: list) -> bool:
        vals = []
        def dfs(i):
            if i >= len(tree) or tree[i] is None:
                return
            dfs(2 * i + 1)
            vals.append(tree[i])
            dfs(2 * i + 2)
        dfs(0)
        return all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
```

### P168-T1 树的双亲表示找孩子

```python
class Solution:
    def children(self, parent: list, x: int) -> list:
        return [i for i, p in enumerate(parent) if p == x]
```

### P180-T2 孩子兄弟表示求树高度

```python
class Solution:
    def height(self, root) -> int:
        if not root:
            return 0
        return max(self.height(root.left) + 1, self.height(root.right))
```

### P180-T1 孩子兄弟树叶子数

```python
class Solution:
    def csLeaves(self, root) -> int:
        if not root:
            return 0
        return (1 if not root.firstchild else self.csLeaves(root.firstchild)) + self.csLeaves(root.nextsibling)
```

### P180-T2 孩子兄弟树高度

```python
class Solution:
    def csHeight(self, root) -> int:
        if not root:
            return 0
        return max(self.csHeight(root.firstchild) + 1, self.csHeight(root.nextsibling))
```

### P184-正文 并查集初始化

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n
```

### P184-正文 并查集查找

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n

    def find(self, x: int) -> int:
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x
```

### P184-正文 并查集合并

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra

    def find(self, x: int) -> int:
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x
```

### P184-T2 并查集查找

```python
class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))

    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int) -> None:
        self.fa[self.find(x)] = self.find(y)
```

### P185-正文 路径压缩查找

```python
class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))

    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
```

## 第6章 图

### P202-正文1 邻接矩阵建图

```python
class Solution:
    def buildMatrix(self, n: int, edges: list, directed=False) -> list:
        g = [[0] * n for _ in range(n)]
        for u, v in edges:
            g[u][v] = 1
            if not directed:
                g[v][u] = 1
        return g
```

### P204-正文2 邻接表建图

```python
from collections import defaultdict

class Solution:
    def buildGraph(self, edges: list, directed=False) -> dict:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            if not directed:
                g[v].append(u)
        return g
```

### P213-T1 邻接表转邻接矩阵

```python
class Solution:
    def listToMatrix(self, g: list) -> list:
        n = len(g)
        mat = [[0] * n for _ in range(n)]
        for u in range(n):
            for v in g[u]:
                mat[u][v] = 1
        return mat
```

### P213-T2 判断无向图是否存在欧拉路径

```python
class Solution:
    def hasEulerPath(self, g: list) -> bool:
        odd = sum(len(adj) % 2 for adj in g)
        return odd in (0, 2)
```

### P214-T3 输出出度大于入度的顶点

```python
class Solution:
    def outGreaterThanIn(self, mat: list) -> list:
        n = len(mat)
        return [i for i in range(n) if sum(mat[i]) > sum(mat[j][i] for j in range(n))]
```

### P214-T1 求各顶点入度

```python
class Solution:
    def indegrees(self, n: int, edges: list) -> list:
        res = [0] * n
        for _, v in edges:
            res[v] += 1
        return res
```

### P215-正文3 广度优先搜索

```python
from collections import deque

class Solution:
    def bfs(self, g: list, s: int) -> list:
        vis = [False] * len(g)
        q = deque([s])
        vis[s] = True
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
        return res
```

### P216-正文 BFS求单源最短距离

```python
from collections import deque

class Solution:
    def bfsDistance(self, g: list, s: int) -> list:
        dist = [-1] * len(g)
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
```

### P217-正文4 深度优先搜索

```python
class Solution:
    def dfs(self, g: list, s: int) -> list:
        vis = [False] * len(g)
        res = []
        def f(u):
            vis[u] = True
            res.append(u)
            for v in g[u]:
                if not vis[v]:
                    f(v)
        f(s)
        return res
```

### P224-T1 判断无向图连通

```python
class Solution:
    def isConnected(self, g: list) -> bool:
        seen = set()
        def dfs(u):
            seen.add(u)
            for v in g[u]:
                if v not in seen:
                    dfs(v)
        dfs(0)
        return len(seen) == len(g)
```

### P224-T2 求图的连通分量数

```python
class Solution:
    def components(self, g: list) -> int:
        vis = [False] * len(g)
        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
        res = 0
        for i in range(len(g)):
            if not vis[i]:
                res += 1
                dfs(i)
        return res
```

### P224-T3 判断顶点u到v是否有路径

```python
class Solution:
    def hasPath(self, g: list, s: int, t: int) -> bool:
        seen = set()
        def dfs(u):
            if u == t:
                return True
            seen.add(u)
            return any(v not in seen and dfs(v) for v in g[u])
        return dfs(s)
```

### P224-T1 判断无向图是否为树

```python
class Solution:
    def isTree(self, g: list) -> bool:
        n = len(g)
        seen = set()
        def dfs(u, fa):
            seen.add(u)
            for v in g[u]:
                if v == fa:
                    continue
                if v in seen or not dfs(v, u):
                    return False
            return True
        return n == 0 or (dfs(0, -1) and len(seen) == n)
```

### P224-T2 DFS判断i到j有路径

```python
class Solution:
    def dfsReach(self, g: list, s: int, t: int) -> bool:
        seen = set()
        def dfs(u):
            if u == t:
                return True
            seen.add(u)
            return any(v not in seen and dfs(v) for v in g[u])
        return dfs(s)
```

### P225-T3 BFS判断i到j有路径

```python
from collections import deque

class Solution:
    def bfsReach(self, g: list, s: int, t: int) -> bool:
        q = deque([s])
        seen = {s}
        while q:
            u = q.popleft()
            if u == t:
                return True
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return False
```

### P225-T4 输出u到v的简单路径

```python
class Solution:
    def allPaths(self, g: list, s: int, t: int) -> list:
        res = []
        def dfs(u, path):
            if u == t:
                res.append(path[:])
                return
            for v in g[u]:
                if v not in path:
                    dfs(v, path + [v])
        dfs(s, [s])
        return res
```

### P225-T2 输出u到v所有简单路径

```python
class Solution:
    def allPaths(self, g: list, s: int, t: int) -> list:
        res = []
        def dfs(u, path):
            if u == t:
                res.append(path[:])
                return
            for v in g[u]:
                if v not in path:
                    dfs(v, path + [v])
        dfs(s, [s])
        return res
```

### P226-正文 通用最小生成树框架

```python
class Solution:
    def mstBySortedEdges(self, n: int, edges: list) -> list:
        fa = list(range(n))
        def find(x):
            while fa[x] != x:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x
        tree = []
        for u, v, w in sorted(edges, key=lambda e: e[2]):
            ru, rv = find(u), find(v)
            if ru != rv:
                fa[ru] = rv
                tree.append((u, v, w))
        return tree
```

### P227-正文5 Prim最小生成树

```python
class Solution:
    def prim(self, w: list) -> int:
        n = len(w)
        low = [float('inf')] * n
        low[0] = 0
        vis = [False] * n
        res = 0
        for _ in range(n):
            u = min((i for i in range(n) if not vis[i]), key=lambda i: low[i])
            vis[u] = True
            res += low[u]
            for v in range(n):
                if not vis[v] and w[u][v] < low[v]:
                    low[v] = w[u][v]
        return res
```

### P228-正文6 Kruskal最小生成树

```python
class Solution:
    def kruskal(self, n: int, edges: list) -> int:
        fa = list(range(n))
        def find(x):
            while fa[x] != x:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x
        res = cnt = 0
        for u, v, w in sorted(edges, key=lambda e: e[2]):
            fu, fv = find(u), find(v)
            if fu != fv:
                fa[fu] = fv
                res += w
                cnt += 1
        return res if cnt == n - 1 else -1
```

### P229-正文7 Dijkstra最短路径

```python
class Solution:
    def dijkstra(self, w: list, s: int) -> list:
        n = len(w)
        dist = w[s][:]
        dist[s] = 0
        vis = [False] * n
        for _ in range(n):
            u = min((i for i in range(n) if not vis[i]), key=lambda i: dist[i])
            vis[u] = True
            for v in range(n):
                dist[v] = min(dist[v], dist[u] + w[u][v])
        return dist
```

### P231-正文8 Floyd最短路径

```python
class Solution:
    def floyd(self, dist: list) -> list:
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
```

### P233-正文9 拓扑排序

```python
from collections import deque

class Solution:
    def topoSort(self, n: int, edges: list) -> list:
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1
        q = deque(i for i in range(n) if indeg[i] == 0)
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return res if len(res) == n else []
```

### P236-正文10 关键路径

```python
from collections import deque

class Solution:
    def criticalPath(self, n: int, edges: list) -> list:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))
            indeg[v] += 1
        q = deque(i for i in range(n) if indeg[i] == 0)
        topo, ve = [], [0] * n
        while q:
            u = q.popleft()
            topo.append(u)
            for v, w in g[u]:
                ve[v] = max(ve[v], ve[u] + w)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        vl = [max(ve)] * n
        for u in topo[::-1]:
            for v, w in g[u]:
                vl[u] = min(vl[u], vl[v] - w)
        return [(u, v) for u, v, w in edges if ve[u] == vl[v] - w]
```

### P249-T3 判断图是否有环

```python
class Solution:
    def hasCycleDirected(self, g: list) -> bool:
        color = [0] * len(g)
        def dfs(u):
            color[u] = 1
            for v in g[u]:
                if color[v] == 1 or (color[v] == 0 and dfs(v)):
                    return True
            color[u] = 2
            return False
        return any(color[i] == 0 and dfs(i) for i in range(len(g)))
```

### P260-T1 判断拓扑序列是否唯一

```python
from collections import deque

class Solution:
    def uniqueTopo(self, n: int, edges: list) -> bool:
        g = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            if len(q) > 1:
                return False
            u = q.popleft()
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return True
```

### P262-T2 邻接矩阵NextNeighbor

```python
class Solution:
    def nextNeighborMatrix(self, mat: list, x: int, y: int) -> int:
        for v in range(y + 1, len(mat)):
            if mat[x][v]:
                return v
        return -1
```

### P262-T3 邻接表NextNeighbor

```python
class Solution:
    def nextNeighborList(self, g: list, x: int, y: int) -> int:
        for i, v in enumerate(g[x]):
            if v == y and i + 1 < len(g[x]):
                return g[x][i + 1]
        return -1
```

## 第7章 查找

### P266-正文1 顺序查找

```python
class Solution:
    def sequentialSearch(self, nums: list, x) -> int:
        for i, v in enumerate(nums):
            if v == x:
                return i
        return -1
```

### P268-正文2 折半查找

```python
class Solution:
    def binarySearch(self, nums: list, x) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == x:
                return mid
            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

### P269-正文3 分块查找

```python
class Solution:
    def blockSearch(self, blocks: list, x) -> int:
        for block in blocks:
            if block and x <= max(block):
                for i, v in enumerate(block):
                    if v == x:
                        return i
                return -1
        return -1
```

### P271-正文 分块查找示例

```python
class Solution:
    def stepSearch(self, nums: list, x: int) -> int:
        k = 0
        while k < len(nums) and nums[k] < x:
            k += 3
        for i in (k, k - 1, k - 2):
            if 0 <= i < len(nums) and nums[i] == x:
                return i
        return -1
```

### P277-T1 递归折半查找

```python
class Solution:
    def binarySearch(self, nums: list, x: int) -> int:
        def dfs(l, r):
            if l > r:
                return -1
            m = (l + r) // 2
            if nums[m] == x:
                return m
            return dfs(m + 1, r) if nums[m] < x else dfs(l, m - 1)
        return dfs(0, len(nums) - 1)
```

### P277-T1 递归折半查找

```python
class Solution:
    def binarySearchRec(self, nums: list, x: int) -> int:
        def dfs(l, r):
            if l > r:
                return -1
            m = (l + r) // 2
            if nums[m] == x:
                return m
            return dfs(m + 1, r) if nums[m] < x else dfs(l, m - 1)
        return dfs(0, len(nums) - 1)
```

### P277-T2 顺序查找并前移

```python
class Solution:
    def seqSearchMoveFront(self, nums: list, x: int) -> int:
        for i, v in enumerate(nums):
            if v == x:
                if i > 0:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
                    return i - 1
                return i
        return -1
```

### P278-T3 二维有序矩阵查找

```python
class Solution:
    def findInMatrix(self, mat: list, x: int) -> bool:
        if not mat or not mat[0]:
            return False
        i, j = 0, len(mat[0]) - 1
        while i < len(mat) and j >= 0:
            if mat[i][j] == x:
                return True
            if mat[i][j] > x:
                j -= 1
            else:
                i += 1
        return False
```

### P280-正文4 BST查找

```python
class Solution:
    def searchBST(self, root, x):
        while root and root.val != x:
            root = root.right if root.val < x else root.left
        return root
```

### P281-正文5 BST插入

```python
class Solution:
    def insertIntoBST(self, root, x):
        if not root:
            return TreeNode(x)
        if x < root.val:
            root.left = self.insertIntoBST(root.left, x)
        elif x > root.val:
            root.right = self.insertIntoBST(root.right, x)
        return root
```

### P282-正文6 BST删除

```python
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            p = root.right
            while p.left:
                p = p.left
            root.val = p.val
            root.right = self.deleteNode(root.right, p.val)
        return root
```

### P302-T1 判断是否为BST

```python
class Solution:
    def isValidBST(self, root) -> bool:
        def dfs(node, lo, hi):
            if not node:
                return True
            return lo < node.val < hi and dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
        return dfs(root, float('-inf'), float('inf'))
```

### P302-T1 中序判断BST

```python
class Solution:
    def judgeBST(self, root) -> bool:
        pre = None
        def dfs(node):
            nonlocal pre
            if not node:
                return True
            if not dfs(node.left):
                return False
            if pre is not None and pre >= node.val:
                return False
            pre = node.val
            return dfs(node.right)
        return dfs(root)
```

### P302-T2 求BST结点层次

```python
class Solution:
    def levelOfBSTNode(self, root, x) -> int:
        level = 1
        while root:
            if root.val == x:
                return level
            root = root.left if x < root.val else root.right
            level += 1
        return 0
```

### P303-T3 BST查找小于x的最大元素

```python
class Solution:
    def predecessor(self, root, x):
        ans = None
        while root:
            if root.val < x:
                ans = root
                root = root.right
            else:
                root = root.left
        return ans
```

### P303-T3 判断AVL

```python
class Solution:
    def isAVL(self, root) -> bool:
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        return dfs(root) != -1
```

### P303-T4 BST最小值最大值

```python
class Solution:
    def minKey(self, root):
        while root and root.left:
            root = root.left
        return root.val if root else None

    def maxKey(self, root):
        while root and root.right:
            root = root.right
        return root.val if root else None
```

### P304-T2 求BST第k小

```python
class Solution:
    def kthSmallest(self, root, k: int):
        arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                arr.append(node.val)
                dfs(node.right)
        dfs(root)
        return arr[k - 1]
```

### P304-T5 输出BST中不小于k的值

```python
class Solution:
    def outputGeK(self, root, k) -> list:
        if not root:
            return []
        return self.outputGeK(root.right, k) + ([root.val] if root.val >= k else []) + self.outputGeK(root.left, k)
```

### P304-T6 带子树规模的BST第k小

```python
class Solution:
    def kthSmall(self, root, k: int):
        left_count = getattr(root.left, 'count', 0) if root and root.left else 0
        if not root or k < 1 or k > root.count:
            return None
        if left_count == k - 1:
            return root
        if left_count >= k:
            return self.kthSmall(root.left, k)
        return self.kthSmall(root.right, k - left_count - 1)
```

### P319-正文7 散列查找

```python
class HashTable:
    def __init__(self, m: int):
        self.m = m
        self.a = [None] * m

    def add(self, x: int) -> bool:
        for i in range(self.m):
            j = (x + i) % self.m
            if self.a[j] in (None, x):
                self.a[j] = x
                return True
        return False

    def search(self, x: int) -> int:
        for i in range(self.m):
            j = (x + i) % self.m
            if self.a[j] == x:
                return j
            if self.a[j] is None:
                return -1
        return -1
```

### P326-T1 判断整数集合是否有重复

```python
class Solution:
    def hasDuplicate(self, nums: list) -> bool:
        return len(nums) != len(set(nums))
```

## 第8章 排序

### P333-正文1 直接插入排序

```python
class Solution:
    def insertionSort(self, nums: list) -> list:
        for i in range(1, len(nums)):
            x = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > x:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = x
        return nums
```

### P334-正文2 折半插入排序

```python
class Solution:
    def binaryInsertionSort(self, nums: list) -> list:
        for i in range(1, len(nums)):
            x = nums.pop(i)
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= x:
                    left = mid + 1
                else:
                    right = mid
            nums.insert(left, x)
        return nums
```

### P335-正文3 希尔排序

```python
class Solution:
    def shellSort(self, nums: list) -> list:
        gap = len(nums) // 2
        while gap:
            for i in range(gap, len(nums)):
                x = nums[i]
                j = i
                while j >= gap and nums[j - gap] > x:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = x
            gap //= 2
        return nums
```

### P340-正文4 冒泡排序

```python
class Solution:
    def bubbleSort(self, nums: list) -> list:
        for i in range(len(nums) - 1):
            flag = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
            if not flag:
                break
        return nums
```

### P343-正文5 快速排序

```python
class Solution:
    def quickSort(self, nums: list) -> list:
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        left = [x for x in nums[1:] if x < pivot]
        right = [x for x in nums[1:] if x >= pivot]
        return self.quickSort(left) + [pivot] + self.quickSort(right)
```

### P348-T1 奇偶分区

```python
class Solution:
    def oddEvenPartition(self, nums: list) -> list:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
```

### P349-T3 快速选择第k小

```python
class Solution:
    def kthSmallest(self, nums: list, k: int):
        nums.sort()
        return nums[k - 1]
```

### P350-T1 荷兰国旗排序

```python
class Solution:
    def sortColors(self, nums: list) -> None:
        left = i = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
```

### P350-T2 奇偶分区

```python
class Solution:
    def oddEvenPartition(self, nums: list) -> list:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 1:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
```

### P350-T3 荷兰国旗问题

```python
class Solution:
    def flagArrange(self, nums: list) -> list:
        left = i = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        return nums
```

### P350-T4 集合划分最小差

```python
class Solution:
    def setPartition(self, nums: list) -> int:
        nums.sort()
        mid = len(nums) // 2
        return sum(nums[mid:]) - sum(nums[:mid])
```

### P351-正文6 简单选择排序

```python
class Solution:
    def selectionSort(self, nums: list) -> list:
        for i in range(len(nums)):
            k = min(range(i, len(nums)), key=lambda j: nums[j])
            nums[i], nums[k] = nums[k], nums[i]
        return nums
```

### P353-正文7 堆排序

```python
from heapq import heapify, heappop

class Solution:
    def heapSort(self, nums: list) -> list:
        heapify(nums)
        return [heappop(nums) for _ in range(len(nums))]
```

### P362-T1 判断是否为小根堆

```python
class Solution:
    def isMinHeap(self, nums: list) -> bool:
        n = len(nums)
        for i in range(n):
            l, r = 2 * i + 1, 2 * i + 2
            if l < n and nums[i] > nums[l]:
                return False
            if r < n and nums[i] > nums[r]:
                return False
        return True
```

### P362-T1 单链表选择排序

```python
class Solution:
    def selectSortList(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        dummy = p = ListNode()
        for x in sorted(vals):
            p.next = ListNode(x)
            p = p.next
        return dummy.next
```

### P362-T2 判断小根堆

```python
class Solution:
    def isMinHeap(self, nums: list) -> bool:
        return all((2 * i + 1 >= len(nums) or nums[i] <= nums[2 * i + 1]) and (2 * i + 2 >= len(nums) or nums[i] <= nums[2 * i + 2]) for i in range(len(nums)))
```

### P362-T3 优先队列入队出队

```python
from heapq import heappop, heappush

class PriorityQueue:
    def __init__(self):
        self.h = []

    def enqueue(self, value, priority):
        heappush(self.h, (priority, value))

    def dequeue(self):
        return heappop(self.h)[1] if self.h else None
```

### P364-正文 归并两个有序段

```python
class Solution:
    def mergeRange(self, nums: list, low: int, mid: int, high: int) -> None:
        nums[low:high + 1] = sorted(nums[low:high + 1])
```

### P366-正文8 二路归并排序

```python
class Solution:
    def mergeSort(self, nums: list) -> list:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        a = self.mergeSort(nums[:mid])
        b = self.mergeSort(nums[mid:])
        i = j = 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        return res + a[i:] + b[j:]
```

### P366-正文 计数排序

```python
class Solution:
    def countSort(self, nums: list, k: int) -> list:
        cnt = [0] * k
        for x in nums:
            cnt[x] += 1
        res = []
        for x, c in enumerate(cnt):
            res.extend([x] * c)
        return res
```

### P366-正文10 计数排序

```python
class Solution:
    def countingSort(self, nums: list) -> list:
        if not nums:
            return nums
        mn, mx = min(nums), max(nums)
        cnt = [0] * (mx - mn + 1)
        for x in nums:
            cnt[x - mn] += 1
        nums[:] = [i + mn for i, c in enumerate(cnt) for _ in range(c)]
        return nums
```

### P368-正文9 基数排序

```python
class Solution:
    def radixSort(self, nums: list) -> list:
        if not nums:
            return nums
        exp = 1
        while max(nums) // exp:
            bucket = [[] for _ in range(10)]
            for x in nums:
                bucket[x // exp % 10].append(x)
            nums[:] = [x for b in bucket for x in b]
            exp *= 10
        return nums
```

### P373-T1 合并k个有序表

```python
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: list) -> list:
        h = []
        for i, arr in enumerate(lists):
            if arr:
                heappush(h, (arr[0], i, 0))
        res = []
        while h:
            x, i, j = heappop(h)
            res.append(x)
            if j + 1 < len(lists[i]):
                heappush(h, (lists[i][j + 1], i, j + 1))
        return res
```

### P373-T1 计数比较排序片段

```python
class Solution:
    def compareCountSort(self, nums: list) -> list:
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    cnt[j] += 1
                else:
                    cnt[i] += 1
        res = [None] * len(nums)
        for i, c in enumerate(cnt):
            res[c] = nums[i]
        return res
```

### P379-T1 链表直接插入排序

```python
class Solution:
    def insertionSortList(self, head):
        dummy = ListNode()
        while head:
            p = dummy
            while p.next and p.next.val < head.val:
                p = p.next
            nxt = head.next
            head.next = p.next
            p.next = head
            head = nxt
        return dummy.next
```

### P379-T1 对子表直接插入排序

```python
class Solution:
    def insertSortRange(self, nums: list, m: int, n: int) -> list:
        for i in range(m + 1, m + n):
            x = nums[i]
            j = i - 1
            while j >= m and nums[j] > x:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = x
        return nums
```

### P380-T1 选择合适排序算法

```python
class Solution:
    def sortArray(self, nums: list) -> list:
        return sorted(nums)
```

### P380-T2 以最后元素划分

```python
class Solution:
    def partitionLast(self, nums: list) -> int:
        pivot = nums[-1]
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
        nums[i] = pivot
        return i
```

### P389-T1 置换选择生成初始归并段

```python
class Solution:
    def replacementSelection(self, nums: list, m: int) -> list:
        runs = []
        while nums:
            run = sorted(nums[:m])
            runs.append(run)
            nums = nums[m:]
        return runs
```
