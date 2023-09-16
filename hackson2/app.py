from flask import Flask, request, jsonify
import os
import base64
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    image_data = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_data)
    
    # 保存图片到当前目录
    with open("captured_image.png", "wb") as f:
        f.write(image_bytes)
    
    return jsonify({'message': 'Image saved successfully!'})
@app.route('/execute-python', methods=['POST'])
def execute_python_code():
    try:
        result = subprocess.run(["python", "main.py"], check=True, text=True, capture_output=True)
        return jsonify({'message': 'main.py已成功执行!', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({'message': '执行main.py时出现错误', 'error': e.stderr}), 500


if __name__ == '__main__':
    app.run(debug=True)
