class Solution:
    def countAndSay(self, n: int) -> str:
        curval = ['1']
        for i in range(n - 1):
            s = curval
            curval=[]
            j = 0
            while j < len(s):
                count = 1
                k = j + 1
                while k < len(s):
                    if s[k] == s[j]:
                        count += 1
                        k += 1
                        pass
                    else:
                        break
                curval.append(str(count))
                curval.append(s[j])
                j = k

        return ''.join(t)


s = Solution()
t = s.countAndSay(5)
print(t)
