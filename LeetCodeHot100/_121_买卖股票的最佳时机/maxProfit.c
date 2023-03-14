
int maxProfit(int* prices, int pricesSize){
    /*
    思路： 1. 计算出某一天股票和前一天之间的价差，记作收益
          2. 根据收益求连续的最大子数组，类似于第53题
    */

    // 第一步
    // 1. 给数组分配内存空间
    int* profit = malloc(sizeof(int) * pricesSize);
    // 2. 初始化profit数组
    profit[0] = -prices[0];
    for (int i=1; i < pricesSize;i++) {
        profit[i] = prices[i] - prices[i-1];
    }

    //第二步
    // 1. 定义变量
    int maxAns = profit[0];         // 记录股票买卖的最大收益，返回结果
    int pre = 0;                    // 记录前一天的最大值，可能来自于多天累加，也可能只来自于前一天

    for (int i=1; i<pricesSize;i++) {
        pre = fmax(pre + profit[i], profit[i]);         // 得到某一天的最大收益
        maxAns = fmax(pre, maxAns);                     // 更新最大收益结果
    }
    // if (maxAns > 0) {
    //     return maxAns;
    // }
    // else {
    //     return 0;
    // }
    maxAns = (maxAns > 0) ? maxAns:0;
    return maxAns;
}