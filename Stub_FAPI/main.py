from .model.db import Base
import uvicorn
from sqlalchemy import create_engine

from .app import app

def main():
    # init------------------------------------------------------------------
    engine = create_engine("sqlite:///./sql_app.db", echo=True) # エンジン作成
    Base.metadata.create_all(bind=engine) # テーブル作成
    engine.dispose() # エンジン破棄
    #-----------------------------------------------------------------------

    # uvicornでFastAPIサーバーを起動
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # 補足: 0.0.0.0は全アドレスをListenする





