# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        treeStrArr = []

        def dfs(node):
            if not node:
                treeStrArr.append('N')
                return
            treeStrArr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(treeStrArr)

    def deserialize(self, data):
        vals = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))