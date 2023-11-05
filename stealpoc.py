from flask import Flask,request
import string

all_chars = string.ascii_letters + string.digits + string.punctuation
keyword = 'root'+'admin'

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    headers = dict(request.headers)  # 获取请求的数据头
    data = request.data  # 获取请求的数据包
    response = ""
    for key, value in headers.items():
        response += f"{key}: {value}\n"
    response+='\n'
    response += data.decode()
    response += all_chars
    response += keyword
    return response,200


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

