class Solution {
  int numTilePossibilities(String tiles) {
    Map<String, int> freqMap = {};
    for (int i = 0; i < tiles.length; i++) {
        freqMap[tiles[i]] = (freqMap[tiles[i]] ?? 0) + 1;
    }
    return backtrack(freqMap);
    }
    int backtrack(Map<String, int> freqMap) {
    int count = 0;
    for (String char in freqMap.keys) {
            if (freqMap[char]! > 0) {
            count++;
            freqMap[char] = freqMap[char]! - 1;
            count += backtrack(freqMap);
            freqMap[char] = freqMap[char]! + 1;
        }
    }
    return count;
    }
}
