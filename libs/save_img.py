#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/2/3 11:31
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : save_img.py
import os
import urllib.request


def save_img(img_url, file_name, file_path='img'):
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 img文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹', file_path, '不存在，重新建立')
            os.makedirs(file_path)  # os.mkdir(file_path)

        tmp_path = file_path + '/' + file_name
        if not os.path.exists(tmp_path):
            # 获得图片后缀，splitext 可以将文件与扩展名分开
            file_suffix = os.path.splitext(img_url)[1]
            filename = '{}{}{}{}'.format(
                file_path, os.sep, file_name, file_suffix)  # 拼接图片名（包含路径）
            urllib.request.urlretrieve(
                img_url, filename=filename)  # 下载图片，并保存到文件夹中
            # print('小票下载成功')
        else:
            pass
            # print('小票已存在，不下载')
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)
