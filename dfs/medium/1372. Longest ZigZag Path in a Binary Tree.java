// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int res = 0;

    public int longestZigZag(TreeNode root) {
        dfs(root.left, 1, 'L');
        dfs(root.right, 1, 'R');
        return res;
    }

    public void dfs(TreeNode node, int path, char dir) {
        if (node == null) return;
        res = Math.max(res, path);
        if (dir == 'L') {
            dfs(node.right, path + 1, 'R');
            dfs(node.left, 1, 'L');
        } else {
            dfs(node.left, path + 1, 'L');
            dfs(node.right, 1, 'R');
        }        
    }
}