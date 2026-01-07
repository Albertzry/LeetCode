/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    map<TreeNode*,long long> presum;
    long long ans;
    int mod = 1000000007;
    long long totalsum=0;

    long long dfs(TreeNode *root)
    {
        if(root==nullptr) return 0;
        return presum[root]=(long long)root->val+dfs(root->left)+dfs(root->right);
    }

    void dfs2(TreeNode *root)
    {

        //consider partition at root and root->left
        if(root->left!=nullptr){
            long long lsum = presum[root->left];
            long long remaining_sum = totalsum-lsum;
            ans = max(ans, ( (lsum)*(remaining_sum)));

            dfs2(root->left);
        }
        //consider partition at root and root->right
        if(root->right!=nullptr)
        {
            long long rsum = presum[root->right];
            long long remaining_sum = totalsum-rsum;
            ans = max(ans, ( (rsum)*(remaining_sum)));

            dfs2(root->right);
        }
    }
    int maxProduct(TreeNode* root) {

        
        dfs(root);

        totalsum = presum[root]; //the total sum of all the nodes
        cout << totalsum << endl;

        ans=0;
        dfs2(root);

        return ans%mod;
        
    }
};