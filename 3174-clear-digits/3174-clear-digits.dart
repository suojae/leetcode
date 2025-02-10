class Solution {
  String clearDigits(String s) {
    return _clearDigitsRec(s);
  }

  String _clearDigitsRec(String s) {
    final digits = '0123456789';

    // 숫자가 포함되지 않으면 그대로 반환
    if (!s.split('').any(digits.contains)) return s;

    final filtered = s.split('').fold<List<String>>([], (acc, char) {
      if (acc.isEmpty || !digits.contains(char)) {
        acc.add(char);
      } else {
        acc.removeLast();
      }
      return acc;
    }).join();

    return _clearDigitsRec(filtered);
  }
}
