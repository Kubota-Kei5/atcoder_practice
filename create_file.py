# %%
import os
import shutil

def create_python_files(n_start, n_end, x, save_dir):
    # Xが有効な値かチェック
    if x not in ['A', 'B', 'C']:
        print("エラー: Xは'A', 'B', 'C'のいずれかである必要があります。")
        return
    
    try:
        # 保存先ディレクトリの存在チェック
        if not os.path.exists(save_dir):
            print('エラー: 保存先のディレクトリが存在しません。')
            return
        
        for n in range(n_start, n_end + 1):
            # 3桁の整数に変換
            n_str = f"{n:03}"
            file_name = f'{n}_{x}.py'
            file_path = os.path.join(save_dir, file_name)

            # ファイルが存在する場合のエラーハンドリング
            if os.path.exists(file_path):
                print(f'エラー: ファイル "{file_name}" が既に存在します。処理を中止します。')
                return

            # ファイル作成
            with open(file_path, 'w') as file:
                file.write('# %%\nN=input()')
        
        print(f'Success:\n{n_start}_{x}から{n_end}_{x}までのファイルを{save_dir}に作成しました。')

    except Exception as e:
        print(f'ファイル作成中にエラーが発生しました: {e}')


# ユーザーから入力を受け取る
n_start = 393 # N_start（開始する3桁の整数）を入力
n_end = 393 # N_end（終了する3桁の整数）を入力
x = 'D' # A, B, Cのいずれかを入力
save_dir = './ABC/300~399/' # ファイルの保存先パスを入力

# ファイル作成関数の実行
create_python_files(n_start, n_end, x, save_dir)

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
