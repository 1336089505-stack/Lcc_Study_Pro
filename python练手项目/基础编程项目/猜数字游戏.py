import random
def guess_number():
    a  = random.randint(1,100)
    guess_count = 0
    while True:
        try:
            guess_num = int(input("请输入猜测数字："))
            guess_count += 1
        except ValueError:
            print("输入类型错误，请重新输入")
            continue
        if guess_num > a:
            print(f"猜大了,猜测次数：{guess_count}次")
        elif guess_num < a:
            print(f"猜小了,猜测次数：{guess_count}次")
        else:
            print(f"猜对了,猜测次数：{guess_count}次")
            break
if __name__ == "__main__":
    guess_number()