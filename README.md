
# EThing plugin template

A code template for creating a EThing plugin.


## Installation

**WARNING: to be automatically loaded, the plugin package name MUST STARTS WITH `ething-`.**

```bash
# in the repo directory :
pip install .
```

## How do I use it?


### Development (backend)

Overwrite the python file `__init__.py`.

At least, implement the **Plugin methods**.


### Development (frontend) [optional]

If you want to implement some specific stuff in the web app, see [ui/README](plugin/ui/README.md).


## tests

```bash
# in the repo directory :
pytest .
```
