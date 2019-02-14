# LeetCodeSolution



### 0003.  Longest Substring Without Repeating Characters ###

记录子串的开始位置start\_index，往后遍历子串尾部tail\_index，用set记录子串字符。


- 发现有重复字符出现，计算此时set的长度，并和当前最大长度比较并更新。更新start\_index为第一个重复字符后一个位置，直到结尾。

    
- 如果不是重复字符，添加到set中。
