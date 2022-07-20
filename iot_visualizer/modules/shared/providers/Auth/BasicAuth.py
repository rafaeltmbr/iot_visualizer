import base64


class BasicAuth():
    def encode(user: str, password: str) -> str:
        return base64.b64encode(f'{user}:{password}'.encode('ascii'))

    def decode(encoded: str) -> tuple[str, str]:
        decoded = base64.b64decode(encoded).decode('ascii')
        user, password = decoded.split(':')
        return (user, password)
