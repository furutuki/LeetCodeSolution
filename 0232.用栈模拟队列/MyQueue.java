import java.util.Stack;

class MyQueue {

    Stack<Integer> stack;
    Stack<Integer> stack2;
    /** Initialize your data structure here. */
    public MyQueue() {
        stack = new Stack<>();
        stack2 = new Stack<>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        stack.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (!stack2.empty()) {
            return stack2.pop();
        }
        while (!stack.empty()) {
            stack2.push(stack.pop());
        }
        return stack2.pop();
    }

    /** Get the front element. */
    public int peek() {
        if (!stack2.empty()) {
            return stack2.peek();
        }
        while (!stack.empty()) {
            stack2.push(stack.pop());
        }
        return stack2.peek();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.empty() && stack2.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */