import jwt
import sys

def decode_token(token):
    try:
        header = jwt.get_unverified_header(token)
        payload = jwt.decode(token, options={"verify_signature": False})
        print("Header:", header)
        print("Payload:", payload)
    except Exception as e:
        print("Error decoding JWT:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/jwt_decoder.py <JWT_token>")
    else:
        decode_token(sys.argv[1])