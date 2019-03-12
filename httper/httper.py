#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/1 16:10
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : httper.py
import requests

from config import USER_AGENT, CONTENT_TYPE, REQUESTS_COOKIES, LANGUAGE, COOKIE, HTTP_HEADERS
from libs import cookie_to_dict


class HTTP:
    user_agent = USER_AGENT
    language = LANGUAGE
    content_type = CONTENT_TYPE
    cookies = cookie_to_dict(REQUESTS_COOKIES)
    cookie = COOKIE

    @classmethod
    def make_session(cls):
        session = requests.session()
        session.headers.update(
            {"User-Agent": cls.user_agent, 'Content-Type': cls.content_type})
        requests.utils.add_dict_to_cookiejar(
            session.cookies, cookie_dict=cls.cookies)
        return session

    @staticmethod
    def make_session2():
        session = requests.session()
        session.headers.update(HTTP_HEADERS)
        print(session.headers.values())
        return session


if __name__ == '__main__':
    http = HTTP()
    http.make_session2()
