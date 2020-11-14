public class RelativeSortArray {

    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] bucket = new int[1001];
        for (int value : arr1) {
            bucket[value]++;
        }

        int idx = 0;
        for (int value : arr2) {
            while (bucket[value] > 0) {
                arr1[idx++] = value;
                bucket[value]--;
            }
        }

        for (int i = 0; i < bucket.length; i++) {
            while (bucket[i] > 0) {
                arr1[idx++] = i;
                bucket[i]--;
            }
        }

        return arr1;
    }

}
