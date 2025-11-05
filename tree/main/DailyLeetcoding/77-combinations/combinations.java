import java.util.*;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();

        // Start DFS for each index (like your Python version)
        for (int i = 0; i < n; i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(i + 1);
            dfs(i, n, k, cur, res);
        }

        return res;
    }

    private void dfs(int index, int n, int k, List<Integer> cur, List<List<Integer>> res) {
        // base case
        if (cur.size() == k) {
            res.add(new ArrayList<>(cur));
            return;
        }

        if (index >= n) return;

        // recursive calls
        for (int i = index + 1; i < n; i++) {
            List<Integer> next = new ArrayList<>(cur);
            next.add(i + 1);
            dfs(i, n, k, next, res);
        }
    }
}
