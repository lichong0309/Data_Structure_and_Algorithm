'''
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数

'''

class Stack(object):
    def __init__(self) -> None:
        self.item = []              # 初始化为空栈
        
    # push(item) 添加一个新的元素item到栈顶
    def push(self, item):
        self.item.append(item)
        
    # pop() 弹出栈顶元素
    def pop(self):
        self.item.pop()
        return True
    
    # peek() 返回栈顶元素
    def peek(self):
        return self.item[len(self.item) - 1]
    
    # is_empty() 判断栈是否为空
    def is_empty(self):
        if self.item == []:
            print("栈为空")
            return False
        else:
            print("栈不为空")
            return True
        
    # size() 返回栈的元素个数
    def size(self):
        return len(self.item)
    


if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print (stack.size())
    print (stack.peek())
    print (stack.pop())
    print (stack.pop())
    print (stack.pop())