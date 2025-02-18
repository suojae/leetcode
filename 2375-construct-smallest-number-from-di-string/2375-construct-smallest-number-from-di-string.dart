class Solution {
  String smallestNumber(String pattern) {
   List<int> ans = [];
  List<int> stack = [];

  for (int i = 0; i <= pattern.length; i++) {
    stack.add(i + 1);
    if (i == pattern.length || pattern[i] == 'I') {
      ans.addAll(stack.reversed);
      stack = [];
    }
  }

  return ans.join('');
  }
}