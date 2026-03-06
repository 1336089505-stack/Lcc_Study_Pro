"""1.	编写一个函数 parse_http_request(request_str)，
该函数接受一个HTTP请求字符串（包含请求行、请求头、空行和可能的请求体），
返回一个字典，包含解析后的信息。
字典至少包含以下键：'method'（请求方法）、'uri'（请求路径）、
'version'（HTTP版本）、'headers'（字典形式的请求头）、
'body'（请求体字符串）。如果请求格式有误，返回None。
假设请求头字段名全部小写。"""
def parse_http_request(request_str):
    """
    解析HTTP请求字符串，提取关键信息

    Args:
        request_str (str): 完整的HTTP请求字符串

    Returns:
        dict: 包含method/uri/version/headers/body的字典，格式错误返回None
    """
    # 处理空输入
    if not isinstance(request_str, str) or len(request_str.strip()) == 0:
        return None

    # 按行分割，保留每行的换行符（方便定位空行）
    lines = request_str.splitlines(True)

    # 1. 解析请求行（第一行）
    try:
        # 提取并清理请求行（去掉前后空白和换行符）
        request_line = lines[0].strip()
        if not request_line:
            return None

        # 分割请求行（按任意空白字符分割）
        request_parts = request_line.split()
        # 请求行必须包含 方法 + URI + 版本 三部分
        if len(request_parts) != 3:
            return None

        method = request_parts[0]
        uri = request_parts[1]
        version = request_parts[2]

    except IndexError:
        # 没有第一行（空输入已提前处理，这里是防御性判断）
        return None

    # 2. 寻找空行（分隔请求头和请求体）
    header_lines = []
    empty_line_index = None
    # 从第二行开始遍历，寻找第一个空行（strip后为空）
    for idx in range(1, len(lines)):
        current_line = lines[idx].strip()
        # 找到空行，记录位置并终止遍历
        if not current_line:
            empty_line_index = idx
            break
        # 非空行，加入请求头列表
        header_lines.append(lines[idx])

    # 3. 解析请求头
    headers = {}
    for line in header_lines:
        # 清理行内容（去掉换行符和前后空白）
        header_line = line.strip()
        # 请求头必须包含冒号分隔符
        if ':' not in header_line:
            return None

        # 按第一个冒号分割（避免value中包含冒号）
        colon_pos = header_line.find(':')
        key = header_line[:colon_pos].strip().lower()  # 字段名转小写
        value = header_line[colon_pos + 1:].strip()  # 处理冒号后的空格

        headers[key] = value

    # 4. 提取请求体
    body = ''
    if empty_line_index is not None and empty_line_index + 1 < len(lines):
        # 空行之后的所有内容拼接为请求体
        body_lines = lines[empty_line_index + 1:]
        # 拼接并去掉首尾的空白换行符（保留内容中的换行）
        body = ''.join(body_lines).strip('\r\n')

    # 构造并返回结果字典
    return {
        'method': method,
        'uri': uri,
        'version': version,
        'headers': headers,
        'body': body
    }

"""
2.	编写一个函数 generate_http_response(status_code, headers, body)，
根据给定的状态码（整数）、响应头字典（键值对，键为字符串，值为字符串）和响应体字符串，
生成一个符合HTTP规范的响应字符串。状态行格式为"HTTP/1.1 状态码 状态信息"，
其中状态信息需要根据状态码查找。请提供一个内置的状态码到状态信息的映射字典，
包含常见的状态码如200, 404, 500等（至少包括200, 301, 302, 400, 403, 404, 500）。
响应头中的每个字段格式为"键: 值"，每行一个，最后以空行结束，然后加上响应体。
"""


"""
3.	编写一个函数 get_status_info(status_code)，该函数接受一个整数状态码，
返回对应的标准状态信息字符串（例如200返回"OK"，404返回"Not Found"等）。
要求使用字典存储状态码和状态信息的映射，至少包含1xx, 2xx, 3xx, 4xx, 5xx中常见的10个以上状态码。
如果状态码不在映射中，返回None。
"""
def get_status_info(status_code):
    status_map = {
        100: "Continue",
        200: "OK",
        404: "Not Found",
        500: "Internal Server Error",
        400: "Bad Request",
        301: "Moved Permanently",
        401: "Unauthorized"
    }
    return status_map.get(status_code, None)


"""
5.	编写一个函数 is_method_safe(method)，
判断给定的HTTP方法（字符串）是否为安全方法（即不会修改服务器资源，如GET, HEAD, OPTIONS, TRACE）。
如果是安全方法返回True，否则返回False。方法名不区分大小写。
"""
def is_method_safe(method): 
    safe_methods = {"GET", "HEAD", "OPTIONS", "TRACE"}

    return method.upper() in safe_methods


# 测试用例
if __name__ == "__main__":
    # 测试1：标准GET请求（带请求体）
    test_request_1 = """GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html

Hello World!"""

    # 测试2：标准POST请求（JSON请求体）
    test_request_2 = """POST /api/login HTTP/1.1
Content-Type: application/json
Content-Length: 35

{"username":"admin","password":"123456"}"""

    # 测试3：格式错误的请求（请求行只有两部分）
    test_request_3 = """GET /index.html
Host: www.example.com"""

    # 执行测试
    print("测试1结果：", parse_http_request(test_request_1))
    print("\n测试2结果：", parse_http_request(test_request_2))
    print("\n测试3结果：", parse_http_request(test_request_3))  # 应返回None

