

### 0003.  Longest Substring Without Repeating Characters ###

记录子串的开始位置start\_index，往后遍历子串尾部tail\_index，用set记录子串字符。


- 发现有重复字符出现，计算此时set的长度，并和当前最大长度比较并更新。更新start\_index为第一个重复字符后一个位置，直到结尾。

    
- 如果不是重复字符，添加到set中。

### 0004. Median of Two Sorted Arrays ###

连个有序整数list归并排序成一个新list，再计算中位数

### 0007. Reverse Integer ###

int转成字符串再反转，再判断下正负以及是否在signed int32范围内就可以
