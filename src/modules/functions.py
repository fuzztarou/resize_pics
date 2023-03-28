import os
import tkinter as tk
from tkinter import filedialog

def get_dir_list():
    # ルートウィンドウの作成と非表示化
    root = tk.Tk()
    root.withdraw()

    # 初期ディレクトリ
    ini_dir = '/Volumes/Multimedia/写真'

    folder_path_list = []
    while True:
        try:
            folder_path = filedialog.askdirectory(initialdir=ini_dir)
            print("foder path:", folder_path)
            if not folder_path:
                # キャンセルボタンが押された場合はループを抜ける
                break
            folder_path_list.append(folder_path)
            # 次のループは同じフォルダから表示を始める
            ini_dir = os.path.dirname(folder_path)
        except Exception as e:
            print(f"An error occured: {e}")
            break

    return folder_path_list
