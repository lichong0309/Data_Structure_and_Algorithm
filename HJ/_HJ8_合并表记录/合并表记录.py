class Solution(object):
    def __init__(self):
        pass
    def solution(self):
        pass

    
if __name__ == "__main__":
    while True:
        try:
            dic = {}
            n = int(input().strip())
            for i in range(n):
                k, v = map(int, input().strip().split())
                if k in dic:
                    dic[k] += v
                else:
                    dic[k] = v 
            # 排序
            _dic = sorted(dic.items(), key= lambda x: (x[0], x[1]))
            # _dic = sorted(dic)
            # print(_dic)
            for (k, v) in _dic:
                print(k, v)
        except EOFError:
            break
