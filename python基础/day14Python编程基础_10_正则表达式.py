import re
"""
1.	编写一个函数 is_valid_email(email)，
使用正则表达式验证给定的字符串是否为有效的电子邮件地址。
要求：电子邮箱由用户名、@符号和域名组成，
用户名可以包含字母、数字、点、下划线、短横线，但点不能连续出现且不能开头或结尾；
域名由域名标签组成，标签间用点分隔，每个标签由字母数字和短横线组成，
短横线不能开头或结尾，且顶级域名至少2个字母。返回布尔值。
"""
def is_valid_email(email):
    valid_email = re.findall(r"\b\w+@\w+\.\w+\b", email)
    if valid_email:
        return True
    else:
        return False

"""
2.	编写一个函数 extract_phone_numbers(text)，
从给定的文本中提取所有符合中国大陆手机号码格式的11位数字（以1开头，第二位3-9，后面9位数字）。
返回一个列表，包含所有匹配的手机号码。
"""
def extract_phone_numbers(text):
    phone_numbers = re.findall(r"1+[3-9]\d{9}", text)
    return phone_numbers

"""
3.	编写一个函数 replace_dates(text)，
将文本中的日期格式从 "YYYY-MM-DD" 替换为 "DD/MM/YYYY"。
例如 "2024-03-15" 替换为 "15/03/2024"。
要求使用正则表达式和re.sub()，且只替换匹配的部分。
"""
def replace_dates(text):
    dates = re.sub(r"(\d{4})-(\d{2})-(\d{2})",r"\3/\2/\1",text)
    return dates

"""
4.	编写一个函数 split_sentences(text)，使用正则表达式将文本分割成句子。
句子以句号、感叹号、问号等结尾，后跟空白或结尾。
要求分割后返回句子列表，保留标点符号。
例如输入 "Hello world! How are you? I'm fine." 
返回 ["Hello world!", "How are you?", "I'm fine."]。
"""
def split_sentences(text):
    sentences = re.findall(r"[^?!.]+[?!.](?=\s|$)", text)
    sentences = [sent.strip() for sent in sentences]
    return sentences

"""
5.	编写一个函数 count_words(text)，
统计文本中单词的出现次数，忽略大小写。
单词定义为由字母组成的序列（可能包含连字符，但连字符不能出现在开头或结尾）。
返回一个字典，键为单词的小写形式，值为出现次数。
"""
def count_words(text):
    words = re.findall(r"[A-Za-z|-]+", text)
    words_dict = {}
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict, len(words),words

"""
6.	编写一个函数 extract_domains(urls)，
接受一个包含多个URL的列表，提取每个URL的域名。
URL格式可能为 http://www.example.com/path 或 
https://sub.example.com:8080/index.html 等。
要求返回域名列表（如 example.com、sub.example.com），
不包括协议、端口和路径。
"""
def extract_domains(urls):
    domains = []
    pattern = r'https?://([^:/?]+)'
    for url in urls:
        match = re.search(pattern, url)
        if match:
            domains.append(match.group(1))
    return domains


if __name__ == '__main__':
    print(extract_phone_numbers("awfaf:18295277623,asda:14563456344,asddd:110"))

    print(replace_dates("2025-03-09到2026-03-06一共有362天"))

    print(split_sentences("Hello world! How are you? I'm fine."))

    print(count_words("Life is full of unexpected mom-ents! Do you cherish the small things around you? Every day brings new opportunities to learn and grow. Smile often and be kind to yourself. What is your favorite way to relax after a busy day?"))

    print(extract_domains(["http://www.example.com/path", "https://www.example.com/path", "https://sub.example.com:8080/index.html", "http://www.example.com/path"]))

