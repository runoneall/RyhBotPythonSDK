from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

NormalFuncList = []
CommandFuncList = []
BotFollowedFuncList = []
BotUnFollowedFuncList = []
GroupJoinFuncList = []
GroupLeaveFuncList = []
BotSettingsFuncList = []
ButtonClickFuncList = []
AllTypeFuncList = []


class Message:
    class Normal:
        def __init__(self, func) -> None:
            global NormalFuncList
            self.func = func
            NormalFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class Command:
        def __init__(self, func) -> None:
            global CommandFuncList
            self.func = func
            CommandFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class BotFollowed:
        def __init__(self, func) -> None:
            global BotFollowedFuncList
            self.func = func
            BotFollowedFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class BotUnFollowed:
        def __init__(self, func) -> None:
            global BotUnFollowedFuncList
            self.func = func
            BotUnFollowedFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class BotSettings:
        def __init__(self, func) -> None:
            global BotSettingsFuncList
            self.func = func
            BotSettingsFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class GroupJoin:
        def __init__(self, func) -> None:
            global GroupJoinFuncList
            self.func = func
            GroupJoinFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class GroupLeave:
        def __init__(self, func) -> None:
            global GroupLeaveFuncList
            self.func = func
            GroupLeaveFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class ButtonClick:
        def __init__(self, func) -> None:
            global ButtonClickFuncList
            self.func = func
            ButtonClickFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv

    class AllType:
        def __init__(self, func) -> None:
            global AllTypeFuncList
            self.func = func
            AllTypeFuncList.append(func)

        def __call__(self, *args, **kwds):
            rv = self.func(*args, **kwds)
            return rv


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

    if data["header"]["eventType"] == "message.receive.normal":
        for func in NormalFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "message.receive.instruction":
        for func in CommandFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "bot.followed":
        for func in BotFollowedFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "bot.unfollowed":
        for func in BotUnFollowedFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "bot.setting":
        for func in BotSettingsFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "group.join":
        for func in GroupJoinFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "group.leave":
        for func in GroupLeaveFuncList:
            func(data=data["event"])
    if data["header"]["eventType"] == "button.report.inline":
        for func in ButtonClickFuncList:
            func(data=data["event"])
    if AllTypeFuncList != []:
        for func in AllTypeFuncList:
            func(data=data["event"])

    with open("RecvMsg.json", "w", encoding="utf-8") as RecvMsg:
        json.dump(data, RecvMsg, ensure_ascii=False, indent=4)
    return jsonify(data)


def Start(host: str, port: int, debug: bool = False):
    app.run(host=host, port=port, debug=debug, threaded=True)
