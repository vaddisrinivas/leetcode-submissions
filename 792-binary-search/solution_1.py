# https://leetcode.com/problems/binary-search
import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)
        mid = (start+stop)//2
        while mid>=0 and mid<len(nums) and start!=stop:
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                stop = mid
            else:
                start = mid+1
            mid = (start+stop)//2
        else:
            return -1
            
# https://leetcode.com/problems/rotting-oranges
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        d = Queue()
        fo = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    d.put((i,j,0))
                elif grid[i][j]==1:
                    fo += 1
        m = set()
        twos = d.qsize()
        if fo==0:
            return 0
        while d.qsize()>0:
            i, j, k = d.get()
            r, c = len(grid),len(grid[i])
            # print(i,j,k,m,c)
            if grid[i][j]==1:
                grid[i][j]=2
                fo -= 1
            if i+1<r and 0<=j<c and grid[i+1][j]==1 and (i+1,j) not in m:
                d.put((i+1,j,k+1))
                m.add((i+1,j))
            if i-1>=0 and 0<=j<c and grid[i-1][j]==1  and (i-1,j) not in m:
                d.put((i-1,j,k+1))
                m.add((i-1,j))

            if 0<=i<r and j+1<c and grid[i][j+1]==1 and (i,j+1) not in m:
                d.put((i,j+1,k+1))
                m.add((i,j+1))

            if 0<=i<r and j-1 >=0 and grid[i][j-1]==1 and (i,j-1) not in m:
                d.put((i,j-1,k+1))
                m.add((i,j-1))

        return k if not fo else -1

                   
                   
         
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def cd(node,direction,c):
            
            if not node:
                return c  
            lc = cd(node.left, False, c+1 if direction else 1)
            rc = cd(node.right, True, c+1 if not direction else 1)
            return max(lc,rc)
        return cd(root, None, 0)-1
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i, j, k, l, c = 0, 0, 0, len(nums),-1
        while i<l and j<l:
            if nums[i]==nums[j]:
                c += 1
                if c<2:
                    nums[k] = nums[j]
                    k += 1
                j+=1
            else:
                c = -1
                i = j
        return k
# https://leetcode.com/problems/rotate-array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n #optimization based on fact -> n times rotation == NO rotation

        # reversing the first part of array 
        for i in range((n-k)//2):
            nums[i], nums[n-k-1-i] = nums[n-k-1-i], nums[i]

        # reversing the second part of array
        for i in range(k//2):
            nums[n-k+i], nums[n-1-i] = nums[n-1-i], nums[n-k+i]

        # reversing the entire array
        for i in range(n//2):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
# https://leetcode.com/problems/leaf-similar-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def cd(node):
            if not (node.left or node.right) : return [node.val]
            lc = cd(node.left) if node.left else []
            rc = cd(node.right) if node.right else []
            # print(lc,rc,node.val)
            return lc + rc 
        lc = cd(root1)
        rc = cd(root2)
        # print(lc,rc)
        return lc==rc
        
        
# https://leetcode.com/problems/leaf-similar-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def cd(node):
            if not (node.left or node.right) : return [node.val]
            lc = cd(node.left) if node.left else []
            rc = cd(node.right) if node.right else []
            print(lc,rc,node.val)
            return lc + rc 
        lc = cd(root1)
        rc = cd(root2)
        print(lc,rc)
        return lc==rc
        
        
# https://leetcode.com/problems/happy-number
class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            return sum([int(i)**2 for i in str(n)])
        
        slow, fast = n, sos(sos(n))

        while (slow != fast) and (fast != 1):
            # print(slow, fast)
            slow, fast = sos(slow),sos(sos(fast))
            # print(slow, fast)
        return fast == 1
# https://leetcode.com/problems/count-good-nodes-in-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def cd(node,max_num):
            if not (node.left or node.right) : return 1 if node.val>=max_num else 0
            lc = cd(node.left, max(max_num,node.val)) if node.left else 0
            rc = cd(node.right, max(max_num,node.val)) if node.right else 0
            return lc + rc + (1 if node.val>=max_num else 0)
        return cd(root,root.val)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def cd(node,max_num):
            if not (node.left or node.right) : return 1 if node.val>=max_num else 0
            lc = cd(node.left, max(max_num,node.val)) if node.left else 0
            rc = cd(node.right, max(max_num,node.val)) if node.right else 0
            return lc + rc + (1 if node.val>=max_num else 0)
        return cd(root,root.val)
# https://leetcode.com/problems/reverse-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        holder = curr

        while curr:
            holder = curr.next
            curr.next = prev
            prev = curr
            curr = holder
        return prev
# https://leetcode.com/problems/decode-string
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res = ""
        i = 0
        dig = ""
        while i < len(s):
            if s[i].isdigit():
                dig += s[i]
            elif s[i].isalpha():
                if len(st)==0:
                    res += s[i]
                else:
                    st[0][1]+= s[i]
            elif s[i]=="[":
                st = [[int(dig),""]]+st
                dig = ""
            elif s[i]=="]":
                if len(st)==1:
                    res += st[0][0]*st[0][1]
                    st = []
                else:
                    st[1][1] += st[0][0]*st[0][1]
                    del st[0]
            i += 1
        return res






            
                
                
                



# https://leetcode.com/problems/maximum-average-subarray-i
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k])
        prev = sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            prev = prev-nums[i-1]+nums[i+k-1]
            avg = max(avg,prev)
        return avg/k
# https://leetcode.com/problems/longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dup = [1]*len(nums)
        for i,j in enumerate(nums[1:],1):
            dup[i] += max([0] + [dup[k] for k,l in enumerate(dup[:i]) if nums[k]<j])
        return max(dup)
        
# https://leetcode.com/problems/longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dup = [1]*len(nums)
        for i,j in enumerate(nums[1:],1):
            prev = [dup[k] for k,l in enumerate(dup[:i]) if nums[k]<j]
            dup[i] += max(prev) if prev else 0
        return max(dup)
        
# https://leetcode.com/problems/path-sum-iii
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def cd(node, visited):  
            if not node:
                return 0
            c = 0
            for i,j in enumerate(visited):
                visited[i] = j + node.val
                if visited[i]==targetSum:
                    c += 1
            
            visited += [node.val]
            if visited[-1]==targetSum:
                c += 1
            lc = cd(node.left, visited.copy()) if node.left else 0
            rc = cd(node.right, visited.copy()) if node.right else 0
            return c + rc + lc
        if not root:
            return 0
    
        return cd(root, [])
# https://leetcode.com/problems/max-consecutive-ones-iii
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = [i for i, j in enumerate(nums) if j == 0]
        zeros = [-1] + zeros + [len(nums)]
        start, stop, maxcon = 1, 1, 0
        before, between = 0, 0

        if k == len(nums) or k>len(zeros):
            return len(nums)

        while stop < len(zeros):
            if (stop - start) == k:
                before, between = zeros[start] - zeros[start - 1], zeros[stop] - zeros[start] -1
                maxcon = max(maxcon, before + between)
                start += 1
            stop += 1
        return maxcon
# https://leetcode.com/problems/max-consecutive-ones-iii
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = [i for i, j in enumerate(nums) if j == 0]
        zeros = [-1] + zeros + [len(nums)]
        start, stop, maxcon = 1, 1, 0
        before, between = 0, 0

        if k == len(nums) or k>len(zeros):
            return len(nums)

        while stop < len(zeros):
            if (stop - start) == k:
                before, between = zeros[start] - zeros[start - 1], zeros[stop] - zeros[start] -1
                maxcon = max(maxcon, before + between)
                start += 1
            stop += 1
        return maxcon
# https://leetcode.com/problems/product-of-array-except-self
from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        i = prod(nums)
        count_zeros = nums.count(0)
        if i==0 and count_zeros == 1:
            product = prod(nums[:nums.index(0)])*prod(nums[nums.index(0)+1:])
            for m,n in enumerate(nums):
                if n==0:
                    nums[m] = product
                else:
                    nums[m] = 0        
        elif i==0 and count_zeros!=1:
            for m,n in enumerate(nums):
               nums[m] = 0
        else:
            for m,n in enumerate(nums):
                nums[m] = i//n
        return nums
# https://leetcode.com/problems/string-compression
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==1:
            return 1
        s = ""
        i = 1
        temp = chars[0]
        prev = 1
        while i<len(chars):
            if chars[i]==temp:
                prev += 1
            else:
                s += temp+(str(prev) if prev>1 else "")
                temp = chars[i]
                prev = 1
            i += 1
        s += temp+(str(prev) if prev>1 else "")
        # print(s)
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)               
# https://leetcode.com/problems/flood-fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        try:
            m = len(image)
            n = len(image[0])
        except:
            return [[]]*m
        if sr>m and sc>n:
            return image
        target = image[sr][sc]
        stack = []
        visited = {(i,j):False for j in range(n) for i in range(m)}
        i = sr
        j = sc

        def change(i,j):
            print("in change",i,j)
            visited[(i,j)]=True
            if image[i][j]==target:
                image[i][j]=color
                return True
            else:
                return False
        
        def dfs(i,j):
            print("in dfs",i,j)
            if i>=m or j>=n:
                return False
            if i<0 or j<0:
                return False
            if visited[(i,j)]:
                return False            
            stack.append((i,j))
            if change(i,j):
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                stack.pop()
            return 
        dfs(i,j)
        return image
# https://leetcode.com/problems/the-kth-factor-of-n
12
# 1 3 5 6 4 2
# 1 2 3 4 6 12
# 1,2,3,4,6,12

import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = 0
        x = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                x.append(i)
                if i!=n//i:
                    x.append(n//i)            
        x.sort()
        return x[k-1] if k <=len(x) else -1
# https://leetcode.com/problems/the-kth-factor-of-n
12
# 1 3 5 6 4 2
# 1 2 3 4 6 12
# 1,2,3,4,6,12

import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = 0
        x = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                x.append(i)
                x.append(n//i)            
        x = sorted(set(x))
        return x[k-1] if k <=len(x) else -1
# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min(strs,key=len)
        res = ""
        broken = False
        for i in range(len(l)):
            for j in range(len(strs)):
                if l[i]!=strs[j][i]:
                    broken=True
                    break
            if broken: return res
            res += l[i]
            
        return res
# https://leetcode.com/problems/reverse-bits
class Solution:
    def reverseBits(self, n: int) -> int:
        n = list(bin(n))[2:]
        l = len(n)
        print(l)
        exn = ['0']*(32-l)
        exn.extend(n)
        n = exn
        l = len(n)
        print(l)

        for i in range((l//2)):
            print(n[i],n[l-1-i])
            n[i],n[l-1-i]=n[l-1-i],n[i]
            
        print("".join(n))
        return int("".join(n),2)

        
# https://leetcode.com/problems/number-of-provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected = []
        for i in range(len(isConnected)):
            temp = [g for g in connected if i+1 in g]
            exists = True if len(temp)>0 else False
            if len(temp)>1:
                for k in temp:
                    connected.remove(k)
                temp = [set().union(*temp)]
                connected.append(temp[0])
            ic = temp[0] if exists else set()
            ic.add(i+1)
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    ic.add(j+1)
            if not exists:
                connected.append(ic)
        
        return len(connected)
# https://leetcode.com/problems/number-of-provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected = []
        for i in range(len(isConnected)):
            # print(isConnected[i])
            temp = [g for g in connected if i+1 in g]
            exists = True if len(temp)>0 else False
            if exists and len(temp)>1:
                for k in temp:
                    connected.remove(k)
                temp = [set().union(*temp)]
                # print(temp,"<---")
                connected.append(temp[0])
            ic = temp[0] if exists else set()
            ic.add(i+1)
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    ic.add(j+1)
            if not exists:
                connected.append(ic)
        
        return len(connected)
# 1,4
# 2,3
# 2,3,4
# 1,3,4
# https://leetcode.com/problems/power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        while n>0:
            if n&1:
                c+=1
            n = n >> 1
        return c==1
# https://leetcode.com/problems/power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        while n>0:
            print(n,n&1)
            if n&1:
                c+=1
            n = n >> 1
        return c==1
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = len(s)
        c = 0
        if l < 3:
            return 0
        
        ss = {'a', 'b', 'c'}
        curr_ss = {char: 0 for char in ss}
        start = 0
        ind = 0
        
        while ind < l:
            curr_ss[s[ind]] += 1
            
            while all(curr_ss[char] > 0 for char in ss):
                c += l - ind
                curr_ss[s[start]] -= 1
                start += 1
            
            ind += 1
        
        return c
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = len(s)
        c = 0
        if l < 3:
            return 0
        
        ss = {'a', 'b', 'c'}
        curr_ss = {char: 0 for char in ss}
        start = 0
        ind = 0
        
        while ind < l:
            curr_ss[s[ind]] += 1
            
            while all(curr_ss[char] > 0 for char in ss):
                c += l - ind
                curr_ss[s[start]] -= 1
                start += 1
            
            ind += 1
        
        return c
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      v = set(list("aeiou"))
      mv = sum([1 if i in v else 0 for i in s[:k]])
      cv = mv
      for i in range(1,len(s)-k+1):
        cv = cv-1 if s[i-1] in v else cv
        cv = cv+1 if s[i+k-1] in v else cv
        mv = mv if mv > cv else cv
      return mv

# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      v = set(list("aeiou"))
      mv = sum([1 if i in v else 0 for i in s[:k]])
      cv = mv
      for i in range(1,len(s)-k+1):
        cv = cv-1 if s[i-1] in v else cv
        cv = cv+1 if s[i+k-1] in v else cv
        mv = max(mv,cv)
      return mv

# https://leetcode.com/problems/can-place-flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while n>0 and i< len(flowerbed):
            if flowerbed[i]==0 and flowerbed[max(0,i-1)]==0 and flowerbed[min(i+1,len(flowerbed)-1)]==0:
                flowerbed[i]=1    
                n-=1
            i += 1
        return n==0


        
# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n =""
        for i in s:
            if i.isalnum():n+=i.lower()
        s=n
        l=len(s)
        if l==1:
            return True
        elif l==2:
            return s[0]==s[1]
        elif l==3:
            return s[0]==s[2]
        if l%2==0:
            return s[:l//2]==s[l//2:][::-1]
        else:
            return s[:(l//2)-1]==s[(l//2)+2:][::-1]
# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalnum()])
        left, right = 0, len(s)-1
        while left <= right:
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        return True
# https://leetcode.com/problems/greatest-common-divisor-of-strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i, j = 0,0
        res = ""
        s1, s2 = set(str1),set(str2)
        def makeStr(s, x):
            return s*(x.count(s))==x
        while i< len(str1) and j<len(str2):
            curr1, curr2 = str1[:i+1],str2[:j+1]
            if curr1==curr2:
                if (makeStr(curr1,str1) and makeStr(curr1,str2)):
                  res = curr1
            else:
                return res
            i+=1
            j+=1
        return res
# https://leetcode.com/problems/greatest-common-divisor-of-strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i, j = 0,0,
        res = ""
        s1, s2 = set(str1),set(str2)
        def makeStr(s, x):
            q = len(x)//len(s)
            if len(x)%len(s)!=0:
                return False
            else:
                return s*q == x

        while i< len(str1) and j<len(str2):
            curr1, curr2 = str1[:i+1],str2[:j+1]
            if curr1==curr2:
                if (makeStr(curr1,str1) and makeStr(curr1,str2)):
                  res = curr1
            else:
                return res
            i+=1
            j+=1
        return res
# https://leetcode.com/problems/keys-and-rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def v(room):
            nonlocal rooms, visited
            # print(room,visited)
            if room in visited:
                return
            else:
                visited.add(room)
                for i in rooms[room]:
                    if i not in visited:
                        v(i)
        v(0)
        # print(visited)
        return len(visited)==len(rooms)
        
# https://leetcode.com/problems/missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)+1
        expected =  l*(l-1)//2
        return expected-sum(nums)
# https://leetcode.com/problems/middle-of-the-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        while s.next is not None:
            f = f.next
            s = s.next
            if s.next is not None:
                s = s.next
        return f
        
        
# https://leetcode.com/problems/intersection-of-two-arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        return list(set([i for i in nums2  if i in nums1]))
# https://leetcode.com/problems/is-subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return True if i==len(s) else  False
        
# https://leetcode.com/problems/online-stock-span
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# https://leetcode.com/problems/smallest-number-in-infinite-set
class SmallestInfiniteSet:
    def __init__(self):
        self.c = 1
        self.s = set()
    def popSmallest(self):
        if self.s:
            r = min(self.s)
            self.s.remove(r)
            return r
        else:
            self.c += 1
            return self.c - 1
    def addBack(self, num):
        if self.c > num:
            self.s.add(num) 

        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# https://leetcode.com/problems/merge-strings-alternately
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0,0
        res = ""
        while i<len(word1) and j< len(word2):
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        if i!=len(word1):
            res+=word1[i:]
        elif j!=len(word2):
            res+=word2[j:]
        return res
# https://leetcode.com/problems/binary-tree-right-side-view
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append((root,0))
        prev_height = 0
        prev_node = None
        to_print = []
        while queue:
            pop, queue = queue[-1], queue[:-1]
            if prev_height!=pop[1]:
                to_print += [prev_node.val]
            prev_height,prev_node = pop[1],pop[0]
            queue = ([(pop[0].left,pop[1]+1)] if pop[0] and pop[0].left else [] )+ queue
            queue = ([(pop[0].right,pop[1]+1)] if pop[0] and pop[0].right else [] )+ queue
        else:
            if prev_node:
                to_print += [prev_node.val]
        return to_print
# https://leetcode.com/problems/zigzag-conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """        
        if numRows ==1:
            return s
        col = 0
        sol_dict = {i:[] for i in range(numRows)}
        row = 0
        c = 0
        while c < len(s):
            if row == numRows:
                while row-1>0 and c<len(s):
                    row-=1
                    col+=1
                    sol_dict[row-1].append(s[c])
                    c+=1
                continue
            sol_dict[row].append(s[c])
            row+=1
            c+=1 
        return "".join("".join(sol_dict[i]) for i in range(numRows))
# https://leetcode.com/problems/zigzag-conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """        
        if numRows ==1:
            return s
        solution = ""
        col = 0
        sol_dict = {i:[] for i in range(numRows)}
        row = 0
        c = 0
        while c < len(s):
            if row == numRows:
                while row-1>0 and c<len(s):
                    row-=1
                    col+=1
                    sol_dict[row-1].append(s[c])
                    c+=1
                continue
            sol_dict[row].append(s[c])
            row+=1
            c+=1 
        return "".join("".join(sol_dict[i]) for i in range(numRows))
# https://leetcode.com/problems/isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        chars = {}
        if len(set(s))!=len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] in chars:
                if t[i]!=chars[s[i]]:
                    return False
            else:
                chars[s[i]]=t[i]
        return True
# https://leetcode.com/problems/number-of-1-bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(bin(n)).count("1")
# Write your MySQL query statement below
# https://leetcode.com/problems/h-index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if len(citations)==1: return 1 if citations[0] else 0
        if sum(citations)==0: return 0
        flag = False
        for i in range(len(citations)):
            if i+1>citations[i]:
                flag = True
                break
        return i if flag else len(citations)
# https://leetcode.com/problems/remove-element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,len(nums)-1
        l = len(nums)
        while i<=j:
            if nums[j]==val:
                j-=1
                continue
            if nums[i]==val:
                nums[i],nums[j]= nums[j],nums[i]
                j -= 1
            i += 1
        return  j+1 if i>j else 0

            
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        l = len(potions)
        def bns(target):
            m = l//2
            x, y = 0, l
            while x<y:
                if potions[m] >= target:
                    y = m
                elif potions[m] < target:
                    x = m+1
                else:
                    break
                m = (x+y)//2
            return m
        return  [l-bns(success/i) for i in spells]
# https://leetcode.com/problems/contains-duplicate-ii
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start, curr = 0,0
        s = dict()

        while curr < len(nums):
            # print(locals())
            if nums[curr] in s:
                if( curr-s[nums[curr]])<=k:
                    return True
                else:
                    start = curr
                    s.clear()
                    s[nums[curr]] = curr
            else:
                s[nums[curr]] = curr
            curr += 1
        return False

# https://leetcode.com/problems/reverse-words-in-a-string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        for j in ([i for i in s.strip().split(" ")][::-1]):
            if len(j)==0:
                continue
            r += j+" "
        return r.strip()
# https://leetcode.com/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(heap):
            m = len(heap)-1
            n =  0
            while n<=(m+1)//2:
                l, r = min(2*n+1,m),min( 2*n+2,m)
                largest = n
                if heap[r]<heap[largest]:
                    largest = r
                if heap[l]<heap[largest]:
                    largest = l
                    if heap[r]<heap[l]:
                        largest = r
                if largest!=n:
                    heap[n],heap[largest] = heap[largest],heap[n]
                    n = largest
                else:
                    break
            return heap

        def heap_up(heap):
            n= len(heap)-1
            while n>0:
                if heap[(n-1)//2]>heap[n]:
                    heap[(n-1)//2], heap[n]=heap[n],heap[(n-1)//2]
                    n = (n-1) //2
                else:
                    break
            return heap   
        heap = []
        for j,i in enumerate(nums):
            if j < k:
                heap.append(i)
                heap = heap_up(heap)
                continue
            if heap[0]<=i:
                heap[0] = i
                heap = heapify(heap)

        return heap[0]
# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        nums[2] += nums[0]
        if len(nums)==3:
            return max(nums)
        for ind,i in enumerate(nums[3:],3):
            nums[ind] += max(nums[ind-2],nums[ind-3])
        return max(nums[-1],nums[-2])
# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 8,7,8,9,7,8
        # 8,7,16,17,23,25
        # 2,7,9,3,1
        # 2,7,11,10,12
        # 7,2,3,9,1
        # 7,2,10,16,11
        if len(nums)<=2:
            return max(nums)
        nums[2] += nums[0]
        if len(nums)==3:
            return max(nums)
        for ind,i in enumerate(nums[3:],3):
            nums[ind] += max(nums[ind-2],nums[ind-3])
        return max(nums[-1],nums[-2])
# https://leetcode.com/problems/odd-even-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            odd, even, evenhead = head, head.next, head.next
        except:
            return head
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next=odd.next
            even = even.next
        odd.next = evenhead
        return head
# https://leetcode.com/problems/odd-even-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            odd, even, evenhead = head, head.next, head.next
        except:
            return head
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next=odd.next
            even = even.next
        odd.next = evenhead
        return head
# https://leetcode.com/problems/search-in-a-binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def s(node,val):
            if not node:
                return
            if node.val==val:
                return node
            elif node.val>val:
                return s(node.left,val)
            else:
                return s(node.right,val)
        return s(root,val)
# https://leetcode.com/problems/search-in-a-binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def s(node,val):
            if not node:
                return
            if node.val==val:
                return node
            elif node.val>val:
                return s(node.left,val)
            else:
                return s(node.right,val)
        return s(root,val)
# https://leetcode.com/problems/unique-paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = [0]*n
        g = [c]*m
        g[-1] = [1]*n
        if m<2:
            return 1
        for i in range(m):
            g[i][-1]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                g[i][j] = g[i+1][j]+g[i][j+1]
                
        return g[0][0]



# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
class Solution:
   def longestSubarray(self, nums: List[int]) -> int:
        zeros = [i for i,j in enumerate(nums) if j==0]
        p = 0
        max1s = 0
        if len(zeros)==len(nums):
            return 0
        elif len(zeros)<2:
            return len(nums)-1
        else:
            zeros = [-1] + zeros + [len(nums)]
        while p<len(zeros)-2:
            i, j, k = zeros[p:p+3]
            max1s = max(max1s, k-1-i-1)
            p += 1
        return max1s
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
class Solution:
   def longestSubarray(self, nums: List[int]) -> int:
        zeros = [i for i,j in enumerate(nums) if j==0]
        p = 0
        max1s = 0
        # print(locals())
        if len(zeros)==len(nums):
            return 0
        elif len(zeros)<2:
            return len(nums)-1
        else:
            zeros = [-1] + zeros + [len(nums)]
        # print(locals())
        while p<len(zeros)-2:
            # print(locals())
            i, j, k = zeros[p:p+3]
            max1s = max(max1s, k-1-i-1)
            p += 1
            # print(locals())
        return max1s
# https://leetcode.com/problems/find-median-from-data-stream
class MedianFinder:

    def __init__(self):
        self.len = 0
        self.arr = []
        self.odd = False

    def addNum(self, num: int) -> None:
        l,r = 0,self.len
        mid = (l+r)//2
        while l<r:
            # print(l,r,mid,self.len,self.arr[mid],num)
            if self.arr[mid]<num:
                r = mid
            elif self.arr[mid]>num:
                l = mid+1
            else:
                break
            mid = (l+r)//2
        self.arr.insert(mid,num)
        self.len += 1
        self.odd = not self.odd
        # print(self.arr)

    def findMedian(self) -> float:
        # print(self.odd)
        if self.odd:
            return self.arr[self.len//2]
        else:
            return (self.arr[(self.len//2)]+self.arr[(self.len//2)-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# https://leetcode.com/problems/find-median-from-data-stream
class MedianFinder:

    def __init__(self):
        self.len = 0
        self.arr = []
        self.odd = False

    def addNum(self, num: int) -> None:
        l,r = 0,self.len
        mid = (l+r)//2
        while l<r:
            # print(l,r,mid,self.len,self.arr[mid],num)
            if self.arr[mid]<num:
                r = mid
            elif self.arr[mid]>num:
                l = mid+1
            else:
                break
            mid = (l+r)//2

        self.arr.insert(mid,num)
        self.len += 1
        self.odd = not self.odd
        # print(self.arr)

    def findMedian(self) -> float:
        # print(self.odd)
        if self.odd:
            return self.arr[self.len//2]
        else:
            return (self.arr[(self.len//2)]+self.arr[(self.len//2)-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        c = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        x = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i,n =len(s)-1,0
        while i>-1:
            if s[i-1]+s[i] in c:
                n+=c[s[i-1]+s[i]]
                i-=2
            else:
                n+=x[s[i]]
                i-=1
            if i==0:
                n+=x[s[i]]
                break
        return n
# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        c = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        x = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i,l =len(s)-1,len(s)
        n = 0
        while i>-1:
            if s[i-1]+s[i] in c:
                n+=c[s[i-1]+s[i]]
                i-=2
            else:
                n+=x[s[i]]
                i-=1
            if i==0:
                n+=x[s[i]]
                break
        return n
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
from pprint import pprint
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        res = [0]*len(prices)
        res[1]=prices[1]-prices[0]
        for i in range(1,len(prices)):
            p = res[i-1]
            res[i] = max(p,p+prices[i]-prices[i-1])
        return res[-1]
# https://leetcode.com/problems/unique-number-of-occurrences
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return len(set(d.values()))==len(d.values())
# https://leetcode.com/problems/unique-number-of-occurrences
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return len(set(d.values()))==len(d.values())
# https://leetcode.com/problems/search-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
# https://leetcode.com/problems/first-bad-version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        stop = n
        mid = (start+stop)//2
        while start<stop:
            # print(start, stop, mid)
            if isBadVersion(mid):
                stop = mid
            else:
                start = mid + 1
            mid = (start+stop)//2
        return stop
# https://leetcode.com/problems/reverse-vowels-of-a-string
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))
        front, back = 0, len(s)-1
        ff, fb = False, False
        while front<back:
            ff = s[front] in vowels
            fb = s[back] in vowels
            if ff and fb:
                # swap
                s = s[:front]+s[back]+s[front+1:back]+s[front]+s[back+1:]
                ff, fb = False, False
                front += 1
                back -= 1
            elif ff and not fb:
                # move from back
                back -= 1
            elif not ff and fb:
                # move from front
                front += 1
            else:
                front += 1
                back -= 1
        return s
# https://leetcode.com/problems/integer-to-roman
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result
# https://leetcode.com/problems/evaluate-division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        inc = 0
        out = 1
        for i,j in enumerate(equations):
            if j[inc] in d:
                d[j[inc]].update({j[out]:values[i]})
            else:
                d[j[inc]] = {j[out]:values[i]}
            if j[out] in d:
                d[j[out]].update({j[inc]:1/values[i] if values[i]!=0 else -1})
            else:
                d[j[out]] = {j[inc]:1/values[i] if values[i]!=0 else -1}
        res = []

        def cd(curr, target,visited,prod=1):
            nonlocal d
            if target in d[curr]:
                return prod*d[curr][target]
            res = None
            for i in d[curr]:
                if i not in visited:
                    visited.add(i)
                    val = cd(i,target,visited.copy(),prod*d[curr][i])
                    if val:
                        res = val
                    visited.remove(i)
            return res
            
            
        for i, j in enumerate(queries):
            if j[inc] not in d or j[out] not in d:
                res.append(-1)
                continue
            val = cd(j[inc],j[out],set(),1)
            res.append(val if val else -1)
        return res
# https://leetcode.com/problems/find-pivot-index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = sum(nums)

        for i in range(len(nums)):
            rSum -= nums[i]
            if lSum == rSum:
                return i
            lSum += nums[i]       
        return -1
        
# https://leetcode.com/problems/find-pivot-index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        temp = 0
        for i,j in enumerate(nums):
            if temp==s-temp-j:
                return i
            temp+=j
        return -1
# https://leetcode.com/problems/removing-stars-from-a-string
class Solution:
    def removeStars(self, s: str) -> str:
        star = '*'
        ind = 0
        c = 0
        while ind<len(s):
            if s[ind]==star:
                s = s[:ind-1]+s[ind+1:]
                ind -=1
                continue
            ind += 1
        return s
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j,l = 0,len(numbers)-1,len(numbers)
        if l==2: return [1,2] if sum(numbers)==target else []
        while i<l and j>-1:
            if j>0 and numbers[j]>target:
                j-=1
                continue
            t = numbers[i]+numbers[j]
            # print(i,j,t)
            if t<target:
                i+=1
                continue
            elif t>target:
                j-=1
            else:
                if i<j:
                    return [i+1,j+1] 
                elif j<i:
                    return [j+1,i+1]
                else:
                    return [i+1,i+2]
            
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j,l = 0,len(numbers)-1,len(numbers)
        if l==2: return [1,2] if sum(numbers)==target else []
        while i<l and j>-1:
            if j>0 and numbers[j]>target:
                j-=1
                continue
            t = numbers[i]+numbers[j]
            # print(i,j,t)
            if t<target:
                i+=1
                continue
            elif t>target:
                j-=1
            else:
                if i<j:
                    return [i+1,j+1] 
                elif j<i:
                    return [j+1,i+1]
                else:
                    return [i+1,i+2]
            
# https://leetcode.com/problems/max-number-of-k-sum-pairs
# from pprint import pprint
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # comps = [abs(k-i) for i in nums]
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                dict_nums[i]+=1
            else:
                dict_nums[i]=1
        i = 0
        j = 0
        # print(dict_nums)
        while i<len(nums):
            # pprint(locals())
            if dict_nums[nums[i]]>0:
                dict_nums[nums[i]] -= 1
            else:
                i+=1
                continue
            if k-nums[i] in dict_nums and dict_nums[k-nums[i]]>0:
                dict_nums[k-nums[i]] -= 1
                j += 1
            else:
                dict_nums[nums[i]] += 1
            i += 1
        return j

# https://leetcode.com/problems/find-the-highest-altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        s = 0
        for i in gain:
            s += i
            m = max(s,m)
        return m
        
# https://leetcode.com/problems/counting-bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 0 2**0
        # 1 1 
        # 1 0 2**1
        # 2 1
        # 1 0 2**2
        # 2 1 
        # 2 0
        # 3 1
        # 1 0 2**3
        # 2 1
        # 2 0
        # 3 1 
        # 2 0
        # 3 1
        # 3 0
        # 4 1
        # 1 0 2**4
        # FIRST HALF, FIRST HALF + 1
        if n==0:
            return [0]
        i = 2
        p = 0
        x = 0
        y = 0
        res = [0,1]
        while i < n+1:
            if i==2**(p+1):
                res.append(1)
                x = 1
                y = 0
                p += 1
            elif i < 2**p + 2**(p-1):
                res.append(res[2**(p-1)+x])
                x += 1
            else:
                res.append(res[2**(p-1)+y]+1)
                y += 1
            i += 1
        return res


# https://leetcode.com/problems/number-of-recent-calls
class RecentCounter:

    def __init__(self):
        self.queue = []
        self.pointer = -1

    def ping(self, t: int) -> int:
        self.queue = [t]+self.queue
        self.pointer += 1
        for i in range(self.pointer,-1,-1):
            if self.queue[i]>=t-3000:
                self.pointer = i
                return i+1

        return len(self.queue) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# https://leetcode.com/problems/number-of-recent-calls
class RecentCounter:

    def __init__(self):
        self.queue = []
        self.pointer = -1

    def ping(self, t: int) -> int:
        self.queue = [t]+self.queue
        self.pointer += 1
        for i in range(self.pointer,-1,-1):
            if self.queue[i]>=t-3000:
                self.pointer = i
                return i+1

        return len(self.queue) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# https://leetcode.com/problems/find-the-difference-of-two-arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        return [a.difference(b),b.difference(a)]
        
# https://leetcode.com/problems/jump-game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = len(nums)-1
        for i in range(p,-1,-1):
            if i+nums[i]>=p:
                p = i
        return p==0

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit, profit, curr_min = 0, 0, prices[0]
        i = 1
        while i<len(prices):
            j = prices[i]
            curr_profit = j - curr_min
            if curr_profit>profit:
                profit = curr_profit
            if prices[i]<curr_min:
                curr_min = prices[i]
            i += 1
        return profit
            


# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -1000000
        max_ending_here = 0

        for rating in nums:
            max_ending_here = max_ending_here + rating
            if max_ending_here < rating:
                max_ending_here = rating
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
        return max_so_far
# https://leetcode.com/problems/increasing-triplet-subsequence
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = []
        b = [0]*len(nums)
        prev = nums[0]
        s.append(prev)
        for i in nums[1:]:
            if i <prev:
                prev = i
            s.append(prev)
    
        j = len(nums)-1
        prev = nums[j]
        b[j] = nums[j]
        while j>-1:
            if nums[j]>prev:
                prev = nums[j]
            b[j] = prev
            j -= 1
        i = 0
        while i< len(nums):
            if s[i]<nums[i]<b[i]:
                return True
            i += 1
        return False



        
# https://leetcode.com/problems/maximum-depth-of-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cd(node):
            if not node:
                return 0
            if node.right and node.left:
                return 1+max(cd(node.right),cd(node.left))
            elif node.right and not node.left:
                return 1+cd(node.right)
            elif not node.right and node.left:
                return 1+cd(node.left)
            else:
                return 1
        return cd(root)
# https://leetcode.com/problems/maximum-depth-of-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cd(node):
            if not node:
                return 0
            if node.right and node.left:
                return 1+max(cd(node.right),cd(node.left))
            elif node.right and not node.left:
                return 1+cd(node.right)
            elif not node.right and node.left:
                return 1+cd(node.left)
            else:
                return 1
        return cd(root)
# https://leetcode.com/problems/combination-sum-iii
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def bt(curr,curr_pos,st,s):
            if curr_pos==k-1:
                if st<=n-s<=9:
                    result.append(curr+[n-s])
                return
            for i in range(st,10):
                if i>=n-s:
                    continue
                bt(curr + [i],curr_pos+1,i+1,s+i)
        bt([],0,1,0)
        return result
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        arr = []
        m = 0
        c = 0
        while slow is not None:
            c += 1
            slow = slow.next
        t = 0
        slow = head
        while slow is not None:
            if t<c//2:
                arr += [slow.val]
            else:
                m = max(m,arr.pop() +slow.val)
            slow = slow.next
            t += 1
        return m


        
# https://leetcode.com/problems/container-with-most-water
from pprint import pprint
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def area(l,b):
            return l*b

        l = len(height)
        if l==2:
            return area(1,min(height[0],height[1]))
        m1, m2 = 0, l-1
        max_area = 0
        area_temp = 0
        while m1<=m2 :
            # pprint(locals())
            if height[m1]>height[m2]:
                area_temp = area(m2-m1, height[m2])
                m2 -= 1
            else:
                area_temp = area(m2-m1, height[m1])
                m1 += 1
            if area_temp > max_area:
                max_area = area_temp
            # pprint("*"*10)
            # pprint(locals())
            # pprint("-"*10)
        return max_area
        
# Write your MySQL query statement below
from world where area>=3000000 or population>=25000000;
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue,ms,lms, ps, prev_height = [(root,0)], root.val, 0, 0, 0
        while queue:
            pop, queue = queue.pop(), queue
            if prev_height!=pop[1]:
                if ms<ps:
                    ms = ps
                    lms = prev_height
                ps = 0
            ps += pop[0].val
            prev_height,prev_node = pop[1],pop[0]
            queue = ([(pop[0].left,pop[1]+1)] if pop[0] and pop[0].left else [] )+ queue
            queue = ([(pop[0].right,pop[1]+1)] if pop[0] and pop[0].right else [] )+ queue
        else:
            if ms<ps:
                ms = ps
                lms = prev_height 
        return lms+1
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue,ms,lms, ps, prev_height = [(root,0)], root.val, 0, 0, 0
        while queue:
            pop, queue = queue.pop(), queue
            if prev_height!=pop[1]:
                if ms<ps:
                    ms = ps
                    lms = prev_height
                ps = 0
            ps += pop[0].val
            prev_height,prev_node = pop[1],pop[0]
            queue = ([(pop[0].left,pop[1]+1)] if pop[0] and pop[0].left else [] )+ queue
            queue = ([(pop[0].right,pop[1]+1)] if pop[0] and pop[0].right else [] )+ queue
        else:
            if ms<ps:
                ms = ps
                lms = prev_height 
        return lms+1
# https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = 0
        l = len(nums)
        for i in range(l):
            if nums[i]==0:
                ct+=1
                continue
            else:
                nums[i-ct]=nums[i]
        for i in range(l-ct,l):
            nums[i]=0
            
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i,j,k = 0, 1,1
        l = len(nums)
        if l==2:
            return 2 if nums[0]!=nums[1] else 1
        while i<l-1:
                
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[k]=nums[j]
                i = j
                j+=1
                k+=1
            if j==l and k!=l:
                nums[k]=nums[j-1]
                break
        return k
# https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i,j,l = 0,0,len(nums)
        mc,c = 0,0
        while i<l and j<l:
            if nums[i]==nums[j]:
                c += 1
                j += 1
            else:
                mc = max(c,mc)
                if mc>l/2:
                    break
                c = 0
                i = j
        return nums[j-1]
# https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = Counter(nums)
        l = len(nums)
        for i in s:
            if s[i]>l/2:
                return i
        
# https://leetcode.com/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = list(accumulate([gas[i]-cost[i] for i in range(len(gas))]))
        if diffs[-1]<0:return -1
        m,ind = diffs[0],0
        for i in range(1,len(diffs)):
            if diffs[i]<=m:
                m,ind = diffs[i],i
        return (ind+1)%len(gas)
# https://leetcode.com/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = list(accumulate([gas[i]-cost[i] for i in range(len(gas))]))
        print(diffs)
        if diffs[-1]<0:return -1
        m,ind = diffs[0],0
        for i in range(1,len(diffs)):
            if diffs[i]<=m:
                m,ind = diffs[i],i
        return (ind+1)%len(gas)
# https://leetcode.com/problems/single-number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}
        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        for i in s:
            if s[i]==1:
                return i
# https://leetcode.com/problems/reverse-words-in-a-string-iii
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = ""
        for i in words:
            res += i[::-1]
            res += " "
        return res.strip()
/**
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;

    while (i >= 0 && j >= 0) {
        if (nums2[j] > nums1[i]) {
            nums1[k] = nums2[j];
            j--;
        } else {
            nums1[k] = nums1[i];
            i--;
        }
        k--;
    }
    while (j >= 0) {
        nums1[k] = nums2[j];
        j--;
        k--;
    }
};
# https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = len(nums1)-1
        while i>-1 and j >-1:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            elif nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                nums1[k]=nums1[i]
                k-=1
                nums1[k]=nums2[j]
                j-=1
                i-=1
                k-=1
        # print(nums1,nums2,i,j,k)
        if j>-1:
            for z in range(j,-1,-1):
                nums1[z]=nums2[j]
                j -= 1
        return
            
            
# https://leetcode.com/problems/domino-and-tromino-tiling
class Solution:
    def numTilings(self, n: int) -> int:
        count = 0
        if n<=2:
            return n
        dp = {}
        def ind(t1,t2):
            if t1 and t2:
                return 0
            if t1 and not t2:
                return 1
            if not t1 and t2:
                return 2
            if not t1 and not t2:
                return 3
        
        def solve(i,t1,t2):
            if i==n:
                return 1
            count = 0
            t3, t4 = i+1<n, i+1<n 
            if i in dp and dp[i][ind(t1,t2)] is not None:
                return dp[i][ind(t1,t2)]
            # t1 and t2 are available; means we can fill t1, t2 or t1,t2,t3 or t1,t2,t4
            if t1 and t2: count+=solve(i+1, True, True) 
            if t1 and t2 and t3 : count+=solve(i+1, True, False) 
            if t1 and t2 and t3 : count+=solve(i+1, False, True)
            if t1 and t2 and t3 : count+=solve(i+1, False, False)
            
            # t1 and t2 are filled - so move to next column
            if not t1 and not t2 : count+=solve(i+1,True, True)
            # t1 is available but t2 is not; means we can fill t1, t3 or t1,t3,t4
            if t1 and not t2 and t3 : count+=solve(i+1,False, True)
            if t1 and not t2 and t3 : count+=solve(i+1, False, False)
            # t1 is not available but t2 is; means we can fill t2, t4 or t2,t3,t4
            if not t1 and t2 and t3 : count+=solve(i+1,True,False)
            if not t1 and t2 and t3 : count+=solve(i+1,False,False)
            if i not in dp:
                dp[i] =[None]*4
            dp[i][ind(t1,t2)] = count
            return count
        
        count = solve(0,True, True)
        # print(dp)
        return count%(10**9+7)
            
# https://leetcode.com/problems/domino-and-tromino-tiling
class Solution:
    def numTilings(self, n: int) -> int:
        count = 0
        if n<=2:
            return n
        dp = {}
        def ind(t1,t2):
            if t1 and t2:
                return 0
            if t1 and not t2:
                return 1
            if not t1 and t2:
                return 2
            if not t1 and not t2:
                return 3
        
        def solve(i,t1,t2):
            if i==n:
                return 1
            count = 0
            t3, t4 = i+1<n, i+1<n 
            if i in dp and dp[i][ind(t1,t2)] is not None:
                return dp[i][ind(t1,t2)]
            # t1 and t2 are available; means we can fill t1, t2 or t1,t2,t3 or t1,t2,t4
            if t1 and t2: count+=solve(i+1, True, True) 
            if t1 and t2 and t3 : count+=solve(i+1, True, False) 
            if t1 and t2 and t3 : count+=solve(i+1, False, True)
            if t1 and t2 and t3 : count+=solve(i+1, False, False)
            
            # t1 and t2 are filled - so move to next column
            if not t1 and not t2 : count+=solve(i+1,True, True)
            # t1 is available but t2 is not; means we can fill t1, t3 or t1,t3,t4
            if t1 and not t2 and t3 : count+=solve(i+1,False, True)
            if t1 and not t2 and t3 : count+=solve(i+1, False, False)
            # t1 is not available but t2 is; means we can fill t2, t4 or t2,t3,t4
            if not t1 and t2 and t3 : count+=solve(i+1,True,False)
            if not t1 and t2 and t3 : count+=solve(i+1,False,False)
            if i not in dp:
                dp[i] =[None]*4
            dp[i][ind(t1,t2)] = count
            return count
        
        count = solve(0,True, True)
        # print(dp)
        return count%(10**9+7)
            
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found=[]
        def cd(node,path,target):
            nonlocal found
            if not node:
                return None
            if node.val==target.val:
                # print(path)
                path+=","+str(node.val)
                found.append(path.split(","))
                return node
            # print(path, target.val, node.val)
            lc = cd(node.left,path+","+str(node.val),target) if node.left else None
            rc = cd(node.right,path+","+str(node.val),target) if node.right else None
            return lc if lc else (rc if rc else None)
        prev = None
        t1 = cd(root,"",p)
        t2 = cd(root,"",q)
        t3 = None
        # print("**",found)
        if found and len(found)==2:
            for i in range(len(found[0])):  
                if i<len(found[1]) and found[0][i]==found[1][i]:
                    prev = found[0][i]
                else:
                    break
        if prev:
            t3 = cd(root,"",TreeNode(int(prev)))
        return t3
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found=[]
        def cd(node,path,target):
            nonlocal found
            if not node:
                return None
            if node.val==target.val:
                # print(path)
                path+=","+str(node.val)
                found.append(path.split(","))
                return node
            # print(path, target.val, node.val)
            lc = cd(node.left,path+","+str(node.val),target) if node.left else None
            rc = cd(node.right,path+","+str(node.val),target) if node.right else None
            return lc if lc else (rc if rc else None)
        prev = None
        t1 = cd(root,"",p)
        t2 = cd(root,"",q)
        t3 = None
        print("**",found)
        if found and len(found)==2:
            for i in range(len(found[0])):  
                if i<len(found[1]) and found[0][i]==found[1][i]:
                    prev = found[0][i]
                else:
                    break
        if prev:
            t3 = cd(root,"",TreeNode(int(prev)))
        return t3
# https://leetcode.com/problems/edit-distance
from copy import deepcopy
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # carrot
        # shred
        # t delete
        # o, r replace
        # c, a replace
        # pizza
        # pasta
        # i,z,z replace
        # sridhar
        # samrat
        # r replace 
        # h delete
        # rid replace
        # inen-tion
        # execution
        # free
        # reep
        # match length
        # common characters/sequences
        # minimal distance
        # ops = [None, None, None]
        # d = [ops for i in range(len(word2))]
        # d = [None]*len(word1)
        d = {}
        def dfs(n1,n2):
            if n1<len(word1) and n2<len(word2) and (n1,n2) in d:
                return d[(n1,n2)]
            while n2<len(word2) and n1<len(word1) and word1[n1]==word2[n2] :
                n1 += 1
                n2 += 1
            if (n1>=len(word1) and n2>=len(word2)):
                return 0
            elif n1>=len(word1) and n2<len(word2):
                return len(word2)-n2
            elif n1<len(word1) and n2>=len(word2):
                return len(word1)-n1
            c = 0
            # insert 
            c0 = dfs(n1,n2+1)+1
            # delete
            c1 = dfs(n1+1,n2)+1
            # replace
            c2 = dfs(n1+1,n2+1)+1
            d[(n1,n2)]=min(c0,c1,c2)
            return d[(n1,n2)]
            # return min(c0,c1,c2)
        return dfs(0,0)
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)
        return [True if i+extraCandies>=m else False for i in candies]
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        slow,fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next  
            fast = fast.next.next 
        slow.next = slow.next.next
        return head
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast, prev = head, head, None
        while fast.next:
            prev = slow
            slow = slow.next  
            fast = fast.next.next if fast.next.next else fast.next
        if prev:
            prev.next = slow.next 
            return head
        else:
            return None
# https://leetcode.com/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])-> int:
        # l = len(intervals)
        intervals.sort(reverse=True)
        mx = intervals[0]
        c = 0
        for i in intervals[1:]:
            if i[1] <= mx[0]:
                mx = i
            else:
                c+= 1
        return c

        # dp = {}
        # dp[l-1] = 1
        # def dfs(ind):
        #     if ind >= l:
        #         return 0
        #     if ind in dp:
        #         return dp[ind]
        #     c = 0
        #     for i in range(ind + 1, l):
        #         if intervals[i][0] >= intervals[ind][1] and dp[i] > c:
        #             c = dp[i]   
        #     dp[ind] = c + 1
        #     return dp[ind]
        # mn = 0
        # for i in range(l-1,-1,-1):
        #     curr = dfs(i)
        #     if curr > mn:
        #         mn = curr

        # return l - mn 
         
# https://leetcode.com/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])-> int:
        # l = len(intervals)
        intervals.sort(reverse=True)
        mx = intervals[0]
        c = 0
        for i in intervals[1:]:
            if i[1] <= mx[0]:
                mx = i
            else:
                c+= 1
        return c

        # dp = {}
        # dp[l-1] = 1
        # def dfs(ind):
        #     if ind >= l:
        #         return 0
        #     if ind in dp:
        #         return dp[ind]
        #     c = 0
        #     for i in range(ind + 1, l):
        #         if intervals[i][0] >= intervals[ind][1] and dp[i] > c:
        #             c = dp[i]   
        #     dp[ind] = c + 1
        #     return dp[ind]
        # mn = 0
        # for i in range(l-1,-1,-1):
        #     curr = dfs(i)
        #     if curr > mn:
        #         mn = curr

        # return l - mn 
         
/**
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    let a = {}
    if (deck.length<2){
        return false
    }

    deck.forEach((i)=> {
        if (Object.hasOwn(a,i)){
            a[i] = ++a[i];
        }
        else {
            a[i] = 1;
        }
    });
    console.log(a);
    function gcd(a, b) 
    { 
        if (a == 0) 
            return b; 
        return gcd(b % a, a); 
    } 

    let result = Object.values(a)[0]
    for (const [key, value] of Object.entries(a)) {
        result = gcd(value, result); 
        if(result == 1) 
        { 
        return false; 
        } 
    }

    // Object.values(a).forEach((i) => {
    //     if (i!=c){
    //         return false
    //     }
    //     else{
    //         console.log(i,c)
    //     }
    // });
    return true
};
/**
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    let a = {}
    if (deck.length<2){
        return false
    }

    deck.forEach((i)=> {
        if (Object.hasOwn(a,i)){
            a[i] = ++a[i];
        }
        else {
            a[i] = 1;
        }
    });
    function gcd(a, b) 
    { 
        if (a == 0) 
            return b; 
        return gcd(b % a, a); 
    } 

    let result = Object.values(a)[0]
    for (const [key, value] of Object.entries(a)) {
        result = gcd(value, result); 
        if(result == 1) 
        { 
        return false; 
        } 
    }

    // Object.values(a).forEach((i) => {
    //     if (i!=c){
    //         return false
    //     }
    //     else{
    //         console.log(i,c)
    //     }
    // });
    return true
};
/**
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    let a = {}
    if (deck.length<2){
        return false
    }

    deck.forEach((i)=> {
        if (Object.hasOwn(a,i)){
            a[i] = ++a[i];
        }
        else {
            a[i] = 1;
        }
    });
    function gcd(a, b) 
    { 
        if (a == 0) 
            return b; 
        return gcd(b % a, a); 
    } 

    let result = Object.values(a)[0]
    for (const [key, value] of Object.entries(a)) {
        result = gcd(value, result); 
        if(result == 1) 
        { 
        return false; 
        } 
    }

    // Object.values(a).forEach((i) => {
    //     if (i!=c){
    //         return false
    //     }
    //     else{
    //         console.log(i,c)
    //     }
    // });
    return true
};
# https://leetcode.com/problems/text-justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def jw(k,v):
            gaps = (k[1]-k[0])-1
            if gaps>0:
                sp = max(1,v//gaps)
                ex = v%gaps
                res = ""
                for i in range(k[0],k[1]-1):
                    res += words[i]+" "*(sp + (1 if ex>0 else 0))
                    ex -= 1
                    i += 1
                res += words[i]
                return res
            else:
                return words[k[0]]+" "*v
        fin=[]
        c,s = 0,0
        st = 0
        for i,w in enumerate(words):
            if c+s+len(w)>maxWidth:
                fin.append(jw((st,i),maxWidth-c))
                st = i
                c, s = 0,0
            c += len(w)
            s += 1
        if c: 
            x = (" ".join(i for i in words[st:]))
            fin+=[x+" "*(maxWidth-len(x))] 
        # print(r)
        return fin
# https://leetcode.com/problems/text-justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        fin={}
        c,s = 0,0
        st = 0
        for i,w in enumerate(words):
            if c+s+len(w)>maxWidth:
                fin[(st,i)]=(maxWidth-c)
                st = i
                c, s = 0,0
            c += len(w)
            s += 1
        r = []
        for k,v in fin.items():
            gaps = (k[1]-k[0])-1
            if gaps>0:
                sp = max(1,v//gaps)
                ex = v%gaps
                res = ""
                for i in range(k[0],k[1]-1):
                    res += words[i]+" "*(sp + (1 if ex>0 else 0))
                    ex -= 1
                    i += 1
                res += words[i]
                r += [res]
            else:
                r +=[words[k[0]]+" "*v]
            # print(r)
        if c: 
            x = (" ".join(i for i in words[st:]))
            r+=[x+" "*(maxWidth-len(x))] 
        # print(r)
        return r
# https://leetcode.com/problems/maximum-subsequence-score
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # Building a list of tuples to represent pairs
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        
        # Sorting pairs by the corresponding value in nums2
        pairs.sort(key = lambda pair : pair[1], reverse = True)

        minHeap = []
        n1Sum = 0
        result = 0 # max score

        for num1, num2 in pairs:
            n1Sum += num1
            heapq.heappush(minHeap, num1)

            if len(minHeap) > k:
                n1Sum -= heapq.heappop(minHeap)
            
            if len(minHeap) == k:
                result = max(result, n1Sum * num2)

        return result
# https://leetcode.com/problems/first-missing-positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while True:
            if i not in nums:
                break
            i += 1
        return i
        
# https://leetcode.com/problems/candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]: res[i]+=res[i-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]: res[i]=max(res[i],res[i+1]+1)
        return sum(res)
            
# https://leetcode.com/problems/implement-trie-prefix-tree
class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = {}
    

class Trie:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        word+=";"
        l = len(word)
        def dfs(node,x):
            if x==l:
                return 
            if word[x] not in node.children:
                node.children[word[x]]=Node(word[x])
            return dfs(node.children[word[x]],x+1)
        return dfs(self.trie,0)
        

    def search(self, word: str) -> bool:
        word+=";"
        l = len(word)
        def dfs(node,x):
            if x==l:
                return True
            if word[x] not in node.children:
                return False
            return dfs(node.children[word[x]],x+1)
        return dfs(self.trie,0)


    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        def dfs(node,x):
            if x==l:
                return True
            if prefix[x] not in node.children:
                return False
            return dfs(node.children[prefix[x]],x+1)
        return dfs(self.trie,0)
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l = len(digits)
        if l==0:
            return []
        # tail recursion
        def bt(curr_str,curr_digit,res):
            if len(curr_str)==l-1:
                for i in d[digits[curr_digit]]:
                    res += [curr_str+i]
                return res
            else:
                for i in d[digits[curr_digit]]:
                    res = bt(curr_str+i,curr_digit+1,res)
                return res
        return bt("",0,[])
        # 233
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l = len(digits)
        if l==0:
            return []
        def bt(curr_str,curr_digit):
            result = []
            if len(curr_str)==l-1:
                for i in d[digits[curr_digit]]:
                    result += [curr_str+i]
                return result
            else:
                for i in d[digits[curr_digit]]:
                    result += bt(curr_str+i,curr_digit+1)
                return result
        return bt("",0)
        # 233
# https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l



        
# https://leetcode.com/problems/determine-if-two-strings-are-close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 , w2 = {}, {}
        for i in word1:
            if i in w1:
                w1[i] += 1
            else:
                w1[i]=1
        for i in word2:
            if i in w2:
                w2[i] += 1
            else:
                w2[i]=1
        if set(w1.keys())!=set(w2.keys()):
            return False
        if sorted(w1.values())!=sorted(w2.values()):
            return False
        for i in w2:
            if w2[i] not in w1.values():
                return False
        return True
        
# https://leetcode.com/problems/determine-if-two-strings-are-close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 , w2 = {}, {}
        for i in word1:
            if i in w1:
                w1[i] += 1
            else:
                w1[i]=1
        for i in word2:
            if i in w2:
                w2[i] += 1
            else:
                w2[i]=1
        print(locals())
        if set(w1.keys())!=set(w2.keys()):
            return False
        if sorted(w1.values())!=sorted(w2.values()):
            return False
        for i in w2:
            if w2[i] not in w1.values():
                return False
        return True
        
# https://leetcode.com/problems/reverse-string
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l//2):
            s[i],s[l-1-i]=s[l-1-i],s[i]
            print( s[i],s[l-1-i])
# https://leetcode.com/problems/equal-row-and-column-pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
      cols = []
      for col_num in range(len(grid)):
        col = []
        for row in grid:
          col += [row[col_num]]
        cols += [col]
      pairs = 0
      for i in range(len(grid)):
        for j in grid:
          if j==cols[i]:
            pairs += 1
      return pairs
        
        
# https://leetcode.com/problems/equal-row-and-column-pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
      cols = []
      for col_num in range(len(grid)):
        col = []
        for row in grid:
          col += [row[col_num]]
        cols += [col]
      pairs = 0
      for i in range(len(grid)):
        for j in grid:
          if j==cols[i]:
            pairs += 1
      return pairs
        
        
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        c = 0
        points.sort(key=lambda x: x[1])
        # print(points)
        i, l = 1, len(points)
        s,m = points[0]
        while i<l:
            # print(m,c,points[i][1])
            if m<points[i][0]:
                m = points[i][1]
                c += 1
            i += 1
        return c+1
# https://leetcode.com/problems/number-of-islands
class Solution:
    def numIslands(self, grid: List[List[str]]):
        eq ={}
        s = set()
        h = 0
        i,j=0, 0
        x,y = len(grid), len(grid[0])
        def valid(k):
            p,q = k
            nonlocal s
            if 0<=p<x and 0<=q<y and grid[p][q]=="1" and (p,q) not in s:
                return True
            else:
                return False
        c = 0
        for a in range(x):
            for b in range(y):
                if valid((a,b)):
                    eq[h] = (a,b)
                    s.add(eq[h])
                    t = h+1
                    while h<len(eq):
                        (i,j) = eq[h]
                        s.add(eq[h])
                        for k in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                            if valid(k):
                                # print("valid",k,h,t,eq)
                                eq[t] = k
                                t += 1
                                grid[k[0]][k[1]] = 0
                            # else:
                            #     print("invalid",k)
                        h+=1
                    h = t
                    c += 1
        return c


                        
            
# https://leetcode.com/problems/min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)-3
        while l>=0:
            m = min(cost[l+1],cost[l+2])
            cost[l] += m
            l -= 1
        return min(cost[0],cost[1])

        
# https://leetcode.com/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        s = []
        res = [0]*l
        for ind, i in enumerate(temperatures):
            while s and s[-1][0]<i:
                p = s.pop()
                res[p[1]]=ind-p[1]
            s.append((i,ind))
       
        return res
# https://leetcode.com/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        s = []
        res = [0]*l
        for ind, i in enumerate(temperatures):
            while s and s[-1][0]<i:
                p = s.pop()
                res[p[1]]=ind-p[1]
            else:
                s.append((i,ind))
       
        return res
# https://leetcode.com/problems/squares-of-a-sorted-array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums)-1
        sq = [0]*len(nums)
        sqi=j
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                sq[sqi]=nums[j]**2
                j-=1
            else:
                sq[sqi]=nums[i]**2
                i+=1
            sqi-=1
        return sq
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze
from queue import Queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = Queue()
        q.put((entrance[0] , entrance[1] , 0))
        t = 0
        ans =[]
        maze[entrance[0]][entrance[1]] = "+"
 
        while(not q.empty()) :
            s = q.qsize()
            for i in range(s) :
                node = q.get() 
                # boundary conditions
                if node[0]==0 or node[0]==len(maze)-1 :
                    if node[2]!=0 :
                        return node[2]
                    ans += [node[2]]
                elif node[1] == 0 or node[1]==len(maze[0])-1 :
                    if node[2]!=0 :
                        return node[2]
                    ans += [node[2]]
                
                dx = [0 , -1 , 0 ,1 ]
                dy = [-1 , 0 , 1 , 0]

                for ind in range(4) :
                    x = node[0] + dx[ind]
                    y = node[1] + dy[ind] 
                    if x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]!="+" :
                        maze[x][y] = "+"
                        q.put((x,y,node[2]+1))

        if len(ans) == 0:
            return -1 
    
        return -1 if max(ans)==0 else max(ans) 
# https://leetcode.com/problems/insert-delete-getrandom-o1
class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val in self.s: return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s: return False
        self.s.remove(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# https://leetcode.com/problems/insert-delete-getrandom-o1
class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val in self.s: return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s: return False
        self.s.remove(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# https://leetcode.com/problems/length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if c: break
            else:
                c += 1
        return c
# https://leetcode.com/problems/length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        w = False
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if w: break
            else:
                c += 1
                w = True
        return c
# https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0,1,1]

        for i in range(3,n+1):
            d.append(d[i-1]+d[i-2]+d[i-3])
        return d[n]
# https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        d = {0:0,1:1,2:1}

        for i in range(3,n+1):
            d[i] = d[i-1]+d[i-2]+d[i-3]
        return d[n]
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        key_dict = {needle[i]:i for i in range(len(needle))}
        print(key_dict)
        ph, pn = len(needle)-1,len(needle)-1
        
        while ph<len(haystack):
            # print(f"haystack {haystack} at {ph} {haystack[ph]} needle {needle} at {pn} {needle[pn]}")
            if haystack[ph] == needle[pn]:
                if pn==0:
                    return ph
                ph -= 1
                pn -= 1
            else:
                if haystack[ph] in key_dict:
                    ph += len(needle) - min(key_dict[haystack[ph]]+1,pn)
                else:
                    ph += len(needle)
                pn = len(needle) -1
        if pn==-1:
            return ph+1
        else:
            return -1
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        key_dict = {needle[i]:i for i in range(len(needle))}
        print(key_dict)
        ph, pn = len(needle)-1,len(needle)-1
        
        while ph<len(haystack):
            print(f"haystack {haystack} at {ph} {haystack[ph]} needle {needle} at {pn} {needle[pn]}")
            if haystack[ph] == needle[pn]:
                if pn==0:
                    return ph
                ph -= 1
                pn -= 1
            else:
                if haystack[ph] in key_dict:
                    ph += len(needle) - min(key_dict[haystack[ph]]+1,pn)
                else:
                    ph += len(needle)
                pn = len(needle) -1
        if pn==-1:
            return ph+1
        else:
            return -1
# https://leetcode.com/problems/jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:

        l=len(nums)
        mins = [1]*l
        mins[-1]=0
        for i in range(l-2,-1,-1):
            if nums[i]==0: 
                mins[i]=0
                continue
            if nums[i]+i>=l-1: continue
            var = [mins[j] for j in range(i+1,i+nums[i]+1) if mins[j]!=0]
            if  var : mins[i]=1+min(var) 
            else: mins[i]=0
        return mins[0]
   
# https://leetcode.com/problems/jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:

        l=len(nums)
        mins = [1]*l
        mins[-1]=0
        for i in range(l-2,-1,-1):
            if nums[i]==0: 
                mins[i]=0
                continue
            if nums[i]+i>=l-1: continue
            var = [mins[j] for j in range(i+1,i+nums[i]+1) if mins[j]!=0]
            if  var : mins[i]=1+min(var) 
            else: mins[i]=0
        print(mins)
        return mins[0]
   
# https://leetcode.com/problems/guess-number-higher-or-lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int,) -> int:
        l, r = 0, n
        while l<=r:
            i = (l+r)//2
            g = guess(i)
            if g == -1:
                r = i
            elif g == 1:
                l = i+1
            else:
                return i
        return 1
        
# https://leetcode.com/problems/running-sum-of-1d-array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        for i,j in enumerate(nums):
            prev += j
            nums[i] = prev
        return nums
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pprint import pprint
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        l = 1
        oh = head
        prev = head
        if prev.next is None and i<n:
            return None
        
        while prev.next is not None:
            l += 1
            prev = prev.next
    
        prev, next_node = head, head.next
        target = l - n -1
        if target == -1:
            return head.next
    
        while prev.next and next_node.next and i<target:
            prev, next_node =  next_node, next_node.next
            i += 1
    
        prev.next = next_node.next
        return oh
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pprint import pprint
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        l = 1
        oh = head
        prev, next_node = head, head.next
        if prev.next is None and i<n:
            return None
        
        while prev.next is not None:
            l += 1
            prev = prev.next
    
        prev, next_node = head, head.next
        target = l - n -1
        if target == -1:
            return head.next
    
        while prev.next and next_node.next and i<target:
            # print("*****************")
            # pprint(locals())
            prev, next_node =  next_node, next_node.next
            i += 1
        #     pprint(locals())
        # print("*****************")
        # pprint(prev)
    
        prev.next = next_node.next
        return oh
# https://leetcode.com/problems/asteroid-collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i, item in enumerate(asteroids):
            # print(locals())
            if item>0:
                st = [item]+st
            else:
                if st==[] or st[0]<0:
                    st = [item]+st
                    continue
                while st:
                    if st[0]<0:
                        st = [item]+st
                        break
                    if st[0]==abs(item):
                        st = st[1:]
                        break
                    elif st[0]<abs(item):
                        st = st[1:]
                    else:
                        break
                else:
                    st = [item]
        return st[::-1]
