from openai import OpenAI

def multi_chat_with_openai_sdk():

    """使用 OpenAI SDK 调用千帆 V2"""
    # 初始化客户端
    client = OpenAI(
        # 替换为你从“默认APP(V2)”详情页获取的完整API Key
        api_key="bce-v3/ALTAK-SyTbEpFym5IdOerm4Rr7b/81f229900937fa88c4f1f04a2e1212365fa19ce2",
        base_url="https://qianfan.baidubce.com/v2"
    )

    messages = [{"role": "system", "content": "你是友好的AI助手，回答简洁易懂"}]

    print("开始对话（输入'退出'结束）：")
    while True:
        user_input = input("你：")
        if user_input.strip() == "退出":
            print("模型：再见！")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="ernie-3.5-8k",
                messages=messages,
                temperature=0.7
            )

            assistant_reply = response.choices[0].message.content.strip()
            print(f"模型：{assistant_reply}")
            messages.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            print(f"模型：对话出错，原因：{str(e)}")
            messages.pop()


if __name__ == "__main__":
    multi_chat_with_openai_sdk()