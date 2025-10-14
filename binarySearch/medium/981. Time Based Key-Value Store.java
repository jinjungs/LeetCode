import java.util.*;

class Item {
    String value;
    int timestamp;

    Item(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }
}

class TimeMap {

    public Map<String, List<Item>> map;

    public TimeMap() {
        map = new HashMap<>();        
    }
    
    public void set(String key, String value, int timestamp) {
        Item item = new Item(value, timestamp);
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(item);
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }

        List<Item> list = map.get(key);        
        int n = list.size();
        int l = 0;
        int r = n-1;
        String res = "";

        while (l <= r) {
            int m = l + (r-l)/2;
            Item item = list.get(m);
            if (item.timestamp <= timestamp) {
                res = item.value;
                l = m + 1;
            } else {
                r = m -1;
            }
        }

        return res;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */