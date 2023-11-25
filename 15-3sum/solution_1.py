class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==3: return [] if sum(nums) else [nums]
        c = Counter(nums)
        res = set()
        k = list(c.keys())
        k.sort()
        i,j,l = 0,0,len(k)
        if l==1: return [] if sum(nums) else [[0]*3]
        while j<l:
            d = -(k[i]+k[j])
            if d in c:
                if((i!=j) or (i==j and c[k[i]]>1)):
                    c[k[i]]-=1
                    c[k[j]]-=1
                    if c[d]!=0:
                        res.add(tuple(sorted([k[i],k[j],d])))
                    c[k[i]]+=1
                    c[k[j]]+=1
            j+=1
            if j==l-1:
                i,j=i+1,i+1
        return res