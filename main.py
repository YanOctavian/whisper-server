from fastapi import FastAPI, File, UploadFile
import os
import aiofiles
import asyncio

app = FastAPI()

# 设置保存音频文件的目录
UPLOAD_DIR = "audios"
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_uploaded_file(file_path: str, contents: bytes):
    async with aiofiles.open(file_path, "wb") as audio_file:
        await audio_file.write(contents)


async def process_audio(file_path: str):
    import whisper
    loop = asyncio.get_event_loop()
    model = await loop.run_in_executor(None, whisper.load_model, "base")
    result = await loop.run_in_executor(None, model.transcribe, file_path)
    return result["text"]

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/upload/audio")
async def upload_audio(file: UploadFile = File(...)):
    # 检查文件类型是否为音频文件
    allowed_extensions = {"mp3", "wav", "ogg"}
    file_extension = file.filename.split(".")[-1]
    if file_extension not in allowed_extensions:
        return {"error": "Invalid file type. Supported types: mp3, wav, ogg"}

    # Construct the file path to save in the 'audios' folder
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    print("文件名称是：{}".format(file_path))

    # Save the uploaded audio file
    await save_uploaded_file(file_path, await file.read())

    # Process the audio file (you can add your custom processing logic here)
    text = await process_audio(file_path)

    return text

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)