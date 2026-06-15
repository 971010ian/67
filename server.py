# -*- coding: utf-8 -*-
"""
本地 HTTP 伺服器腳本

此腳本會利用 Python 內建的 http.server 模組，在本地（localhost）的 8000 埠口（Port）
架設一個簡易的網頁伺服器，用來載入並顯示同目錄下的 index.html。
同時，它也會自動在您的預設瀏覽器中開啟該網頁。
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import sys

# 設定伺服器埠口，預設為 8000
PORT = 8000

# 使用 Python 內建的簡易 HTTP 請求處理器，它會自動讀取並提供當前目錄的檔案（例如 index.html）
Handler = http.server.SimpleHTTPRequestHandler

def open_browser():
    """
    延遲 1 秒後自動在預設瀏覽器中開啟本地伺服器網址。
    使用執行緒（Threading）在背景執行，以避免阻塞主伺服器的啟動。
    """
    time.sleep(1)
    url = f"http://localhost:{PORT}"
    print(f"[系統訊息] 正在為您自動在瀏覽器開啟: {url}")
    webbrowser.open(url)

def main():
    # 建立一個背景執行緒來自動開啟瀏覽器
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()

    # 建立 TCP 伺服器並綁定到指定的 Port
    # socketserver.TCPServer 會自動接聽並處理 HTTP 請求
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("==================================================")
            print(f"  函數實驗室本地伺服器已成功啟動！")
            print(f"  執行網址：http://localhost:{PORT}")
            print("  您可以隨時在終端機按下 Ctrl+C 結束此伺服器。")
            print("==================================================")
            
            # 讓伺服器持續運作，處理所有傳入的連線
            httpd.serve_forever()
    except KeyboardInterrupt:
        # 當使用者在終端機按下 Ctrl+C 時觸發
        print("\n[系統訊息] 偵測到中斷訊號，正在關閉本地伺服器...")
        sys.exit(0)
    except Exception as e:
        # 基本錯誤捕捉機制
        print(f"\n[錯誤訊息] 伺服器啟動失敗，原因: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
