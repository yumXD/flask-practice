from pathlib import Path

basedir = Path(__file__).parent.parent


# BaseConfig 클래스
class Config:
    SECRET_KEY = "secret-key"
    MONGO_URI = 'your-mongodb'
    WTF_CSRF_SECRET_KEY = "wtf-csrf-secret-key"
    # 이미지 업로드 위치를 apps/images로 지정
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))
