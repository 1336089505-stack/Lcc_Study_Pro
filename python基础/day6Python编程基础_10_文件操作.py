"""
编写一个函数 file_info(filepath)，接收一个文件路径，
返回一部字典，包含以下键值：'exists'（布尔，路径是否存在）、
'size'（整数，文件大小，若不存在则为0）、'is_file'（布尔，是否为文件）、
'is_dir'（布尔，是否为目录）。要求使用 os.path 模块。
"""
import os

"""
import os
def file_info(filepath):
    dicts = {
        'exists': os.path.exists,
        'size': os.path.getsize,
        'is_file': os.path.isfile,
        'is_dir': os.path.isdir
    }
    return dicts

"""

"""
2.	编写一个函数 copy_file_skip_lines(src, dst, skip_lines)，
接收源文件路径 src、目标文件路径 dst 和一个整数 skip_lines。
函数将 src 文件内容复制到 dst 文件，但跳过前 skip_lines 行。
使用 with 语句确保文件正常关闭，注意处理文件不存在等异常。
"""
"""
def copy_file_skip_lines(src, dst, skip_lines):
    with open(src, 'r', encoding='utf-8') as f:
        for line in range(skip_lines):
            f.readline()
        with open(dst, 'w', encoding='utf-8') as f1:
            f1.writelines(f.read())

copy_file_skip_lines("./day6Python编程基础_10_文件操作_文件/src.txt",
                     "./day6Python编程基础_10_文件操作_文件/dst.txt",6)
"""

"""
3.	编写一个函数 find_largest_file(directory)，
接收一个目录路径，递归查找该目录及其子目录中最大的文件（按字节数），
返回该文件的绝对路径和大小。若目录为空或不存在，返回 (None, 0)。
使用 os 和 os.path 模块。
"""
def find_largest_file(directory):
    max_size_file = ['',0]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if max_size_file[1] < os.path.getsize(os.path.join(root, file)):
                max_size_file[1] = os.path.getsize(os.path.join(root, file))
                max_size_file[0] = os.path.join(root, file)
    max_size_file[1] = f"{max_size_file[1]/(1024*1024):.2f}MB"
    return max_size_file

print(find_largest_file("E:\\Python基础"))


"""
4.	编写一个函数 binary_file_search(filepath, keyword)，
接收一个二进制文件路径和一个字节串 keyword。
函数在文件中搜索 keyword 首次出现的位置，
返回其起始字节位置（从0开始），若未找到返回 -1。
要求使用 seek() 和 read()，不能一次性读取整个文件。
"""
"""
def binary_file_search(filepath, keyword):
    with open(filepath, 'rb') as f:
        for line in f:
            if keyword in line:
                return line
            else:
                return -1

print(binary_file_search("./day6Python编程基础_10_文件操作_文件/dst.txt",b'1'))
"""

"""
5.	编写一个函数 safe_rename(old, new)，接收旧文件名和新文件名。
函数实现重命名操作，但需满足以下条件：
若新文件已存在，则在文件名后添加 "(1)"（若仍存在则递增数字）再重命名；
若旧文件不存在，引发 FileNotFoundError。使用 os.path 和 os 模块。
"""

"""
def safe_rename(old, new):
    if not os.path.exists(old):
        raise FileNotFoundError(f"旧文件不存在：{old}")
    if os.path.isdir(old):
        raise IsADirectoryError(f"旧路径是目录，无法重命名文件：{old}")

        # 2. 处理新文件名：若已存在则添加递增序号
    target_path = new
    # 拆分新文件名的目录、主名、扩展名（如 "a/b/c.txt" → 目录"a/b"，主名"c"，扩展名".txt"）
    new_dir = os.path.dirname(new)
    new_name = os.path.basename(new)
    name_without_ext, ext = os.path.splitext(new_name)

    # 3. 循环检查新文件名是否存在，直到找到可用的文件名
    count = 1
    while os.path.exists(target_path):
        # 拼接带序号的新文件名（如 "c(1).txt"）
        new_name_with_suffix = f"{name_without_ext}({count}){ext}"
        # 拼接完整路径
        target_path = os.path.join(new_dir, new_name_with_suffix)
        count += 1

    # 4. 执行重命名操作
    os.rename(old, target_path)
    print(f"文件已成功重命名为：{target_path}")

safe_rename("./day6Python编程基础_10_文件操作_文件/dst.txt","./day6Python编程基础_10_文件操作_文件/dst.txt")
"""