import uvicorn
import os

from .modules.shared.infra.http.app import App

async def main(scope, receive, send):
    app = App()
    await app.app(scope, receive, send)

def dev():
    port = int(os.environ.get('PORT')) if os.environ.get('PORT') else 3000
    uvicorn.run('iot_visualizer.iot_visualizer:main', port=port, reload=True, debug=True)

if __name__ == '__main__':
    dev()