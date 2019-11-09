

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

[0023. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)  
K路归并数组  
解法：利用优先队列直接存放所有的数组元素  
大坑：使用python3在本地运行ok，提交代码一直报错"TypeError '<' not supported between instances of 'ListNode' and 'ListNode'"     
原因是网站提供的ListNode的定义没有__lt__方法
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
```
而我在本地运行时ListNode的定义里给加了__lt__()的实现，然后网站测试代码里定义却没有这个方法。
为了规避这个问题，使用一个wrapper类包住提供的ListNode对象即可：
```
class Wrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
```
[代码](https://github.com/furutuki/LeetCodeSolution/tree/master/0023.%20Merge%20K%20Sorted%20Lists)


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

### 0039. Combination Sum ###
解法：回溯  
先排序，然后做dfs搜索即可  

### 0040. Combination Sum II ###
解法：回溯。  
和problem 0039的区别时每个元素只能用一次，只要在递归时下标参数+1跳过当前item即可

### 0041. First Missing Positive ###
解法：排序再遍历

### 0042. Trapping Rain Water ###
计算一堆长方体围成的水域的面积  
解法一：不断地找围起来的能够存放水的子区间，然后累加水域面积。针对子区间左右边界的确定，如下计算：
- 左边界：找递增的长方体直到下一个相邻变矮，此最高长方体为左边界  
- 有边界：从左边界后边第二个开始遍历，如果当前高度大于等于左边界高度，那么这个就是要找的右边界限。否则看看它是否是当前遍历过的长方体中最高的一个，如果是记录其下标。这样最终得到的最高的那根长方体的下标就是右边界。

解法二：双指针法。从左右往中间遍历，在比较挨矮的那边一致记录最高的高度，然后累加当前高度和最高高度之间的差即可

### 0046. Permutations ###
求全排列  
解法：DFS

[0048. Rotate Image](https://leetcode.com/problems/rotate-image/)  
顺时针旋转矩阵90度  
解法：以对角线为分界线，遍历矩阵对角线一边的每个元素，顺时针放到下一个位置即可。  
[代码](https://github.com/furutuki/LeetCodeSolution/tree/master/0048.%20Rotate%20Image)  

[0049. Group Anagrams](https://leetcode.com/problems/group-anagrams/)  
将一组单词按照含有相同字母的方式分类
解法一：对每个单词排序，再对单词列表排序，遍历。  
[代码](https://github.com/furutuki/LeetCodeSolution/blob/master/0049.%20Group%20Anagrams/Solution.py)

解法二：遍历列表每个单词，对每个单词的字母排序，以排序后的单词为key，将排序前的单词座位value添加到字典中。遍历完成后输出字典的values即可。
[代码](https://github.com/furutuki/LeetCodeSolution/blob/master/0049.%20Group%20Anagrams/Solution2.py)
