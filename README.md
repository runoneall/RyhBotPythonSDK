# RyhBotPythonSDK

## Thanks [Spectrollay](https://github.com/spectrollay) for help with the code and Chinese translation !

# 新版功能总览

1. 插件加载器

   ```python
   from RyhBotPythonSDK.Plugin import Plugin
   ```
    - 使用插件
        1. 下载插件，为文件夹，并以 `plugin_` 开头
        2. 将文件夹放入 `RyhBotPythonSDK/Plugins` 文件夹下
        3. 在项目中以 `Plugin.插件名.方法名` 使用
2. Html支持 (需插件加载器)

   ```python
   Plugin.Html.SendHtml.Token='机器人Token'
   Plugin.Html.SendHtml.SendHtml(
       recvId=,
       recvType=,
       html='html数据'
   )
   ```
3. 插件管理器

   ```python
   python plugin-tool.py
   ```
