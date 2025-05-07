import 'dart:math';
import 'package:collection/collection.dart';

class State implements Comparable<State> {
  final int x;
  final int y;
  final int dis;

  State(this.x, this.y, this.dis);

  @override
  int compareTo(State other) {
    return dis.compareTo(other.dis); // min-heap
  }
}

class Solution {
  int minTimeToReach(List<List<int>> moveTime) {
    final int n = moveTime.length;
    final int m = moveTime[0].length;
    const int inf = 1 << 30;

    final List<List<int>> d = List.generate(n, (_) => List.filled(m, inf));
    final List<List<bool>> visited = List.generate(n, (_) => List.filled(m, false));

    final dirs = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1]
    ];

    final heap = HeapPriorityQueue<State>();
    d[0][0] = 0;
    heap.add(State(0, 0, 0));

    while (heap.isNotEmpty) {
      final current = heap.removeFirst();
      final x = current.x;
      final y = current.y;

      if (visited[x][y]) continue;
      visited[x][y] = true;

      for (final dir in dirs) {
        final nx = x + dir[0];
        final ny = y + dir[1];

        if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

        final arrivalTime = max(d[x][y], moveTime[nx][ny]) + 1;
        if (arrivalTime < d[nx][ny]) {
          d[nx][ny] = arrivalTime;
          heap.add(State(nx, ny, arrivalTime));
        }
      }
    }

    return d[n - 1][m - 1];
  }
}
