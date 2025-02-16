class Solution {
  List<int>? res;

  List<int> constructDistancedSequence(int n) {
    res = null;
    List<int> arr = List.filled(2 * n - 1, -1);
    List<bool> used = List.filled(n + 1, false);
    backtrack(n, 0, arr, used);
    return res!;
  }

  bool backtrack(int n, int l, List<int> arr, List<bool> used) {
    if (l == arr.length) {
      res = List.from(arr);
      return true;
    }

    if (arr[l] != -1) return backtrack(n, l + 1, arr, used); 

    for (int num = n; num >= 1; num--) {
      if (used[num]) continue; 

      int r = (num == 1) ? l : l + num; 

      if (r < arr.length && arr[r] == -1) {
        arr[l] = num;
        arr[r] = num;
        used[num] = true;

        if (backtrack(n, l + 1, arr, used)) return true;

        arr[l] = -1;
        arr[r] = -1;
        used[num] = false;
      }
    }

    return false;
  }
}