import kotlin.math.max
import kotlin.math.min

class Solution {
    fun partitionDisjoint(nums: IntArray): Int {
        val minRight = IntArray(nums.size)
        var min = Int.MAX_VALUE
        for (i in nums.size - 1 downTo 0) {
            minRight[i] = min(min, nums[i])
            min = minRight[i]
        }
        var max = Int.MIN_VALUE
        for (i in nums.indices) {
            max = max(max, nums[i])
            if (max <= minRight[i + 1]) {
                return i + 1
            }
        }

        return 0
    }
}

fun main(argc: Array<String>) {
    println(Solution().partitionDisjoint(intArrayOf(5,0,3,8,6)))
    println(Solution().partitionDisjoint(intArrayOf(1, 1, 1, 0, 6, 12)))
}