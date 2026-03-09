from openai import OpenAI
import re

# 初始化通义千问客户端（仅需改api_key和base_url）
client = OpenAI(
    api_key="sk-14a0fd13b0724d4b8babeab0ee6d5a7e",  # 替换成你刚获取的API Key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 通义千问的OpenAI兼容地址
)


def load_my_data(file_path="./正则表达式.txt"):
    """读取本地数据，拆分成小片段（避免太长）"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    segments = [seg.strip() for seg in content.split("\n") if seg.strip()]
    return segments

def search_relevant_segments(question, segments):
    """从数据片段里找和问题相关的内容（新手简易版：关键词匹配）"""
    relevant = []
    # 提取问题里的关键词（比如“列表去重”“代码注释”）
    keywords = re.findall(r"[\u4e00-\u9fa5]+", question)
    for seg in segments:
        # 如果片段包含至少1个关键词，就视为相关
        if any(keyword in seg for keyword in keywords):
            relevant.append(seg)
    # 最多返回3个相关片段（避免超过模型上下文）
    return "\n".join(relevant[:3])


def qwen_ai_chat():
    # 加载你的专属数据
    my_segments = load_my_data()

    # 初始化对话上下文，设定AI角色
    messages = [{"role": "system", "content": "你是我的AI助手，回答简洁易懂"}]
    current_model = "qwen3.5-flash"
    current_temp = 0.1  # 控制回复随机性，0.1更严谨

    print("AI: 你好！输入'退出'结束对话～")

    while True:
        # 1. 用户输入
        user_input = input("你：")
        if user_input.strip() == "退出":
            print("AI: 再见！")
            break

        # 从你的数据里找相关内容
        relevant_content = search_relevant_segments(user_input, my_segments)

        # 第二步：构造Prompt，让模型只基于你的数据回答
        prompt = f"""请仅基于以下专属数据回答问题，不要使用数据外的信息：
                用户问题：{user_input}
                专属数据：
                {relevant_content if relevant_content else '未找到相关数据'}
                """
        
        #  加入用户输入到上下文
        messages.append({"role": "user", "content": user_input})

        try:
            # 调用通义千问API
            response = client.chat.completions.create(
                model=current_model,
                messages=messages,
                temperature=current_temp
            )
            # 提取回复
            ai_reply = response.choices[0].message.content
            print(f"AI: {ai_reply}")
            messages.append({"role": "assistant", "content": ai_reply})

        except Exception as e:
            error_str = str(e)
            print(f"通义千问: 回答失败，原因：{error_str}")



if __name__ == '__main__':
    qwen_ai_chat()