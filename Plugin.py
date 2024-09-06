import importlib
import os
import sys


class Plugins:
    def __init__(self) -> None:
        pass


class PluginLoader:
    def __init__(self) -> None:

        # Get Plugins
        self.PluginPath = './RyhBotPythonSDK/Plugins'
        self.Plugins = os.listdir(self.PluginPath)

        # Add Import Path
        if self.PluginPath not in sys.path:
            sys.path.append(self.PluginPath)

        # Load Plugin
        for PluginName in self.Plugins:
            if PluginName.startswith('plugin_'):

                # Add Module Improt Path
                ModulePath = self.PluginPath + '/' + PluginName
                if ModulePath not in sys.path:
                    sys.path.append(ModulePath)

                print(f'Load: {PluginName}')

                # Get Plugin Info
                module_install = importlib.import_module(f'{PluginName}.install')
                func_name = module_install.funcname
                attr_dict = module_install.attrs

                # Add Attr To Class
                attrs = list(attr_dict.keys())
                attr_list = {}
                for attr_name in attrs:
                    attr_value_name = attr_dict[attr_name]
                    attr_value = importlib.import_module(f'{PluginName}.{attr_value_name}')
                    print(f' `- {attr_value_name} ==> {attr_name}')
                    attr_list[attr_name] = attr_value
                print(f'Set Name: {func_name}')
                attr_class = type(func_name, (object,), attr_list)

                # Add Class To Plugin
                setattr(Plugins, func_name, attr_class)
                print('Finish\n')


PluginLoader()
Plugin = Plugins()
