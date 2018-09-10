# -*- coding:utf-8 -*-
import paramiko
import os
import sys
from config import config

def upload_file(local_path, server_path):
	try:
		t = paramiko.Transport((config.hostname, config.port))
		t.connect(username=config.username, password=config.password)
		sftp = paramiko.SFTPClient.from_transport(t)
		# 这里的os.path.join 只是个人需要 可以直接sftp.put(local_file_path, remote_file_path)
		sftp.put(local_path, server_path)
		t.close()
		return True
	except Exception as e:
		print(e)

