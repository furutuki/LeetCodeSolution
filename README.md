

### [0003.  Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ###

[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0003.%20Longest%20Substring%20Without%20Repeating%20Characters/Solution.py):  
记录子串的开始位置start\_index，往后遍历子串尾部tail\_index，用set记录子串字符。


- 发现有重复字符出现，计算此时set的长度，并和当前最大长度比较并更新。更新start\_index为第一个重复字符后一个位置，直到结尾。

    
- 如果不是重复字符，添加到set中。

### [0004. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0004.%20Median%20of%20Two%20Sorted%20Arrays/Solution.py): 连个有序整数list归并排序成一个新list，再计算中位数

### [0005. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0005.%20Longest%20Palindromic%20Substring/Solution.py): 利用动态规划，假设matrix[i][j]表示子字符串substring(i, j)是否是回文，遍历一遍就可以。

### [0007. Reverse Integer](https://leetcode.com/problems/reverse-integer) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0007.%20Reverse%20Integer/Solution.py): int转成字符串再反转，再判断下正负以及是否在signed int32范围内就可以

### [0008. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0008.%20String%20to%20Integer%20(atoi)/Solution.py): 直接遍历一遍即可

### [0012. Integer to Roman](https://leetcode.com/problems/integer-to-roman) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0012.%20Integer%20to%20Roman/Solution.py): 利用list从大到小存储roman integer和字母的对应关系，不断取数字的商和余数即可

### [0013. Roman to Integer](https://leetcode.com/problems/roman-to-integer) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0013.%20Roman%20to%20Integer/Solution.py): 直接利用字典数据结构就可以

### [0014. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0014.%20Longest%20Common%20Prefix/Solution.py): 遍历一遍字符串数组，不断更新最长前缀即可。也可以使用trie树来计算。   


### [0022. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) ###
[解法](https://github.com/furutuki/LeetCodeSolution/tree/master/0022.%20Generate%20Parentheses):  
为了保证和题目描述的顺序一致，使用dfs遍历即可。如果不要求顺序DP，BFS都可以。

### [0023. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) ###  
K路归并数组  
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0023.%20Merge%20K%20Sorted%20Lists/Solution.py)：利用优先队列直接存放所有的数组元素  
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

### [0033. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0033.%20Search%20in%20Rotated%20Sorted%20Array/Solution.py)：二分法。  
先看中间点是不是符合条件，是直接返回中间点索引，否则逻辑如下：  
- 如果左半有序  
（1）目标在左半，那么继续递归搜索左半  
（2）目标不在左半，继续搜索右半

- 如果右半有序  
（1）目标在右半，那么继续递归搜索右半  
- 返回不存在  


### [0034. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ###
[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0034.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/Solution.py)：二分查找法（循环实现）    
一旦找到target，分别向前、向后搜索等于target的数，得到坐标范围。（如果数组元素都是一样，要找的target也是这个数，那么算法复杂度退化到了O(n))  

[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0034.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array/Solution2.py)：二分递归查找  
针对中点两边分别递归搜索得到结果l、r。合并l、r的结果。具体如下：  
如果l、r中含有-1，说明至少有一半不存在target，那么在l、r这2个结果中取大的即可
如果l、r中不含-1，说明target正好跨越了中点mid，那么取l的左侧坐标和r的右侧坐标，得到的区间就是结果


### [0035. Search Insert Position](https://leetcode.com/problems/search-insert-position/) ###
[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0035.%20Search%20Insert%20Position/Solution.py)：暴力搜索（遍历）  
[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0035.%20Search%20Insert%20Position/Solution2.py)：二分查找法

###[0036. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)  ###
[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0036.%20Valid%20Sudoku/Solution.py)：暴力，按行、列，九宫格分别遍历一遍  
[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0036.%20Valid%20Sudoku/Solution2.py)：优化后的暴力（针对每个元素只遍历一次，在循环中针对三种情况进行判断）  

========== 一个python的坑 ============  
写法一：  
```
t = [{}] * 4  
t[2]["hello"] = "s"  
print(t)  
```
 输出结果：  
```
 [{'hello': 's'}, {'hello': 's'}, {'hello': 's'}, {'hello': 's'}] 
```
 和预期的不一样
  
写法二：
```
  
 t = [{},{},{},{}]  
 t[2]["hello"] = "s"  
 print(t)  
 ```

 输出结果：
 ```
[{}, {}, {'hello': 's'}, {}]  
```


### [0037. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)  ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0037.%20Sudoku%20Solver/Solution.py)：  
回溯

### [0039. Combination Sum](https://leetcode.com/problems/combination-sum/)  ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0039.%20Combination%20Sum/Solution.py)：  
回溯。 
先排序，然后做dfs搜索即可  

### [0040. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)  ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0040.%20Combination%20Sum%20II/Solution.py)：  
回溯。    
和problem 0039的区别时每个元素只能用一次，只要在递归时下标参数+1跳过当前item即可

### [0041. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)  ###
给定一个无序数组，找出最小的缺失的数  

[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0041.%20First%20Missing%20Positive/Solution.py)：  
排序再遍历

### [0042. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)  ###
计算一堆长方体围成的水域的面积  

[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0042.%20Trapping%20Rain%20Water/Solution.py)：  
不断地找围起来的能够存放水的子区间，然后累加水域面积。针对子区间左右边界的确定，如下计算：
- 左边界：找递增的长方体直到下一个相邻变矮，此最高长方体为左边界  
- 有边界：从左边界后边第二个开始遍历，如果当前高度大于等于左边界高度，那么这个就是要找的右边界限。否则看看它是否是当前遍历过的长方体中最高的一个，如果是记录其下标。这样最终得到的最高的那根长方体的下标就是右边界。

[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0042.%20Trapping%20Rain%20Water/Solution2.py)：  
双指针法。从左右往中间遍历，在比较挨矮的那边一致记录最高的高度，然后累加当前高度和最高高度之间的差即可

### [0046. Permutations](https://leetcode.com/problems/permutations/)  ###
求全排列  
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0046.%20Permutations/Solution.py): DFS

### [0048. Rotate Image](https://leetcode.com/problems/rotate-image/)  ###
顺时针旋转矩阵90度  
[解法](https://github.com/furutuki/LeetCodeSolution/tree/master/0048.%20Rotate%20Image)  ：以对角线为分界线，遍历矩阵对角线一边的每个元素，顺时针放到下一个位置即可。  

### [0049. Group Anagrams](https://leetcode.com/problems/group-anagrams/) ### 
将一组单词按照含有相同字母的方式分类  

[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0049.%20Group%20Anagrams/Solution.py)：对每个单词排序，再对单词列表排序，遍历。  

[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0049.%20Group%20Anagrams/Solution2.py)：遍历列表每个单词，对每个单词的字母排序，以排序后的单词为key，将排序前的单词座位value添加到字典中。遍历完成后输出字典的values即可。  

### [0053. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) ###
[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0053.%20Maximum%20Subarray/Solution.py): DP  
假设dp[i]代表[0, i]范围内以i结尾的子区间的最大的和。初始状态：  
```
dp[0] = nums[0]
```
子问题分解：   
- 如果 nums[i] > 0，那么dp[i] = dp[i - 1] + nums[i]；   
- 否则 dp[i] = nums[i]。也即：  
```
dp[i] = max(dp[i - 1] + nums[i], nums[i])
```


### [0055. Jump Game](https://leetcode.com/problems/jump-game/)  ###
一个整形数组nums，长度为len，初始位于index=0的位置，可以移动[1, numS[index]]步，问nums[len - 1是否可达。

一共用了3种方案，前两种超时（TLE）了，最后一个AC。

[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0055.%20Jump%20Game/Solution.py)：BFS。加入当前位于index=i处，将[index + 1， index + nums[index]]范围内的数都加到队列中，一旦len-1被加到队列，证明可达

[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0055.%20Jump%20Game/Solution2.py)：DP。dp[i]代表从index=i处是否可达nums[len-1]

[解法三](https://github.com/furutuki/LeetCodeSolution/blob/master/0055.%20Jump%20Game/Solution3.py)：DP。dp[i]代表从index=0处是否可达index=i处


### [0078. Subsets](https://leetcode.com/problems/subsets/)  ###
给定一个list，求其中元素的全组合  

[解法](https://github.com/furutuki/LeetCodeSolution/blob/master/0078.%20Subsets/Solution.py)：DFS  
当前结果集中每个list，都添加当前遍历的item做为新的list，添加到结果集。另外当前遍历的item单独成为一个list添加到结果集。最后把空集合[]添加到结果集  

### [0136. Single Number](https://leetcode.com/problems/single-number/)  ###
数组中元素除了一个元素，其他都是出现两次，找出那个只出现一次的元素  

[解法一](https://github.com/furutuki/LeetCodeSolution/blob/master/0136.%20Single%20Number/Solution.py)：对数组排序，遍历一遍即可  


[解法二](https://github.com/furutuki/LeetCodeSolution/blob/master/0136.%20Single%20Number/Solution2.py)：因为只有1个元素出现1次，其他都是2次，充分利用这个特点，对愿数组去重求和*2，再减去愿数组各元素累加之和即可。  

 
[解法三](https://github.com/furutuki/LeetCodeSolution/blob/master/0136.%20Single%20Number/Solution3.py)：所有元素做异或操作即可。 
