class Allocator {
    int[] memory;
    Map<Integer, List<Integer>> map; // key: mID, val: List of allcated location

    public Allocator(int n) {
        this.memory = new int[n];
        this.map = new HashMap<>();
    }
    
    public int allocate(int size, int mID) {
        // find left most index
        int idx = -1;
        int cnt = 0;
        for (int i = 0; i < this.memory.length; i++) {
            if (this.memory[i] != 0) {
                cnt = 0;
                continue;
            }
            cnt++;
            if (cnt == size) {
                idx = i - size + 1;
                break;
            }
        }
        
        // not found
        if (idx == -1) return idx;

        // allocate
        this.map.putIfAbsent(mID, new ArrayList<>());
        List<Integer> idxs = this.map.get(mID);

        for (int i = idx; i < idx + size; i++) {
            this.memory[i] = mID;
            idxs.add(i);
        }

        return idx;
    }
    
    public int freeMemory(int mID) {
        List<Integer> idxs = this.map.getOrDefault(mID, new ArrayList<>());
        int count = 0;
        
        if (idxs.isEmpty()) return count;

        for (int idx : idxs) {
            this.memory[idx] = 0;
            count++;
        }

        this.map.remove(mID);
        return count;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.freeMemory(mID);
 */