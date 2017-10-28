# -*- coding: utf-8 -*-
"""
.. module:: .base.py
    :synopsis: Base API class for dealing with various API's

.. moduleauthor:: Arthur Moore <arthur.moore85@gmail.com>
.. creation date:: 27-10-2017
.. licence:: 
"""
from __future__ import unicode_literals

from bs4 import BeautifulSoup

import re
import requests

from .exceptions import handle_response_codes

__author__ = "arthur"


class Api(object):
    def __init__(self, *args, **kwargs):
        self.service = None
        self.base_url = None
        self.status_code = None
        self.config = None
        self.content = None
        self.current_url = None
        self.response = None
        self.search_regex = None
        self.referrer = None
        self.endpoints = {}

    def get_response(self):
        """
        Initial request.
        :return: request object.
        """
        if self.current_url:
            url = self.current_url
        else:
            url = self.base_url
        r = requests.get(url)
        self.status_code = r.status_code

        if self.status_code == 200:
            self.content = r.content
            return r
        else:
            handle_response_codes(self.status_code)

    def _site_request(self, follow=True, data=None):
        url = self.current_url
        extra = dict(cookies=dict(downloadcaptcha='1'))
        if self.referrer is not None:
            extra['headers'] = dict(referer=self.referrer)
        if not follow:
            extra['allow_redirects'] = False
        if data is not None:
            extra['params'] = data
        self.referrer = url
        return requests.get(url, **extra)

    def search(self, query, system=0):
        """
        Searches URL for media.
        :param query: Search query
        :param system: System type
        :return: Dictionary of results.
        """
        return re.findall(
            self.search_regex,
            self._site_request(
                self.endpoints.get('search'),
                data=dict(query=query, section='roms', sysid=system)
            ).content
        )
