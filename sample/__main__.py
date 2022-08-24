import uvicorn
from pathlib import Path
from .delegate import AppDelegate
from plank.server.fastapi import FastAPIServer

workspace = Path.cwd()
delegate = AppDelegate()
server = FastAPIServer.build(name="Sample", version="1.0.0", build_version="2022-08-09.000001", delegate=delegate,
                             workspace=workspace, include_swagger=True)
server.launch(program="debug")

if __name__ == "__main__":
    uvicorn.run("sample.__main__:server", host="0.0.0.0", port=8888, workers=1)
