import java.util.ArrayList;
import java.util.List;

public class SplitPalindrome {

    private boolean isPalindrome(String s) {
        if (s ==null || s.length() == 0) {
            return false;
        }
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    private void backtrace(String s, int startIndex, List<List<String>> ans, List<String> tmp) {
        if (startIndex >= s.length()) {
            if (tmp.size() > 0) {
                ans.add(new ArrayList<>(tmp));
            }
            return;
        }

        for (int length = 1; length <= s.length() - startIndex; length++) {
            String subString = s.substring(startIndex, startIndex + length);
            if (isPalindrome(subString)) {
                tmp.add(subString);
                backtrace(s, startIndex + length, ans, tmp);
                tmp.remove(tmp.size() - 1);
            }
        }
    }

    public List<List<String>> partition(String s) {
        List<String> tmp = new ArrayList<>();
        List<List<String>> ans = new ArrayList<>();
        backtrace(s, 0, ans, tmp);
        return ans;
    }

    public static void main(String[] argv) {
        SplitPalindrome s = new SplitPalindrome();
        List<List<String>> ans = s.partition("aab");
        for (int i = 0; i < ans.size(); i++) {
            for (int j = 0; j < ans.get(i).size(); j++) {
                System.out.print(ans.get(i).get(j) + "  ");
            }
            System.out.println();
        }
    }

}
