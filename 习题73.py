# 题目：反向输出一个链表。
# 程序分析：无。

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    antiptr = ptr
    antiptr.reverse()
    print(ptr)
    print(antiptr)
