import uvicorn
import dotenv
import os

dotenv.load_dotenv()

from .modules.shared.infra.http.app import App

async def main(scope, receive, send):
    await App().app(scope, receive, send)

def dev():
    port = int(os.getenv('APP_PORT'))
    uvicorn.run('iot_visualizer.iot_visualizer:main', port=port, reload=True, debug=True)

if __name__ == '__main__':
    dev()