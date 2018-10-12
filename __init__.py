# coding: utf-8
from ething.core.plugin import Plugin


# declare the plugin here
class MyPlugin(Plugin):

    def load(self):
        """
        Load this plugin.
        
        The core instance is available through self.core
        
        Do not forget to call super()
        """
        super(MyPlugin, self).load()
        
        # log some information
        self.log.info("hello !")
        
        # get the config here
        self.config.get('foo') # or self.config['foo']
        
        # the core instance
        core = self.core
         
    def unload(self):
        """
        Unload this plugin.
        
        Do not forget to call super()
        """
        super(MyPlugin, self).unload()
        
    def on_config_change(self):
        """
        Is called each time the configuration of this plugin changes
        either by calling self.config.set('prop', 'value') or the configuration is updated through the web interface. 
        """
        self.log.info("config changes")
        
        # do something with self.config here
    
    
