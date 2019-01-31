package com.leetcode.solution;

import java.util.HashMap;

public class Solution {
	
    public int[] twoSum(int[] nums, int target) {
    	
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
        	map.put(nums[i], i);
        }
        
        for (int i = 0; i < nums.length; i++) {
        	if (map.containsKey(target - nums[i]) && map.get(target - nums[i]) != i) {
        		result[0] = i;
        		result[1] = map.get(target - nums[i]);
        		break;
        	}
        }
        
    	return result; 
    }
    
    public static void main(String args[]) {
    	int[] array = new int[] {2, 7, 11, 15};
    	Solution solution = new Solution();
    	int[] result = solution.twoSum(array, 9);
    	System.out.println(result[0] + " " + result[1]);
    	
    	int[] array2 = new int[] {3, 2, 4};
    	result = solution.twoSum(array2, 6);
    	System.out.println(result[0] + " " + result[1]);
    }
}
