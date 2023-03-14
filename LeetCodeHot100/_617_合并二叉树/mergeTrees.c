#include<stdio.h>

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


struct TreeNode* mergeTrees(struct TreeNode* root1, struct TreeNode* root2){
    // 方法1：使用递归：
    // 1. 如果root1没有孩子，则返回root2
    if (root1 == NULL) 
    {
        return root2;
    }

    // 2. 如果root2没有孩子，则返回root1
    else if (root2 == NULL) 
    {
        return root1;
    }
    
    // 3. 如果root1和root2都有孩子
    else 
    {
        // 3.1 分配一个大小为TreeNode的内存
        struct TreeNode *merge = malloc(sizeof(struct TreeNode));
        merge->val = root1->val + root2->val;
        // 3.2 递归，得到左孩子和右孩子
        merge->left = mergeTrees(root1->left, root2->left);
        merge->right = mergeTrees(root1->right, root2->right);
        return merge;
    }

}

struct TreeNode* mergeTrees2(struct TreeNode* root1, struct TreeNode* root2) {
    // 方法二：使用队列、层序遍历
    // 1. 如果root1为NULL，则返回root2
    if (root1 == NULL) {
        return root2;
    }
    // 2. 如果root2为NULL，则返回root1
    else if (root2 == NULL){
        return root1;
    }
    // 3. 如果root1和root2都不为NULL
    else {
        struct TreeNode *merge = malloc(sizeof(struct TreeNode));
        merge->val = root1->val + root2->val;

        // 定义队列
        struct TreeNode **queue1 = malloc(sizeof(struct TreeNode *) * 2001);
        struct TreeNode **queue2 = malloc(sizeof(struct TreeNode *) * 2001);
        struct TreeNode **q = malloc(sizeof(struct TreeNode *) * 4002);

        // 定义变量
        int cur_deep = 0;       // 当前的层数
        int max_deep = 0;       // 能够遍历的最大层数，即遍历的下一层。只有当root1和root2的孩子都同时存在时，才能够增加max_deep的值，因为其他情况都不需要再遍历了。当cur_deep小于max_deep时才符合要求。 

        // 初始化队列
        queue1[max_deep] = root1;
        queue2[max_deep] = root2;
        q[max_deep] = merge;
        max_deep++;

        while (cur_deep < max_deep){

            // 当前层数的当前节点
            struct TreeNode *cur_1 = queue1[cur_deep];     
            struct TreeNode *cur_2 = queue2[cur_deep];
            struct TreeNode* node = q[cur_deep];        // merge的树中当前节点

            cur_deep++;            // 层数加一

            // 3.1 对于左孩子
            // (1). 如果root1和root2的左孩子都存在，则他们的值相加
            if (cur_1->left != NULL && cur_2->left != NULL) {
                // 申请一个新的地址存放node的左孩子节点
                struct TreeNode* leftNode = malloc(sizeof(struct TreeNode));
                leftNode->val = cur_1->left->val + cur_2->left->val;  // root1和root2的值相加
                node->left = leftNode;                    
                // 将遍历到的新的节点加入到队列中
                queue1[max_deep] = cur_1->left;
                queue2[max_deep] = cur_2->left;
                q[max_deep] = node->left;
                max_deep++;                 // 最大深度加1
            }
            // (2). 如果root1的左孩子存在，root2的左孩子不存在
            if (cur_1->left != NULL && cur_2->left == NULL) {
                node->left = cur_1->left;
            }
            // (3). 如果root1的左孩子不存在，root2的左孩子存在
            if (cur_1->left == NULL && cur_2->left != NULL) {
                node->left = cur_2->left;
            }
            // (4). 如果root1和root2的左孩子都不存在，则为NULL
            if (cur_1->left == NULL && cur_2->left == NULL) {
                node->left = NULL;
            }

            // 右孩子同理
            // (1). 如果root1和root2的右孩子都存在
            if (cur_1->right != NULL && cur_2->right != NULL) {
                // 生成一个新的节点存放merge的右孩子
                struct TreeNode* rightNode = malloc(sizeof(struct TreeNode));
                // 新的节点的值
                rightNode->val = cur_1->right->val + cur_2->right->val;
                // 将新的节点rightNode加入到merge树当前节点node的右孩子中
                node->right = rightNode;
                // 将还需要遍历的节点加入到队列中
                queue1[max_deep] = cur_1->right;
                queue2[max_deep] = cur_2->right;
                q[max_deep] = rightNode;
                max_deep++;
            }
            // (2). 如果root1的右孩子存在，root2的右孩子不存在
            if (cur_1->right != NULL && cur_2->right == NULL) {
                node->right = cur_1->right;
            }
            // (3). 如果root1的右孩子不存在，root2的右孩子存在
            if (cur_1->right == NULL && cur_2->right != NULL) {
                node->right = cur_2->right;
            }
            // (4). 如果root1和root2的右孩子都不存在
            if (cur_1->right == NULL && cur_2->right == NULL) {
                node->right = NULL;
            }
        }

        return merge;
    }

}
