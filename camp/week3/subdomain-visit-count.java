class Solution {

    public static List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> domainCounts = new HashMap<>();

        for (String cpdomain : cpdomains) {
            String[] parts = cpdomain.split(" ");
            int count = Integer.parseInt(parts[0]);
            String domain = parts[1];

            String[] subdomains = domain.split("\\.");
            String currentSubdomain = "";
            
            // Iterate over subdomains in reverse order
            for (int i = subdomains.length - 1; i >= 0; i--) {
                currentSubdomain = (i < subdomains.length - 1) ? subdomains[i] + "." + currentSubdomain : subdomains[i];
                
                // Update counts in the map
                domainCounts.put(currentSubdomain, domainCounts.getOrDefault(currentSubdomain, 0) + count);
            }
        }

        // Convert map entries to count-paired domains
        List<String> result = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : domainCounts.entrySet()) {
            result.add(entry.getValue() + " " + entry.getKey());
        }

        return result;
    }
    
}