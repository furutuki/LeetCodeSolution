

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


### 0022. Generate Parentheses ###
为了保证和题目描述的顺序一致，使用dfs遍历即可。如果不要求顺序DP，BFS都可以。

### 0033. Search in Rotated Sorted Array ###
二分法。  
先看中间点是不是符合条件，是直接返回中间点索引，否则逻辑如下：  
- 如果左半有序  
（1）目标在左半，那么继续递归搜索左半  
（2）目标不在左半，继续搜索右半

- 如果右半有序  
（1）目标在右半，那么继续递归搜索右半  
- 返回不存在  


### 00334. Find First and Last Position of Element in Sorted Array ###
解法一：二分查找法（循环实现）  
一旦找到target，分别向前、向后搜索等于target的数，得到坐标范围。（如果数组元素都是一样，要找的target也是这个数，那么算法复杂度退化到了O(n))  

解法二：二分递归查找  
针对中点两边分别递归搜索得到结果l、r。合并l、r的结果。具体如下：  
如果l、r中含有-1，说明至少有一半不存在target，那么在l、r这2个结果中取大的即可
如果l、r中不含-1，说明target正好跨越了中点mid，那么取l的左侧坐标和r的右侧坐标，得到的区间就是结果


### 0035. Search Insert Position ###
解法一：暴力搜索（遍历）  
解法二：二分查找法

### 0036. Valid Sudoku ###
解法一：暴力，按行、列，九宫格分别遍历一遍  
解法二：优化后的暴力（针对每个元素只遍历一次，在循环中针对三种情况进行判断）  

========== 一个python的坑 ============  
写法一：  
t = [{}] * 4  
t[2]["hello"] = "s"  
print(t)  

 输出结果：  
 [{'hello': 's'}, {'hello': 's'}, {'hello': 's'}, {'hello': 's'}] 
  
 和预期的不一样
  
写法二：  
 t = [{},{},{},{}]  
 t[2]["hello"] = "s"  
 print(t)  
 
 输出结果：  
[{}, {}, {'hello': 's'}, {}]  


===================================== 

### 0037. Sudoku Solver ###
解法：回溯
