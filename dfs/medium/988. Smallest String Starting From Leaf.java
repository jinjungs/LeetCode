/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// DFS (recommended)
class Solution {
    String answer = null;

    public String smallestFromLeaf(TreeNode root) {
        dfs(root, new StringBuilder());
        return answer;
    }

    public void dfs(TreeNode node, StringBuilder path) {
        if (node == null) return;
        path.append((char) (node.val + 'a'));

        if (node.left == null && node.right == null) {
            String candidate = path.reverse().toString();
            path.reverse(); // restore

            if (answer == null || candidate.compareTo(answer) < 0) {
                answer = candidate;
            }
        }

        dfs(node.left, path);
        dfs(node.right, path);

        // backTrack
        path.deleteCharAt(path.length() -1);
    }
  
}


// BFS (not recommended)
public class Value {
    TreeNode node;
    List<Integer> path; 

    Value() {}
    Value(TreeNode node, List<Integer> path) {
        this.node = node;
        this.path = path;
    }
}

class Solution {
    public String smallestFromLeaf(TreeNode root) {
        if (root == null) return "";

        // BFS
        Queue<Value> q = new ArrayDeque<>();
        q.offer(new Value(root, new ArrayList<>()));

        List<Integer> res = null;

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {

                Value value = q.poll();
                TreeNode node = value.node;
                List<Integer> path = value.path;

                path.add(node.val);

                // leaf
                if (node.left == null && node.right == null) {
                    if (res == null) {
                        res = path;
                    } else {
                        if (isSmaller(path, res)) {
                            res = path;
                        }
                    }
                }

                if (node.left != null) {
                    q.offer(new Value(node.left, new ArrayList<>(path)));
                }

                if (node.right != null) {
                    q.offer(new Value(node.right, new ArrayList<>(path)));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = res.size() - 1; i >= 0; i--) {
            sb.append((char) (res.get(i) + 'a'));
        }
        
        return sb.toString();
    }

    private boolean isSmaller(List<Integer> a, List<Integer> b) {
        int i = a.size() - 1;
        int j = b.size() - 1;

        while (i >= 0 && j >= 0) {
            if (!a.get(i).equals(b.get(j))) {
                return a.get(i) < b.get(j);
            }
            i--;
            j--;
        }

        // length compare
        return a.size() < b.size();
    }
}