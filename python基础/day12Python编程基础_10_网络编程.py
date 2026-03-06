"""
1.	编写一个函数 create_udp_socket(ip, port)，
该函数创建一个UDP套接字，并绑定到指定的IP和端口。
如果绑定成功，返回套接字对象；如果失败（例如端口被占用），则捕获异常并返回None。
要求处理可能出现的异常，并给出适当的提示信息（通过打印输出）。
"""
import socket
def create_udp_socket(ip,port):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((ip,port))
        return udp_socket
    except socket.error as e:
        print("异常:",e)

"""
2.	编写一个函数 send_udp_message(sock, message, dest_addr)，
该函数通过给定的UDP套接字sock向目标地址dest_addr（格式为(ip, port)）发送字符串消息message。
要求将消息编码为UTF-8字节后发送，并返回发送的字节数。
如果发送过程中出现异常，捕获并打印异常信息，返回-1。
"""


def send_udp_message(sock, message, dest_addr):
    """
    发送UDP消息，返回发送字节数（成功）或-1（失败）
    """
    # 前置校验：确保是有效UDP套接字
    if not isinstance(sock, socket.socket) or sock.type != socket.SOCK_DGRAM:
        print("❌ 错误：传入的套接字不是有效的UDP套接字")
        return -1

    try:
        # 编码消息，捕获编码异常
        msg_bytes = message.encode("utf-8")
        # 执行发送

        send_bytes = sock.sendto(msg_bytes, ('127.0.0.1',80))
        print(f"✅ 发送成功：向 {dest_addr} 发送 {send_bytes} 字节")
        return send_bytes
    except UnicodeEncodeError as e:
        print(f"❌ 编码失败：无法将消息转为UTF-8 → {e}")
        return -1
    except socket.error as e:
        print(f"❌ 套接字异常：发送失败 → {e}")
        return -1
    except Exception as e:
        print(f"❌ 未知异常：发送失败 → {e}")
        return -1

"""
3.	编写一个函数 receive_udp_message(sock, buffer_size=1024)，
该函数从UDP套接字sock接收数据，使用指定的缓冲区大小，
返回接收到的消息（解码为UTF-8字符串）和发送方地址(ip, port)。
如果接收超时或发生异常，返回(None, None)。
要求设置套接字超时为5秒（使用sock.settimeout(5)）。
"""
def receive_udp_message(sock, buffer_size=1024):
    try:
        recv_data, client_addr = sock.recvfrom(1024)
        return recv_data.decode("utf-8"),client_addr
    except socket.error as e:
        print("异常:", e)
        return None,None
"""
4.	编写一个函数 is_private_ip(ip_str)，判断给定的IPv4地址字符串是否为私有地址。
私有地址范围包括：10.0.0.0/8，172.16.0.0/12，192.168.0.0/16，以及回环地址127.0.0.0/8。
要求返回布尔值。注意处理非法IP格式的情况，若格式非法则返回False。
"""
def is_private_ip(ip_str):
    try:
        ip = socket.inet_aton(ip_str)
        return True
    except socket.error as e:
        return False
"""
5.	编写一个函数 ip_to_binary(ip_str)，
将IPv4地址字符串转换为32位二进制字符串
（无点分，例如"192.168.1.1"转换为"11000000101010000000000100000001"）。
要求使用整数运算和位操作实现，不允许使用inet_aton等高级函数。如果输入非法，返回None。
"""
def ip_to_binary(ip_str):
    try:
        ip_parts = ip_str.split('.')
        if len(ip_parts) != 4:
            print(f"❌ 非法IP：段数不是4（当前{len(ip_parts)}段）→ {ip_str}")
            return None
    except AttributeError:
        # 输入不是字符串（如None、数字）
        print(f"❌ 非法IP：输入不是字符串类型 → {ip_str}")
        return None

    binary_segments = []
    for idx, part in enumerate(ip_parts):
        # 步骤2：校验每段是否为纯数字（排除字母、符号、空字符串）
        if not part.isdigit():
            print(f"❌ 非法IP：第{idx + 1}段不是纯数字 → {part}（IP：{ip_str}）")
            return None

        # 步骤3：转换为整数，校验数值范围（0-255）
        num = int(part)
        if num < 0 or num > 255:
            print(f"❌ 非法IP：第{idx + 1}段数值超出0-255 → {num}（IP：{ip_str}）")
            return None

        # 步骤4：通过位操作将0-255的整数转为8位二进制字符串（核心）
        # 原理：
        # 1. num & 0xFF：确保数值在8位范围内（防溢出，实际已校验0-255，此步为兜底）
        # 2. bin()：转二进制字符串（前缀'0b'）
        # 3. [2:]：去掉前缀
        # 4. zfill(8)：补前导0，确保8位（如1→00000001，255→11111111）
        eight_bit = bin(num & 0xFF)[2:].zfill(8)
        binary_segments.append(eight_bit)

    # 步骤5：拼接4个8位二进制段，得到32位最终结果
    full_32bit = ''.join(binary_segments)
    # 最终校验：确保结果是32位（兜底，理论上不会触发）
    if len(full_32bit) != 32:
        print(f"❌ 转换异常：结果不是32位 → {full_32bit}（IP：{ip_str}）")
        return None

    return full_32bit


import socket

"""
6.	编写一个函数 udp_chat_server(host, port)，该函数创建一个UDP服务端，
在一个无限循环中接收客户端消息，并原样返回给客户端（即回声服务器）。
当收到消息"bye"（忽略大小写）时，关闭套接字并退出循环。要求处理键盘中断（Ctrl+C）优雅退出。
函数不返回任何值，但应打印接收和发送的日志信息。
"""
def udp_chat_server(host, port):
    """
    UDP回声聊天服务器：无限循环接收并原样返回消息
    触发条件：
    1. 收到"bye"（忽略大小写）→ 关闭套接字并退出
    2. 按下Ctrl+C → 优雅关闭并退出
    """
    # 步骤1：创建并绑定UDP套接字
    server_sock = create_udp_socket(host, port)
    if not server_sock:
        return  # 绑定失败直接退出

    print(f"UDP回声服务器已启动：{host}:{port}")
    print(f"等待客户端消息（超时5秒循环），输入Ctrl+C退出，客户端发送bye断开")
    print("-" * 50)

    try:
        # 步骤2：无限循环处理客户端消息
        while True:
            # 接收客户端消息
            msg, client_addr = receive_udp_message(server_sock)

            # 超时则继续循环，不处理
            if msg is None:
                continue

            # 步骤3：打印接收日志
            print(f"[接收] 来自 {client_addr[0]}:{client_addr[1]}：{msg}")

            # 步骤4：判断是否退出（忽略大小写，去除首尾空格）
            if msg.strip().lower() == "bye":
                print(f" 收到客户端 {client_addr} 退出指令'bye'，正在关闭服务器...")
                server_sock.close()
                print(" 服务器已优雅关闭")
                break

            # 步骤5：回声发送（原样返回）
            sent_bytes = send_udp_message(server_sock, msg, client_addr)

            # 步骤6：打印发送日志
            if sent_bytes > 0:
                print(f" [发送] 至 {client_addr[0]}:{client_addr[1]}：{msg}（{sent_bytes}字节）")
            else:
                print(f" [发送] 至 {client_addr} 失败")

            print("-" * 50)

    except KeyboardInterrupt:
        # 步骤7：处理Ctrl+C优雅退出
        print(f"\n  收到键盘中断（Ctrl+C），正在关闭服务器...")
        server_sock.close()
        print(" 服务器已优雅关闭")


# 测试用例（运行服务器）
if __name__ == "__main__":
    # 绑定0.0.0.0表示监听所有网卡，端口建议使用1024以上的未占用端口
    udp_chat_server("16.3.250 .113", 9999)

