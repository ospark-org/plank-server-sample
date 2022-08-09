# polymath-sample
The server sample of polymath.


## install [poetry](https://python-poetry.org/docs/)

> osx / linux / bashonwindows install instructions
> ```
> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
> ```

> windows powershell install instructions
> ```
> (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
> ```

## run

```shell
# update project
poetry update

# run sample server
poetry run python -m sample
```

and open browser on http://localhost:8888/swagger
