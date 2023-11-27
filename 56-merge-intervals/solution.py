class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        st = [intervals[0]]
        for i in intervals[1:]:
            p = st[-1]
            if i[0]>p[1]: st.append(i)
            else:
                st[-1]=(min(p[0],i[0]),max(i[1],p[1]))
        return st