import os
import importlib
from src.config import appium_config, npm_config, db_config

# global 변수 지정
npm_config()
# appium_config()
db_config()


# 해당 문구로 끝나는 파일 import
def import_all_ends_with(ends_with: str):
    for root, dirs, files in os.walk("./src"):
        for file in files:
            if file.endswith(ends_with):
                controller_path = os.path.join(root, file)
                # reformat
                controller_path = controller_path.replace('./', '', 1)
                controller_path = controller_path.replace('/', '.')
                controller_path = controller_path.replace('.py', '', 1)
                # import
                importlib.import_module(controller_path)


# controller import
import_all_ends_with('controller.py')
# thread import
# import_all_ends_with('thread.py')
