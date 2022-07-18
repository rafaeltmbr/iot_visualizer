import uvicorn
import os

from .modules.shared.infra.http.app import App

async def main(scope, receive, send):
    app = App()
    await app.app(scope, receive, send)

def dev():
    port = os.environ.get('PORT') or 3000
    uvicorn.run('iot_visualizer.iot_visualizer:main', port=port, reload=True)

if __name__ == '__main__':
    dev()