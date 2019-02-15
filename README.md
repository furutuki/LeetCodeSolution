

### 0003.  Longest Substring Without Repeating Characters ###

记录子串的开始位置start\_index，往后遍历子串尾部tail\_index，用set记录子串字符。


- 发现有重复字符出现，计算此时set的长度，并和当前最大长度比较并更新。更新start\_index为第一个重复字符后一个位置，直到结尾。

    
- 如果不是重复字符，添加到set中。

### 0004. Median of Two Sorted Arrays ###
连个有序整数list归并排序成一个新list，再计算中位数

### 0005. Longest Palindromic Substring ###
利用动态规划，假设matrix[i][j]表示子字符串substring(i, j)是否是回文，遍历一遍就可以。

### 0007. Reverse Integer ###
int转成字符串再反转，再判断下正负以及是否在signed int32范围内就可以

### 0008. String to Integer (atoi) ###
直接遍历一遍即可

### 0012. Integer to Roman ###
利用list从大到小存储roman integer和字母的对应关系，不断取数字的商和余数即可

### 0013. Roman to Integer ###
直接利用字典数据结构就可以

### 0014. Longest Common Prefix ###
遍历一遍字符串数组，不断更新最长前缀即可。也可以使用trie树来计算。   
