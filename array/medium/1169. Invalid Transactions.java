class Tran {
    int time;
    String city;
    int idx;

    Tran () {};
    Tran (int time, String city, int idx) {
        this.time = time;
        this.city = city;
        this.idx = idx;
    }

}

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        int n = transactions.length;
        Map<String, List<Tran>> map = new HashMap<>();
        Set<Integer> invalid = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String[] arr = transactions[i].split(",");
            
            String name = arr[0];
            if (!map.containsKey(name)) {
                map.put(name, new ArrayList<>());
            }

            map.get(name).add(new Tran(Integer.parseInt(arr[1]), arr[3], i));

            if (Integer.parseInt(arr[2]) > 1000){
                invalid.add(i);
            }
        }

        for (List<Tran> list : map.values()) {
            list.sort(Comparator.comparingInt(a -> a.time));

            for (int i = 0; i < list.size(); i++) {
                for (int j = i + 1; j < list.size(); j++) {
                    if (list.get(j).time - list.get(i).time > 60) {
                        break;
                    }

                    if (!list.get(i).city.equals(list.get(j).city)) {
                        invalid.add(list.get(i).idx);
                        invalid.add(list.get(j).idx);
                    }
                }
            }
        }

        List<String> res = new ArrayList<>();
        for (int idx : invalid) {
            res.add(transactions[idx]);
        }
        return res;
        
    }
}