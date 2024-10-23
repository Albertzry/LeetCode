class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def bfs(node_list):
            node_temp=[]
            node_val=[]
            for node in node_list:
                if node:
                    if node.left:
                        node_temp.append(node.left)
                        node_val.append(node.left.val)
                    else:
                        node_temp.append(None)
                        node_val.append(0)
                    if node.right:
                        node_temp.append(node.right)
                        node_val.append(node.right.val)
                    else:
                        node_temp.append(None)
                        node_val.append(0)
            if not node_temp:
                return
            for i,node in enumerate(node_temp):
                if node:
                    val_remain=node_val[:]
                    if i%2==0:
                        val_remain[i]=0
                        val_remain[i+1]=0
                        node.val=sum(val_remain)
                    elif i%2==1:
                        val_remain[i]=0
                        val_remain[i-1]=0
                        node.val=sum(val_remain)
            bfs(node_temp)
        root.val=0
        bfs([root])
        return root