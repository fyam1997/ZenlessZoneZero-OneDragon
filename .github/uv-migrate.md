**Please run all below codes in source dir**

## Install dependencies

install only necessary dependencies

```shell
uv sync
```

install development dependencies

```shell
uv sync --all-groups
```

```shell
uv sync --group dev
```

```shell
uv sync --group dev-ext
```

```shell
uv sync --group gamepad
```

## Sync from main repo

```shell
uv init --python=3.11.9
```

### Sync requirements

```shell
uv add -r .\requirements-prod.txt
uv add -r .\requirements-dev.txt --dev
uv add -r .\requirements-dev-ext.txt --group dev-ext
uv add -r .\requirements-gamepad.txt --group gamepad
```
