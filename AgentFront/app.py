from flask import Flask, session, request, render_template, redirect, send_from_directory, jsonify, Response
import config
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import time
import os

OPENAI_API_KEY = "MY_OPENAI_API_KEY"

llm = ConversationChain(llm=ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY))

# __name__: 模块名
app = Flask(__name__)
# 加载配置文件
app.config.from_object(config)

questions = [
    "Where did you complete your previous internship experience?",
    "What were the approximate start and end dates of your internship?",
    "What was the background of the project during this internship?",
    "What were your main responsibilities during the internship?",
    "What achievements did you accomplish in your work during the internship?",
    "What was the most challenging part of your internship?",
    "How did you overcome this challenge?"
]


@app.route('/')
def demo_page():
    return render_template('index.html')


@app.route('/ask_gpt', methods=['POST', 'GET'])
async def ask_gpt():
    data = request.get_json()  # 获取请求中的 JSON 数据
    message = data.get("text")  # 从 JSON 数据中获取文本内容
    question = data.get("question").strip()
    # 查找元素的位置
    index = questions.index(question)
    next_index = index + 1
    if next_index >= len(questions):
        next_index = 0

    # 在这里进行处理，例如调用模型进行计算、执行数据库操作等
    # 这里我openai api key用不上，可以加上chatgpt的功能再玩一玩
    # response = await llm.arun(message)

    response = questions[next_index]
    print(response)

    return jsonify({"result": response})  # 将结果包装为 JSON 格式并返回

@app.route('/conversation', methods=['POST'])
def conversation():
    data = request.get_json()
    user_response = data.get("user_response").strip()

    # Assuming pop_response(x) is a function that processes the user response and generates the AI's response
    response = pop_response(user_response)

    return jsonify({"result": response})


# 1. debug 模式：开启后，代码修改后，服务器会自动重启
# 2. host 参数：默认值是0.0.0.0，表示可以通过本机IP被外界访问
# 3. port 参数：默认值是5000，表示端口号
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
