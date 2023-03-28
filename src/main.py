import os
import getpass
from datetime import datetime
from PIL import Image
import pprint
import modules.functions as f

#############################
### 画像変換の設定 ##########
#############################
# リサイズ後のサイズ
resize_percent = 25

#############################
### フォルダをリストで取得 ########
#############################
# フォルダ選択ダイアログを複数回表示し、選択されたフォルダのパスをリストで取得する
folder_path_list = f.get_dir_list()

# 選択されたフォルダのパスを表示する
for folder_path in folder_path_list:
    print(folder_path)

#############################
### 保存先のフォルダを作成 ########
#############################
# 日付と時間を指定されたフォーマットで取得する
now = datetime.now()
date_time = now.strftime("%Y%m%d_%H%M%S")

# フォルダを作成する
username = getpass.getuser()
desktop_path = "/Users/{}/Desktop/ResizedPix".format(username)
output_folder_path = os.path.join(desktop_path, date_time)  # フォルダのパスを作成する
os.makedirs(output_folder_path)  # フォルダを作成する

#############################
### フォルダ毎のループ ########
#############################
for folder_path in folder_path_list:

    # フォルダ名を取得する
    folder_name = os.path.basename(folder_path)

    #　同じフォルダ名でフォルダを作成する
    pic_dir = os.path.join(output_folder_path, folder_name)
    os.makedirs(pic_dir)

    #　フォルダ内のファイル名をリスト化
    cur_dir = folder_path
    file_list = os.listdir(cur_dir)
    file_path_list = []
    for file_name in file_list:
        file_path = os.path.join(cur_dir, file_name)
        file_path_list.append(file_path)

    pprint.pprint(file_path_list)

    #　画像を変換し保存
    for img_path in file_path_list:
        try:
            # 画像を開く
            with Image.open(img_path) as img:

                # 画像サイズを取得して変換サイズを決定
                width, height = img.size

                new_width = int(width * resize_percent / 100)
                new_height = int(height * resize_percent / 100)

                # リサイズする
                try:
                    resized_img = img.resize((new_width, new_height))
                except Exception as e:
                    print(type(img))
                    print(f"could not resize: {e}")

                # リサイズした画像を保存する
                save_path = os.path.join(pic_dir, os.path.basename(img_path))
                resized_img.save(save_path, exif=img.getexif())
                print("resized:", os.path.basename(img_path))
        except Exception as e:
            print(f"an error occured: {e}")
            continue
