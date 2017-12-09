# -*- coding: utf-8 -*-
"""
.. module:: .emuapi.py
    :synopsis: EmuParadise API

.. moduleauthor:: Arthur Moore <arthur.moore85@gmail.com>
.. creation date:: 27-10-2017
.. licence:: 
"""
from __future__ import unicode_literals

import HTMLParser

from api.base import Api

__author__ = "arthur"

ENDPOINTS = {
    'search': '/roms/search.php'
}


class EmuApi(Api):
    """
    EmuParadise API.
    This provides an easy to use API to connect to EmuParadise,
    and extract information and data from the website.
    """
    def __init__(self):
        super(EmuApi, self).__init__()
        self.service = 'EmuParadise'
        self.base_url = 'https://www.emuparadise.me'
        self.referrer = None
        self._parser = HTMLParser.HTMLParser()
        self.endpoints = ENDPOINTS
        self.response = self.get_response()
        self.search_regex = '<div class="roms">' \
                            '<a .*?href="(.*?)">(.*?)</a>.*?' \
                            '<a href="\/roms\/roms\.php\?sysid=(\d+)".*?class="sysname">' \
                            '(.*?)</a>.*?<b>Size:</b> (.*?) .*?</div>'
        self.download_url = 'http://direct.emuparadise.me/roms/get-download.php?gid={download_id}' \
                            '&token={token}' \
                            '&mirror_available=true'
        self.requires_arguments = True
        self.token = '211217baa2d87c57b360b9a673a12cfd'

    def get_download_url(self, item):
        """
        Download the selected ROM
        :param item: ResultItem object.
        """
        return self.base_url + item.download_url
