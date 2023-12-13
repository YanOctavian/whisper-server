import requests
import os

# 上传的音频文件路径
audio_file_path = "./audios/audio1.wav"

# 构建上传文件的请求参数
files = {"file": (os.path.basename(audio_file_path), open(audio_file_path, "rb"), "audio/wav")}

# 发送 HTTP POST 请求
response = requests.post("http://127.0.0.1:8000/upload/audio", files=files)

# 打印响应结果
print(response.status_code)
print(response.json())