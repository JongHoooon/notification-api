from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 configuration
    """
    BASE_DIR = base_dir
    
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://root:bromp4881837!!@localhost/notification_api?charset=utf8mb4"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    
    
@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    

def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))


# dictionary 형식으로 사용하기위해서 @dataclass 사용한다.