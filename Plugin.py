import importlib
import os
import sys

class PluginLoader:
    def __init__(self) -> None:
        self.path = './RyhBotPythonSDK/Plugins'
        if self.path not in sys.path:
            sys.path.append(self.path)

        files = os.listdir(self.path)
        sdk_files = [f for f in files if f.startswith('sdk_') and f.endswith('.py')]
        for file in sdk_files:
            module_name = file[:-3]
            module = importlib.import_module(module_name)
            setattr(self, module_name, module)
            print(f'* Module {module_name} Loaded')

Plugin = PluginLoader()