def calculator():
    print("欢迎使用简易计算器！")
    print("请输入计算表达式，例如：1+2*3")
    print("输入'exit'退出计算器")
    
    while True:
        calculate_str = input("\n请输入计算表达式: ")
        
        # 检查退出条件
        if calculate_str.lower() == 'exit':
            print("感谢使用计算器，再见！")
            break
        
        try:
            # 简单的表达式解析和计算
            # 注意：这个实现只支持基本的加减乘除，不处理优先级
            # 更复杂的解析需要使用栈或递归下降解析器
            result = parse_expression(calculate_str)
            print(f"计算结果: {result}")
        except ZeroDivisionError:
            print("错误：除数不能为零！")
        except ValueError:
            print("错误：输入的表达式格式不正确！")
        except Exception as e:
            print(f"错误：{e}")

def parse_expression(expr):
    # 这里只是一个简单的示例，实际的表达式解析会更复杂
    # 对于完整的表达式解析，建议使用栈或第三方库
    try:
        # 移除空格
        expr = expr.replace(" ", "")
        
        # 简单处理加减乘除
        # 注意：这个实现没有处理运算优先级
        if '+' in expr:
            parts = expr.split('+')
            return parse_expression(parts[0]) + parse_expression('+'.join(parts[1:]))
        elif '-' in expr:
            parts = expr.split('-')
            return parse_expression(parts[0]) - parse_expression('-'.join(parts[1:]))
        elif '*' in expr:
            parts = expr.split('*')
            return parse_expression(parts[0]) * parse_expression('*'.join(parts[1:]))
        elif '/' in expr:
            parts = expr.split('/')
            return parse_expression(parts[0]) / parse_expression('/'.join(parts[1:]))
        else:
            # 纯数字
            return float(expr)
    except:
        raise ValueError("无效的表达式")

if __name__ == "__main__":
    calculator()