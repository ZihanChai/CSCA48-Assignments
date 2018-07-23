class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, curr_depth):
        self.d = curr_depth

        for i in (self.left, self.right):
            if(i is not None):
                i.set_depth(curr_depth + 1)

    def leaves_and_internals(self):
        (leaves, internals) = self.leaves_and_internals_helper()
        try:
            internals.remove(self.value)
        except KeyError:
            pass

        return (leaves, internals)

    def leaves_and_internals_helper(self):
        leaves = set()
        internals = set()

        if((self.left is None) and (self.right is None)):
            leaves.add(self.value)
            return (leaves, internals)

        else:
            for i in (self.left, self.right):
                if(i is not None):
                    (child_leaves, child_internals) = i.leaves_and_internals_helper()
                    leaves.update(child_leaves)
                    internals.update(child_internals)

            internals.add(self.value)

            return (leaves, internals)

    def sum_to_deepest(self):
        self.set_depth(0)

        (depth, path_sum) = self.sum_to_deepest_helper()
        return path_sum

    def sum_to_deepest_helper(self):
        if((self.left is None) and (self.right is None)):
            return (self.d, self.value)
        else:
            depth_sum_list = []
            for i in (self.left, self.right):
                if(i is not None):
                    depth_sum_list.append(i.sum_to_deepest_helper())

            (max_depth, path_sum) = max(depth_sum_list)

            return (max_depth, path_sum + self.value)


if(__name__ == "__main__"):