class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:return [newInterval]
        st,q = [intervals[0]],1
        if newInterval[0]<intervals[0][0]:  
            st=[newInterval]
            q = 0
        def deal(i,p):
            if i[0]>p[1]: st.append(i)
            else:
                st[-1]=(min(p[0],i[0]),max(i[1],p[1]))
            
        for i in intervals[q:]:
            if i[0]>newInterval[0]:
                i,newInterval = newInterval,i
            deal(i,st[-1])
        i = newInterval
        deal(i,st[-1])
        return st