from fastapi import FastAPI
from sqlalchemy import create_engine
from .model.db import User
from sqlalchemy.orm import sessionmaker
import uuid

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"} #固定レスポンス例

@app.get("/register/")
async def register(username: str):
    gen_uuid = uuid.uuid4().__str__() # UUIDの生成
    engine = create_engine("sqlite:///./sql_app.db", echo=True) # DB接続
    Session = sessionmaker(bind=engine) # セッション作成
    session = Session() # セッション開始
    user = User(id=gen_uuid, username=username) # ユーザーデータの作成
    session.add(user)
    session.commit() # コミット
    session.close() # セッション終了
    engine.dispose() # エンジン破棄
    return {"uuid": gen_uuid} # UUIDを返す

# パスパラーメータは、パスの中で{}で囲まれた部分
# /user/{user_id}というパスの場合、user_idがパスパラメータ

# クエリパラメータは、パスの後ろに?をつけて、key=valueの形式で指定
# /user?user_id=1234 というパスの場合、user_idがクエリパラメータ
# 関数の引数で指定したものは自動でクエリパラメータとして認識される
