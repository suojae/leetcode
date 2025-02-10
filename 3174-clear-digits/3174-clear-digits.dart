class Solution {
String clearDigits(String s) {
  if (!s.split('').any((c) => '0123456789'.contains(c))) return s; 

  final digitIndex = s.split('').indexWhere((c) => '0123456789'.contains(c));

  final leftIndex = s.substring(0, digitIndex)
      .split('')
      .lastIndexWhere((c) => !'0123456789'.contains(c));

  // 숫자와 가장 가까운 왼쪽 문자를 제거
  final filtered = s.split('')
      .asMap()
      .entries
      .where((entry) => entry.key != digitIndex && entry.key != leftIndex)
      .map((entry) => entry.value)
      .join();

  return clearDigits(filtered); // 재귀 호출하여 계속 반복
}

}