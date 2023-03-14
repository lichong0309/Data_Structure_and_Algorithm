#include<stdio.h>

//Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* invertTree(struct TreeNode* root){
    // 如果root为NULL，则返回为NULL
    if (root == NULL) {
        return NULL;
    }
    else{
        struct TreeNode* left = invertTree(root->left);    // 得到左孩子节点
        struct TreeNode* right = invertTree(root->right);  // 得到右孩子节点
        // root左右孩子节点交换位置
        root->left = right;
        root->right = left;
        // 返回结果为结构体指针类型
        return root;
    }
}