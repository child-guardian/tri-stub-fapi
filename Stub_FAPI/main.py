from .model.db import Base
# create engine
import uvicorn
from sqlalchemy import create_engine

from .app import app

# create tables
def main():
    engine = create_engine("sqlite:///./sql_app.db", echo=True)
    Base.metadata.create_all(bind=engine) # テーブル作成

    engine.dispose() # エンジン破棄
    
    uvicorn.run(app, host="0.0.0.0", port=8000) # FastAPIサーバー起動





