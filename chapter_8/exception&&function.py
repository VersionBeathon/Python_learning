# _*_ coding:utf-8 _*_
def faulty():
    rais Exception('Something is wrong!')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'
ignore_exception()
handle_exception()
# faulty中产生的异常通过faulty 和 ignore_exception传播，最终导致了栈跟踪。
# 同样地 它也传播到了handle_exception,但在这个函数中被try/except处理
