package leetcode;

import java.util.Arrays;

public class MyHashSet {

    private int[] data = new int[31251];

    /** Initialize your data structure here. */
    public MyHashSet() {
        Arrays.fill(data, 0);
    }

    public void add(int key) {
        setKey(key, true);
    }

    public void remove(int key) {
        setKey(key, false);
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return getKey(key);
    }

    private void setKey(int key, boolean add) {
        int index = key >> 5; // key / 32
        int subIndex = key & 31; // key % 32
        if (add) {
            data[index] |= 1 << subIndex;
        } else {
            data[index] &= (~(1 << subIndex));
        }
    }

    private boolean getKey(int key) {
        int index = key >> 5; // key / 32
        int subIndex = key & 31; // key % 32
        return (data[index] >> subIndex & 1) == 1;
    }

}
