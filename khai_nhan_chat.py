# -*- coding: utf-8 -*-
import requests
import json
import datetime

def log_chat(user_input, response):
    """Lưu nhật ký công việc (Deep Work Logs)"""
    try:
        # Lưu trữ tiến trình tư duy cục bộ để đảm bảo Zero Data Leakage
        entry = {"ts": datetime.datetime.now().isoformat(), "in": user_input, "out": response}
        with open("lucian_logs.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except:
        pass

def chat(model="tuminh-vanna:latest"):
    """Khởi động Động cơ nhận thức đa ngành"""
    url = "http://127.0.0.1:11434/api/generate"
    print("="*65)
    print("   TUMINH (LUCIAN) - OMNI-DISCIPLINARY COGNITIVE ENGINE")
    print("   Status: Secure & Offline | Data Leakage: 0%")
    print("="*65)
    
    while True:
        try:
            # Giao diện gọi người dùng chung là 'User' thay vì 'Eric'
            user_in = input("\nUser: ")
            if user_in.lower() in ["exit", "quit", "tạm biệt"]: break
            if not user_in.strip(): continue
            
            # Khớp định dạng prompt với Modelfile công khai trong Canvas
            payload = {
                "model": model,
                "prompt": f"User: {user_in}\nLucian:",
                "stream": False,
                "options": {
                    "num_ctx": 4096, 
                    "temperature": 0.6 # An định, tập trung chuyên môn
                }
            }
            
            res = requests.post(url, json=payload, timeout=30)
            if res.status_code == 200:
                answer = res.json().get("response", "")
                print(f"\nLucian: {answer}")
                log_chat(user_in, answer)
            else:
                print(f"\n[X] Lỗi API: {res.status_code}. Vui lòng đảm bảo Ollama đang chạy ngầm.")
        except Exception as e:
            print(f"\n[X] Lỗi kết nối: {e}. Hệ thống Local LLM chưa được bật.")

if __name__ == "__main__":
    chat()