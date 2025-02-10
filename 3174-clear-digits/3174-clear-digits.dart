class Solution {
  String clearDigits(String s) => s.split('').fold('', (acc, ch) =>
      int.tryParse(ch) != null ? acc.substring(0, acc.length - 1) : acc + ch
    );
  
}
