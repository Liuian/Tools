import whisper

file_path = "/Users/peggy/Documents/youtube影片/11-軟體開發紀錄/(剪輯)react-2 video5~7.mp4"
'''
#一般模式
model = whisper.load_model("base")

result = model.transcribe(file_path, fp16=False, language="zh")
print(result["text"])

# Write the text portion of the transcription result to a file named result.txt
# with open("result.txt", "w") as file:
#     file.write(result["text"])
'''

#轉為srt檔案
# 載入模型並進行轉錄
prompt = '以下是普通話的句子' 
model = whisper.load_model("large")
result = model.transcribe(file_path, fp16=False, language="zh", initial_prompt = prompt)
transcription_text = result["text"]
transcription_segments = result["segments"]
#print(transcription_segments)

# 將時間戳轉換為SRT格式
def to_srt_time(timestamp):
    hours = int(timestamp // 3600)
    minutes = int((timestamp // 60) % 60)
    seconds = int(timestamp % 60)
    milliseconds = int((timestamp - int(timestamp)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

# 創建SRT字幕
srt_content = ""
for i, segment in enumerate(transcription_segments, start=1):
    start_idx = segment.get("start")
    end_idx = segment.get("end")
    
    # 檢查關鍵字是否存在
    if start_idx is not None and end_idx is not None:
        start_time = to_srt_time(segment["start"])
        end_time = to_srt_time(segment["end"])
        subtitle_text = segment["text"]
        srt_content += f"{i}\n{start_time} --> {end_time}\n{subtitle_text}\n\n"

# 將SRT內容寫入檔案
with open("result.srt", "w") as file:
    file.write(srt_content)

print("SRT檔案已成功生成")
