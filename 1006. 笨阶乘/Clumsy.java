package leetcode;

public class Clumsy {
    public int clumsy(int N) {
        int ret = 0;
        int loopCnt = 0;
        int tmp = 0;
        while (N > 0) {
            loopCnt++;
            if (loopCnt % 4 == 1) {
                tmp = (loopCnt / 4 > 0) ? -N : N;
            } else if (loopCnt % 4 == 2) {
                tmp *= N;
            } else if (loopCnt % 4 == 3) {
                tmp /= N;
                ret += tmp;
                tmp = 0;
            } else if (loopCnt % 4 == 0) {
                ret += N;
            }
            N--;
        }
        if (tmp != 0) {
            ret += tmp;
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(new Clumsy().clumsy(10));
    }
}
