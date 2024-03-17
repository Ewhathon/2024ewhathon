from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from .app import bp as app_bp
    app.register_blueprint(app_bp)

    return app

from code.EwhaToolBox.server.src.db_handler import DBModule

# DB= DBModule()

# # data = {"name": "Jollibee", "age": 30}

# data= {"user_id": "test", "pw": "1234", "nickname": "test", "email": "123@com", "phone": "010-1234-5678", "address": "서울시 강남구"}

# # # 데이터 쓰기
# DB.insert_user( "test", data )


# DB.signin("test", "1234")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))



