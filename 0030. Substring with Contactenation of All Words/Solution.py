class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        word_dict = {}
        for word in words:
            if word_dict.get(word) is None:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

        word_count = len(words)
        if word_count == 0:
            return res

        word_len = len(words[0])
        total_len = word_count * word_len
        for i in range(len(s) - word_count * word_len + 1):
            temp_word_dict = {}
            sub_str = s[i:i+total_len]
            j = 0
            for j in range(word_count):
                ok = True
                sub_word = sub_str[j * word_len:(j + 1) * word_len]
                if word_dict.get(sub_word) is None:
                    ok = False
                    break
                else:
                    if temp_word_dict.get(sub_word) is None:
                        temp_word_dict[sub_word] = 1
                    else:
                        temp_word_dict[sub_word] += 1
                    if temp_word_dict[sub_word] > word_dict[sub_word]:
                        ok = False
                        break
            if ok:
                res.append(i)
        return res


s = Solution()
print(s.findSubstring("", []))



