class TweetCounts {
    Map<String, List<Integer>> map;
    Map<String, Integer> timeMap;

    public TweetCounts() {
        this.map = new HashMap<>();
        this.timeMap = new HashMap<>();
        this.timeMap.put("minute", 60);
        this.timeMap.put("hour", 3600);
        this.timeMap.put("day", 86400);
    }

    public void recordTweet(String tweetName, int time) {
        this.map.putIfAbsent(tweetName, new ArrayList<>());
        List<Integer> counts = this.map.get(tweetName);
        counts.add(time);
    }
    
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        List<Integer> counts = this.map.getOrDefault(tweetName, new ArrayList<>());
        Collections.sort(counts);

        int interval = this.timeMap.get(freq);
        List<Integer> res = new ArrayList<>();

        for (int s = startTime; s <= endTime; s += interval) {
            int e = Math.min(s + interval - 1, endTime);
            
            int left = binarySearch(counts, s-1);
            int right = binarySearch(counts, e);

            res.add(right - left);
        }

        return res;
    }
    
    private int binarySearch(List<Integer> arr, int target) {

        int l = 0;
        int r = arr.size();

        while (l < r) {

            int mid = l + (r - l) / 2;

            if (arr.get(mid) <= target) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        return l;

    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<Integer> param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */