import os
from datetime import datetime

def make_log_dir():
    if not os.path.exists("./log"):
        os.makedirs("./log")

def write_log(log):
    today = datetime.now()
    file_path = "./log/" + today.strftime("%Y年%m月%d日") + ".txt"
    f = open(file_path, mode="a")
    f.writelines(log)
    f.write("\n")
    f.close()
