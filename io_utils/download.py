"""
:module: download.py
:description: Downloading module

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 31/12/16
"""
from .directory_utils import Directories
from .platform_io import PlatformBase

__author__ = 'arthur'


class Download(PlatformBase):
    """
    Downloads a ROM/Game
    """
    def __init__(self, *args, **kwargs):
        self.url = None
        self.dirs_obj = Directories()
        self.search = kwargs.get('search')
        super(Download, self).__init__()

    def download(self, rom_url):
        """
        Downloads the ROM
        """
        platform = " ".join(rom_url.split('/')[3].replace('_', ' ').split()[:-1])
        target = self.dirs_obj.target_directory(self.download_location, platform)
        self.search.download(rom_url, target)
