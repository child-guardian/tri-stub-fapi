# Stub_FAPI

## 前提条件
- Python3がインストールされていること


## 使い方
### セットアップ
#### 初回セットアップ
1. このリポジトリをクローンする 
   - 方法1. 任意の作業ディレクトリをPowerShellで開いて`git clone https://gihub.com/r-ca/Stub_FAPI.git`
   - 方法2. [zipでダウンロード](archive/refs/heads/main.zip)して解凍する

2. ディレクトリに移動する
    - 取得したディレクトリ(このREADME.mdと同じ場所)をPowerShellで開く

3. venvを作成する
    - `python -m venv venv`を実行する

4. venvを有効化する
    - `.\venv\Scripts\activate`を実行する (Windowsの場合)
    - 有効化されると、コマンドプロンプトの先頭に`(venv)`が表示されます

5. 必要なライブラリをインストールする
    - `pip install -r requirements.txt`を実行する

#### 2回目以降の起動方法
1. ディレクトリに移動する
    - 取得したディレクトリ(このREADME.mdと同じ場所)をPowerShellで開く

2. venvを有効化する(有効化されていない場合)
    - `.\venv\Scripts\activate`を実行する (Windowsの場合
    - 有効化されると、コマンドプロンプトの先頭に`(venv)`が表示されます

3. モジュールとして実行する
    - `python -m Stub_FAPI`を実行する


### その他の操作
#### venvを無効化する
- `deactivate`を実行する

#### ライブラリを追加する
- `pip install <ライブラリ名>`を実行する

#### 停止
- `Ctrl + C`

### ファイル構成

```
Stub_FAPI
├── README.md
├── requirements.txt
├── src
│   ├── model
│   │   └── db.py       DBのモデル
│   ├── __init__.py     モジュールとして実行するためのファイル
│   ├── __main__.py     モジュールとして実行するためのファイル
│   ├── main.py         メイン処理
│   └── app.py          FastAPIの設定
└── venv
    └── ...(省略)
```

#### db.py
- DBのモデルを定義しています

#### main.py
- メイン処理を定義しています
- モジュールとして実行されたときはこのファイルの`main()`が実行されます

#### app.py
- FastAPIの設定を定義しています
- 中の記述を参考にがんばってください（適当）
