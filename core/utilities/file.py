import configparser
from typing import Any

import paramiko
import xlrd


# 与文件有关的操作，包括针对不同格式的文件的读取、远程文件的下载及上传


def load_ini(file_path: str) -> Any:
    """
    加载 ini 文件
    """
    ini_data = configparser.ConfigParser()
    ini_data.read(file_path, encoding='utf-8')
    return ini_data


def load_ini_key(ini_content, section, key):
    """
    加载 ini 的值
    以 section 定位到是什么 [] 下的内容
    以 key 定位到 键值对
    """
    ini_sections = ini_content.sections()
    if section not in ini_sections:
        return None
    return ini_content.get(section, key)


def load_worksheet_by_index(workbook, index):
    """
    通过 索引号 index 读取 Excel 中的工作簿
    """
    with xlrd.open_workbook(filename=workbook) as f:
        sheet = f.sheet_by_index(index)
    return sheet


def load_worksheet_by_name(workbook, name):
    """
    通过 工作簿的名称 读取 Excel 中的工作簿
    注：在 Excel 中，工作簿的名字唯一
    """
    with xlrd.open_workbook(filename=workbook) as f:
        sheet = f.sheet_by_name(name)
    return sheet


def load_remote_file_lines(hostname, port, username, password, path):
    """
    获取远程文件，并以列表的形式返回，每一行为列表的一个字段

    需要提供：服务器IP，服务器端口，用户名，密码，文件路径（包含文件名）
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, password, compress=True)
    sftp_client = client.open_sftp()
    remote_file = sftp_client.open(path)
    lines = remote_file.readlines()
    remote_file.close()
    sftp_client.close()
    client.close()
    return lines


def upload_file_to_remote(hostname, port, username, password, remote_path, local_path):
    """
    上传本地文件到远程服务器中

    需要提供：服务器IP，服务器端口，用户名，密码，远程存放文件的地址（包含文件名），本体文件的路径
    存在权限问题，使用普通用户角色无法将文件上传到特定的路径下
    """
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath=local_path, remotepath=remote_path)
    sftp.close()
    transport.close()
