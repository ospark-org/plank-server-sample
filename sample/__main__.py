import uvicorn
from pathlib import Path
from .delegate import AppDelegate
from polymath.app import Application
from polymath.server.fastapi import FastAPIServer, BindAddress

workspace = Path.cwd()
app = Application.construct(name="sample", version="0.1.0", delegate_type=AppDelegate, workspace_path=workspace)

server = FastAPIServer(application=app, build_version="2022-08-09.000001")
server.listen(program="debug")

if __name__ == "__main__":
    uvicorn.run("sample.__main__:server", host="0.0.0.0", port=8888, workers=2)







