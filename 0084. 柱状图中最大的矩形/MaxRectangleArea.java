import java.util.Stack;

public class MaxRectangleArea {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        // 末尾加个0强制弹出stack里的元素进行计算
        int[] h = new int[heights.length + 1];
        System.arraycopy(heights, 0, h, 0, heights.length);
        int maxArea = 0;
        for (int i = 0; i < h.length; i++) {
            while (!stack.isEmpty() && h[i] < h[stack.peek()]) {
                int top = stack.peek();
                stack.pop();
                maxArea = Math.max(maxArea, h[top] * (stack.isEmpty() ? i : (i - stack.peek() - 1)));
            }
            stack.push(i);
        }
        return maxArea;
    }
}