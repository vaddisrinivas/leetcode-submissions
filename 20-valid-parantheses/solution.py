class Solution:
    def isValid(self, s: str) -> bool:
        if s=="": return True
        d = {')':'(', '}':'{', ']':'['}
        st = []
        for i in s:
            if st and i in d and st[-1]==d[i]:
                st.pop()
            else:
                st.append(i)
        return st==[]