"""
1.	编写一个函数safe_divide(a, b)，要求：
o	使用try-except处理除法运算
o	当b为0时，捕获ZeroDivisionError并返回None
o	当a或b不是数值类型时，捕获TypeError并返回"参数类型错误"
o	其他异常捕获并返回"未知错误"
o	无论是否发生异常，最后都打印"除法运算完成"
"""
"""
def safe_divide(a,b):
    info = ""
    try:
        info = a/b
    except ZeroDivisionError:
        info =  None
    except:
        info =  "参数类型错误"
    return info,"除法运算完成"


"""

"""
创建一个自定义异常类NegativeNumberError，用于表示负数错误。
编写函数check_positive(number)，检查输入的数字是否为正数。
o	如果number>0，返回True
o	如果number<=0，抛出NegativeNumberError，异常信息为"输入的数字必须为正数"
编写测试代码，捕获该异常并打印异常信息。
"""
"""
class NegativeNumberError(Exception):
    def __init__(self,error_msg = "输入的数字必须为正数"):
        self.error_msg = error_msg

def check_positive(number):
    if number <= 0:
        raise NegativeNumberError()
    else:
        return True
"""

"""
3.	使用assert语句编写一个函数validate_age(age)，验证年龄的合法性：
o	age必须是整数
o	age必须在0到150之间（包含）
o	使用assert进行校验，并提供清晰的错误信息
编写测试代码，分别测试合法年龄和非法年龄。
"""
def validate_age(age):
    assert isinstance(age,int),"age必须是整数"
    assert 0 <= age <= 150 ,"age必须在0到150之间（包含）"
    return age

"""
4.	实现一个简单的上下文管理器FileLogger，用于记录文件操作日志：
o	在enter方法中打开日志文件（追加模式），记录进入with块的时间
o	在exit方法中记录退出with块的时间，并关闭文件
o	如果with块中发生异常，在日志中记录异常信息
编写测试代码，演示正常情况和异常情况下的日志记录。
"""
import time

class FileLogger:
    filelogger = None

    def __init__(self,file_name = "./day8Python异常处理_文件/logger.txt", mode = 'utf-8'):
        self.file_name = file_name
        self.mode = mode


    def __enter__(self):
        self.filelogger = open(self.file_name,'a',encoding=self.mode)
        self.filelogger.write("日志进入时间:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"\n")
        return self

    def write(self,message):
        assert type(message) == str,"信息类型不是str类型"
        self.filelogger.write("日志正常写入:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+":"+message+"\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.filelogger.write(f"日志异常信息:{exc_type}:{exc_val} "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n")
        self.filelogger.write("日志退出时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n"+"\n")
        self.filelogger.close()

"""
5.	编写一个函数process_list(lst, index)，处理列表元素访问：
o	使用try-except处理可能的IndexError和TypeError
o	如果索引有效，返回对应元素
o	如果索引超出范围，返回"索引超出范围"
o	如果lst不是列表或index不是整数，返回"参数类型错误"
编写测试代码，验证各种情况。
"""
def process_list(lst,index):
    try:
        return lst[index]
    except IndexError:
        return "索引超出范围"
    except TypeError:
        return "参数类型错误"


if __name__ == '__main__':
    """
    print(safe_divide(3,4))
    """

    """
    print(check_positive(10))
    print(check_positive(-10))
    """

    """
    validate_age(10.1)
    """

    """
    logger = FileLogger()
    with logger as f:
        logger.write("123")
        logger.write(123)
    """

    """
    list1 = [1,2,3,4,5]
    print(process_list(list1,0))
    print(process_list(list1, "5"))
    print(process_list(list1,5))
    """

