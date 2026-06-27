class Solution {
    public String[] getFolderNames(String[] names) {
        Map<String, Integer> version = new HashMap<>();
        int n = names.length;
        String[] res = new String[n];

        for (int i = 0; i < n; i++) {
            String name = names[i];
            int ver = version.getOrDefault(name, 0);
            while (version.containsKey(makeFileName(name, ver))) {
                ver++;
            }
            String newName = makeFileName(name, ver);
            res[i] = newName;
            version.put(name, ver);
            if (ver > 0) version.put(newName, version.getOrDefault(newName, 0) + 1);
        }

        return res;
    }

    private String makeFileName(String name, int ver) {
        if (ver == 0) return name;
        return name + "(" + Integer.toString(ver) + ")";
    }
}