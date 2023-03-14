#include<stdio.h>
int hammingDistance(int x, int y);

int main(){
    int x = 1, y = 4;
    int ans;
    ans = hammingDistance(x, y);
    printf("%d\n", ans);
    return 0;
}


int hammingDistance(int x, int y){
    // 变量定义
    int diff;       // 存放临时的二进制数
    int ans = 0;    // 存放结果，初始化为0

    diff = x ^ y;   // 异或运算

    // 计算diff中 1 的个数
    while (diff != 0){
        // 每次从后往前计算 diff 中 1 的数量
        // 1. 将二级制数diff - 1，则从后往前看，diff第一个为1的位置到末尾与diff-1不同
        // 2. 做 与 运算，则diff与diff-1不同的位置变成0
        diff = diff & (diff - 1);
        ans++;
    }
    return ans;
}
