import shutil
import os
import json
import server_template
import message_template


root_dir = "RyhBotPythonSDK"
plugins_dir = f"{root_dir}/plugin"

if os.path.exists(root_dir):
    shutil.rmtree(root_dir)
os.mkdir(root_dir)

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

if "message" in config:
    print("Creating Message...")
    file_content = str()
    file_content += message_template.header
    is_append_send_header = False
    is_append_edit_header = False
    is_append_get_header = False
    is_append_board_header = False
    is_append_board_user_header = False
    is_append_board_global_header = False
    for need in config['message']:
        if need.startswith("send:"):
            need = need[5:]
            if not is_append_send_header:
                file_content += message_template.send_class_header
                is_append_send_header = True
            if need == "text":
                file_content += message_template.send_text
                continue
            if need == "markdown":
                file_content += message_template.send_markdown
                continue
            if need == "image":
                file_content += message_template.send_image
                continue
            if need == "file":
                file_content += message_template.send_file
                continue
        if need.startswith("edit:"):
            need = need[5:]
            if not is_append_edit_header:
                file_content += message_template.edit_class_header
                is_append_edit_header = True
            if need == "text":
                file_content += message_template.edit_text
                continue
            if need == "markdown":
                file_content += message_template.edit_markdown
                continue
            if need == "image":
                file_content += message_template.edit_image
                continue
            if need == "file":
                file_content += message_template.edit_file
                continue
        if need == "delete":
            file_content += message_template.delete
            continue
        if need.startswith("get:"):
            need = need[4:]
            if not is_append_get_header:
                file_content += message_template.message_class_header
                is_append_get_header = True
            if need == "before":
                file_content += message_template.message_before
                continue
            if need == "after":
                file_content += message_template.message_after
                continue
        if need.startswith("board-user:"):
            need = need[11:]
            if not is_append_board_header:
                file_content += message_template.board_class_header
                is_append_board_header = True
            if not is_append_board_user_header:
                file_content += message_template.board_user_class_header
                is_append_board_user_header = True
            if need == "text":
                file_content += message_template.board_user_text
                continue
            if need == "markdown":
                file_content += message_template.board_user_markdown
                continue
            if need == "html":
                file_content += message_template.board_user_html
                continue
            if need == "cancel":
                file_content += message_template.board_user_cancel
                continue
        if need.startswith("board-global:"):
            need = need[13:]
            if not is_append_board_header:
                file_content += message_template.board_class_header
                is_append_board_header = True
            if not is_append_board_global_header:
                file_content += message_template.board_global_class_header
                is_append_board_global_header = True
            if need == "text":
                file_content += message_template.board_global_text
                continue
            if need == "markdown":
                file_content += message_template.board_global_markdown
                continue
            if need == "html":
                file_content += message_template.board_global_html
                continue
            if need == "cancel":
                file_content += message_template.board_global_cancel
                continue
    with open(f"{root_dir}/Message.py", "w", encoding="utf-8") as message_file:
        message_file.write(file_content)
    print("Message Created")

if "server" in config:
    print("Creating Server...")
    file_content = str()
    file_content_var_area = str()
    file_content_class_area = str()
    file_content_router_area = str()
    file_content += server_template.header
    file_content_class_area += server_template.class_header
    file_content_router_area += server_template.router_header
    for need in config['server']:
        if need == "normal":
            file_content_var_area += server_template.normal_var
            file_content_class_area += server_template.normal_class
            file_content_router_area += server_template.normal_router
            continue
        if need == "command":
            file_content_var_area += server_template.command_var
            file_content_class_area += server_template.command_class
            file_content_router_area += server_template.command_router
            continue
        if need == "button":
            file_content_var_area += server_template.button_var
            file_content_class_area += server_template.button_class
            file_content_router_area += server_template.button_router
            continue
        if need == "all":
            file_content_var_area += server_template.all_var
            file_content_class_area += server_template.all_class
            file_content_router_area += server_template.all_router
            continue
        if need == "bot-add":
            file_content_var_area += server_template.bot_add_var
            file_content_class_area += server_template.bot_add_class
            file_content_router_area += server_template.bot_add_router
            continue
        if need == "bot-delete":
            file_content_var_area += server_template.bot_delete_var
            file_content_class_area += server_template.bot_delete_class
            file_content_router_area += server_template.bot_delete_router
            continue
        if need == "bot-settings":
            file_content_var_area += server_template.bot_settings_var
            file_content_class_area += server_template.bot_settings_class
            file_content_router_area += server_template.bot_settings_router
            continue
        if need == "user-join":
            file_content_var_area += server_template.user_join_var
            file_content_class_area += server_template.user_join_class
            file_content_router_area += server_template.user_join_router
            continue
        if need == "user-leave":
            file_content_var_area += server_template.user_leave_var
            file_content_class_area += server_template.user_leave_class
            file_content_router_area += server_template.user_leave_router
            continue
    file_content_router_area += server_template.router_footer
    file_content += file_content_var_area
    file_content += file_content_class_area
    file_content += file_content_router_area
    file_content += server_template.server_start
    with open(f"{root_dir}/Server.py", "w", encoding="utf-8") as server_file:
        server_file.write(file_content)
    print("Server Created")

if config['allow-plugin'] == True:
    print("Creating plugin directory...")