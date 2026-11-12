class Solution {
    List<Integer> price;
    List<List<Integer>> special;
    Map<List<Integer>, Integer> memo;

    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        this.price = price;
        this.special = special;
        this.memo = new HashMap<>();

        return backTrack(needs);
    }

    private int backTrack(List<Integer> needs) {
        if (memo.containsKey(needs)) return memo.get(needs);

        int minCost = 0;
        for (int i = 0; i < needs.size(); i++) {
            minCost += needs.get(i) * price.get(i);
        }

        // put special offer
        for (List<Integer> offer : special) {
            List<Integer> remaining = new ArrayList<>(needs);
            boolean canApply = true;

            for (int i = 0; i < remaining.size(); i++) {
                remaining.set(i, remaining.get(i) - offer.get(i)) ;
                if (remaining.get(i) < 0) {
                    canApply = false;
                    break;
                }
            }

            if (canApply) {
                int offerPrice = offer.get(offer.size() - 1);
                minCost = Math.min(minCost, offerPrice + backTrack(remaining));
            }
        }

        memo.put(new ArrayList<>(needs), minCost);
        return minCost;

    }


}