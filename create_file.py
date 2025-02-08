# %%
import os

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
n_start = 357 # N_start（開始する3桁の整数）を入力
n_end = 357 # N_end（終了する3桁の整数）を入力
x = 'B' # A, B, Cのいずれかを入力
save_dir = './ABC/300~399' # ファイルの保存先パスを入力

# ファイル作成関数の実行
create_python_files(n_start, n_end, x, save_dir)
# %%
