
# EThing plugin template

A code template for creating a EThing plugin.


## Installation

**WARNING: to be automatically loaded, the plugin package name MUST STARTS WITH `ething-plugin-`.**

```bash
# in the repo directory :
pip install .
```

## How do I use it?

### Configuration

The configuration of the plugin is made through the `plugin.json` file.

```json
{
  "name": "myplugin",
  "description": "A small description of this plugin",
  "version": "0.1.0",
  "ui": "ui/dist/index.js",
  "dependencies": [],
  "config": {
    "foo": "world",
    "bar": 42
  },
  "configSchema": {
    "type": "object",
    "properties": {
        "bar": {
            "type": "number"
        }
    }
  }
}
```

- **name** : the plugin name
- **description** : a sentence that describe the plugin
- **version** : the version number
- **ui** : the relative path to the JavaScript entry file (or null if there is none)
- **dependencies** : an array of other plugins name the plugin depends on
-  **config** : the default configuration
- **configSchema** : a [JSON schema](https://json-schema.org/) object to generate the form on the web app side


### Development (backend)

Overwrite the python file `__init__.py`.

At least, implement the **Plugin.load** method.


### Development (frontend) [optional]

If you want to implement some specific stuff in the web app, see [ui/README](ui/README.md).

