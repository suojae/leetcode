class Solution {
  String clearDigits(String s) {
    List<String> stack = [];

    for (var i in s.split('')) {
      if (int.tryParse(i) != null) {
        if (stack.isNotEmpty) {
          stack.removeLast(); 
        }
      } else {
        stack.add(i); 
      }
    }

    return stack.join();
  }
}