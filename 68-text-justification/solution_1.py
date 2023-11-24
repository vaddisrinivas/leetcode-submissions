# https://leetcode.com/problems/text-justification
# https://leetcode.com/problems/68-text-justification
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