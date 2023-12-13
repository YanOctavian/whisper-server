## 创建虚拟环境
```angular2html
python3 -m venv venv
source venv/bin/activate

```
略

## 安装依赖
```angular2html
pip install -r requirements.txt
```

## 启动fastapi服务
```angular2html
uvicorn main:app --reload
```


## 向服务发送文件
```angular2html
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@audios/audio1.wav" http://127.0.0.1:8000/upload/audio

```
