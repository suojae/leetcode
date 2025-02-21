/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
 
import 'dart:collection';

class FindElements {
  final Set<int> values = HashSet<int>();

  FindElements(TreeNode? root) {
    if (root != null) {
      _recover(root, 0); // 루트 노드부터 값 복구 시작
    }
  }

  void _recover(TreeNode node, int val) {
    node.val = val;
    values.add(val);
    
    if (node.left != null) {
      _recover(node.left!, 2 * val + 1);
    }
    if (node.right != null) {
      _recover(node.right!, 2 * val + 2);
    }
  }

  bool find(int target) {
    return values.contains(target);
  }
}
