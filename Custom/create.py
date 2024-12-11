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
    print("Creating server plugin...")

if config['allow-plugin'] == True:
    print("Creating plugin directory...")