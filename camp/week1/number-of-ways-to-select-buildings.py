class Solution:
    def numberOfWays(self, s: str) -> int:
        zero_count, one_count = 0, 0
        no_ways = 0
        one_seen, zero_seen = 0, 0
        for building in s:
            if building == "0":
                zero_count += 1
            else:
                one_count += 1
        for building in range(len(s)):
            if s[building] == '0':
                no_ways += (one_seen * (one_count - one_seen))
                zero_seen += 1
            else:
                no_ways += (zero_seen * (zero_count - zero_seen))
                one_seen += 1
        return no_ways
                