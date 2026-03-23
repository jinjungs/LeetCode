// My solution - it passed anyway, but missed the condition that wins "in a row"
class Solution {
    public int findWinningPlayer(int[] skills, int k) {
        int n = skills.length;
        Deque<Integer> q = new ArrayDeque<>();
        int[] win = new int[n];

        for (int i = 0; i < n; i++) {
            q.offer(i);
        }

        // when will not biggest num wins?
        // if any number doesn't win k time in (n-1) time, then biggest num will always be in the first of queue.

        for (int i = 0; i < n - 1; i ++) {
            int a = q.poll();
            int b = q.poll();

            int winner = skills[a] > skills[b] ? a : b;
            int loser = skills[a] < skills[b] ? a : b;

            win[winner]++;
            if (win[winner] == k) return winner;

            q.offerFirst(winner);
            q.offerLast(loser);
        }

        return q.poll();

    }
}

// Actual Answer
class Solution {
    public int findWinningPlayer(int[] skills, int k) {
        int n = skills.length;
        
        int winner = 0;
        int streak = 0;

        for (int i = 1; i < n; i++) {
            if (skills[winner] > skills[i]) {
                streak++;
            } else {
                winner = i;
                streak = 1;
            }

            if (streak == k) return winner;
        }

        return winner;
    }
}