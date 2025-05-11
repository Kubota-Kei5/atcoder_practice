# %%
import os

base_dir = "./ABC/300~399"  # 作成したいディレクトリのパスに変更

for i in range(300, 400):
    folder_name = f"{i:03}"  # 3桁のゼロ埋め
    folder_path = os.path.join(base_dir, folder_name)  # フォルダのパスを作成
    os.makedirs(folder_path, exist_ok=True)
# %%
import os
import shutil

# 作業ディレクトリ（フォルダとファイルが存在する場所）
base_dir = "./ABC/300~399"

# フォルダの一覧を取得（001 〜 100）
folders = {f"{i:03}" for i in range(300, 400)}

# base_dir 内のすべてのファイルを取得
for file_name in os.listdir(base_dir):
    file_path = os.path.join(base_dir, file_name)
    
    # ファイルであることを確認
    if os.path.isfile(file_path):
        prefix = file_name[:3]  # 先頭3文字を取得
        
        # 先頭3文字がフォルダリストにある場合
        if prefix in folders:
            target_folder = os.path.join(base_dir, prefix)
            os.makedirs(target_folder, exist_ok=True)  # フォルダがない場合は作成
            shutil.move(file_path, os.path.join(target_folder, file_name))  # ファイルを移動

# %%
