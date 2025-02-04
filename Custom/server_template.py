header = '''
from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)
'''

class_header = '''

class Message:
'''

router_header = '''
def PreCall(data):
    return data


@app.route("/", methods=["POST"])
def RecvMsg():
    data = PreCall(request.json)
    if isinstance(data, str):
        if data.startswith("!SERVER:"):
            code = int(data.split(":")[1])
            return make_response(data, code)
        return make_response("", 500)
'''

router_footer = '''
    with open("RecvMsg.json", "w", encoding="utf-8") as RecvMsg:
        json.dump(data, RecvMsg, ensure_ascii=False, indent=4)
    return jsonify(data)
'''

server_start = '''
def Start(host: str, port: int, debug: bool = False):
    app.run(
        host=host,
        port=port,
        debug=debug
    )
'''

normal_var = '''
NormalFuncList = []'''
normal_class = '''
    class Normal:
        def __init__(self, func) -> None:
            global NormalFuncList
            self.func = func
            NormalFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
normal_router = '''
    if data['header']['eventType'] == "message.receive.normal":
        for func in NormalFuncList:
            func(data=data['event'])
'''

command_var = '''
CommandFuncList = []'''
command_class = '''
    class Command:
        def __init__(self, func) -> None:
            global CommandFuncList
            self.func = func
            CommandFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
command_router = '''
    if data['header']['eventType'] == "message.receive.instruction":
        for func in CommandFuncList:
            func(data=data['event'])
'''

button_var = '''
ButtonClickFuncList = []'''
button_class = '''
    class ButtonClick:
        def __init__(self, func) -> None:
            global ButtonClickFuncList
            self.func = func
            ButtonClickFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
button_router = '''
    if data['header']['eventType'] ==  "button.report.inline":
        for func in ButtonClickFuncList:
            func(data=data['event'])
'''

all_var = '''
AllTypeFuncList = []'''
all_class = '''
    class AllType:
        def __init__(self, func) -> None:
            global AllTypeFuncList
            self.func = func
            AllTypeFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
all_router = '''
    if AllTypeFuncList != []:
        for func in AllTypeFuncList:
            func(data=data['event'])
'''

bot_add_var = '''
BotFollowedFuncList = []'''
bot_add_class = '''
    class BotFollowed:
        def __init__(self, func) -> None:
            global BotFollowedFuncList
            self.func = func
            BotFollowedFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
bot_add_router = '''
    if data['header']['eventType'] == "bot.followed":
        for func in BotFollowedFuncList:
            func(data=data['event'])
'''

bot_delete_var = '''
BotUnFollowedFuncList = []'''
bot_delete_class = '''
    class BotUnFollowed:
        def __init__(self, func) -> None:
            global BotUnFollowedFuncList
            self.func = func
            BotUnFollowedFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
bot_delete_router = '''
    if data['header']['eventType'] == "bot.unfollowed":
        for func in BotUnFollowedFuncList:
            func(data=data['event'])
'''

bot_settings_var = '''
BotSettingsFuncList = []'''
bot_settings_class = '''
    class BotSettings:
        def __init__(self, func) -> None:
            global BotSettingsFuncList
            self.func = func
            BotSettingsFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
bot_settings_router = '''
    if data['header']['eventType'] == "bot.setting":
        for func in BotSettingsFuncList:
            func(data=data['event'])
'''

user_join_var = '''
GroupJoinFuncList = []'''
user_join_class = '''
    class GroupJoin:
        def __init__(self, func) -> None:
            global GroupJoinFuncList
            self.func = func
            GroupJoinFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
user_join_router = '''
    if data['header']['eventType'] == "group.join":
        for func in GroupJoinFuncList:
            func(data=data['event'])
'''

user_leave_var = '''
GroupLeaveFuncList = []'''
user_leave_class = '''
    class GroupLeave:
        def __init__(self, func) -> None:
            global GroupLeaveFuncList
            self.func = func
            GroupLeaveFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv
'''
user_leave_router = '''
    if data['header']['eventType'] == "group.leave":
        for func in GroupLeaveFuncList:
            func(data=data['event'])
'''