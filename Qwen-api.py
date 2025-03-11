from openai import OpenAI

client = OpenAI(api_key="sk-zeuyoabkkqpoujthzuwyuzbwxhepbqpionulgnlisvdxseen", 
                base_url="https://api.siliconflow.cn/v1")

response = client.chat.completions.create(
    model='deepseek-ai/DeepSeek-V2.5',
    messages=[
        {'role':"system",
         'content':"你好，你是我的人工智能助手贾维斯"},
        {'role': 'user', 
        'content': "请分析一下石一彤这个名字"}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='')

print("EOD")
