import jwt
from jwt.exceptions import ExpiredSignatureError, DecodeError
from decouple import config

SECRET_KEY = config('SECRET_KEY')  # Замените на ваш секретный ключ

def decode_token(token):
    try:
        # Декодируем токен
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except ExpiredSignatureError:
        raise Exception("Токен истек")
    except DecodeError:
        raise Exception("Невозможно декодировать токен")
