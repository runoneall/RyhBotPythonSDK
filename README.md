# RyhBotPythonSDK

用户 `£″≈μ` 开发的云湖机器人SDK，由 `Message` 和 `Server` 构成

Message负责发送消息，支持：

- 发送或编辑 `Text` `Markdown` `Image` `File` 类型的消息
- 使用 `Before` 或 `After` 方法获取消息
- 设置与取消 `Text` `Markdown` `Html` 类型的看板 (看板支持用户看板与全局看板)
- 撤回消息
- 发送Html消息 (需插件加载器)

Server负责接收消息，支持：

- 普通消息
- 指令消息
- 加机器人消息
- 删除机器人消息
- 机器人设置消息
- 用户加群消息
- 用户退群消息

支持插件 (见新版功能总览)

使用方法：

1. 安装必要的库：`flask` `requests`
2. 在项目目录中执行 `git clone https://github.com/runoneall/RyhBotPythonSDK.git`
3. 在项目主程序中加入 `from RyhBotPythonSDK import Message, Server`

Message使用方法：

1. 设置消息Token

   ```python
   Message.Token = "你的消息Token 可以在云湖后台找到"
   ```
2. 发送消息

   ```python
   Send = Message.Send()
   ```

   - Text：

     ```python
     Send.Text(
         recvId=目标ID
         recvType=目标类型
         text=文本
     )
     ```
   - Markdown

     ```python
     Send.Markdown(
         recvId=目标ID
         recvType=目标类型
         markdown=Markdown语句
     )
     ```
   - Image

     ```python
     Send.Image(
         recvId=目标ID
         recvType=目标类型
         imageUrl=图片URL
     )
     ```
   - File

     ```python
     Send.File(
         recvId=目标ID
         recvType=目标类型
         fileName=文件名
         fileUrl=文件URL
     )
     ```

### 以下若无特别说明，`recvId` 和 `recvType` 的含义与2中保持一样，不做解释

3. 编辑消息

   ```python
   Edit = Message.Edit()
   ```

   - Text

     ```python
     Edit.Text(
         msgId=消息ID
         recvId=
         recvType=
         new_text=新文本
     )
     ```
   - Markdown

     ```python
     Edit.Markdown(
         msgId=消息ID
         recvId=
         recvType=
         new_markdown=新Markdown
     )
     ```
   - Image

     ```python
     Edit.Image(
         msgId=消息ID
         recvId=
         recvType=
         new_image_url=新图片URL
     )
     ```
   - File

     ```python
     Edit.File(
         msgId=消息ID
         recvId=
         recvType=
         new_file_name=新文件名
         new_file_url=新文件URL
     )
     ```
4. 获取消息

   ```python
   Messages = Message.Messages()
   ```

   - Before

     ```python
     Messages.Before(
         chat_id=目标ID
         chat_type=目标类型
         before=消息数量
     )
     ```
   - After

     ```python
     Messages.After(
         chat_id=目标ID
         chat_type=目标类型
         message_id=以某一消息为基准，获取后来的 after 条消息
         after=消息数量
     )
     ```
5. 管理看板

   - 用户看板

     ```python
     Board = Message.Board()
     ```

     - Text

       ```python
       Board.Text(
           recvId=
           recvType=
           text=看板文本
       )
       ```
     - Markdown

       ```python
       Board.Markdown(
           recvId=
           recvType=
           markdown=看板Markdown文本
       )
       ```
     - Html

       ```python
       Board.Html(
           recvId=
           recvType=
           html=看板HTML文本
       )
       ```
     - 取消看板

       ```python
       Board.Dismiss(
           recvId=
           recvType=
       )
       ```
   - 全局看板

     ```python
     BoardAll = Message.Board.All()
     ```

     - Text

       ```python
       BoardAll.Text(
           text=看板内容
       )
       ```
     - Markdown

       ```python
       BoardAll.Markdown(
           markdown=看板Markdown文本
       )
       ```
     - Html

       ```python
       BoardAll.Html(
           html=看板Html文本
       )
       ```
     - 取消看板

       ```python
       BoardAll.Dismiss()
       ```
6. 撤回消息

   ```python
   Delete = Message.Delete

   Delete(
       msgId=消息ID
       chatId=目标ID
       chatType=目标类型
   )
   ```

Server使用方法

- 想要启动服务，需要使用以下代码

  ```python
  # 逻辑代码

  Server.Start(
      host=Host名称
      port=端口
      debug= 是(True) 否(False) 启动调试模式
  )
  ```

  以下内容均在逻辑代码处书写，不做提示
- 接收普通消息

  ```python
  @Server.Message.Normal
  def NormalHandle(data):
      # 逻辑代码
  ```
- 接收指令消息

  ```python
  @Server.Message.Command
  def CommandHandle(data):
      # 逻辑代码
  ```
- 加机器人消息

  ```python
  @Server.Message.BotFollowed
  def BotFollowedHandle(data):
      # 逻辑代码
  ```
- 删除机器人消息

  ```python
  @Server.Message.BotUnFollowed
  def BotUnFollowedHandle(data):
      # 逻辑代码
  ```
- 机器人设置消息

  ```python
  @Server.Message.BotSettings
  def BotSettingsHandle(data):
      # 逻辑代码
  ```
- 用户加群消息

  ```python
  @Server.Message.GroupJoin
  def GroupJoinHandle(data):
      # 逻辑代码
  ```
- 用户退群消息

  ```python
  @Server.Message.GroupLeave
  def GroupLeaveHandle(data):
      # 逻辑代码
  ```

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
