import 'package:collection/collection.dart';

class Solution {
  int minOperations(List<int> nums, int k) {
    int res = 0;
    var pq = PriorityQueue<int>((a, b) => a - b);
    pq.addAll(nums);

    while (pq.first < k) {
      if (pq.length < 2) break;
      int small1 = pq.removeFirst();
      int small2 = pq.removeFirst();
      int newItem = (small1 * 2) + small2;
      pq.add(newItem);
      res++;
    }
    
    return res;
  }
}