# -*- coding: utf-8 -*-
"""
.. module:: .resultitem.py
    :synopsis: ResultItem class

.. moduleauthor:: Arthur Moore <arthur.moore85@gmail.com>
.. creation date:: 04-11-2017
.. licence:: 
"""
from __future__ import unicode_literals

__author__ = "arthur"

JAPAN = 'Japan'
EU = 'Europe'
USA = 'USA'

COUNTRIES = {
    '(JPN)': JAPAN,
    '(JAPAN)': JAPAN,
    '(J)': JAPAN,
    '(EU)': EU,
    '(EUROPE)': EU,
    '(E)': EU,
    '(USA)': USA,
    '(U)': USA
}


class ResultItem(object):
    """
    ResultItem object.
    """
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.has_country = False
        self.country = 'Unknown'
        self.download_url = kwargs.get('download_url') + '-download'
        self.system_id = kwargs.get('system_id')
        self.system = self._clean_system(kwargs.get('system'))
        self.filesize_gb = 0
        self.filesize_mb = 0
        self.filesize_kb = 0
        self.name = self._clean_name(kwargs.get('name'))
        self.download_id = self._get_download_id()

        self._clean_filesize(kwargs.get('filesize'))

    def __repr__(self):
        return '<ResultItem: {0} - {1}>'.format(self.id, self.name)

    def _clean_system(self, system_name):
        """
        Cleans up the System name display.
        This is because by default, it returns with horrible
        extra garbage like (SNES) which is totally unnecessary.
        """
        if not system_name:
            # In case the system name was
            # not supplied to ResultItem
            return None

        cleaned = system_name.split('(')[0]
        return cleaned

    def _clean_name(self, name):
        """
        Cleans up the title name.
        This is done because by default, lots of titles come with
        'ROM' or other rubbish that is of no use.
        """
        countries = ('(JPN)', '(USA)', '(EU)', '(JAPAN)', '(EUROPE)', '(E)', '(U)', '(J)')

        if not name:
            # In case the name was not supplied to ResultItem.
            return None

        for country in countries:
            if country in name.upper():
                self.has_country = True
                self.country = COUNTRIES[country]
                name = name.replace(country, '')
                break

        if 'ROM' in name:
            name = name.replace('ROM', '')

        name = name.split('(')[0]

        return name

    def _clean_filesize(self, filesize):
        """
        Sets the filesizes.
        """
        filesize = filesize.upper()
        if '.' in filesize:
            first_val, second_val = filesize.split('.')
            denom_type = second_val[-1]
            second_val = second_val[:-1]

            first_val = int(first_val)
            second_val = int(second_val)
        else:
            denom_type = filesize[-1]
            first_val = int(filesize[:-1])
            second_val = 0

        if denom_type == 'K':
            self.filesize_kb = first_val
        if denom_type == 'M':
            self.filesize_mb = first_val
            self.filesize_kb = second_val * 100
        if denom_type == 'G':
            self.filesize_gb = first_val
            self.filesize_mb = second_val * 100

    def _get_download_id(self):
        """
        Returns a Download ID if possible (Emuparadise)
        """
        code = self.download_url.split('/')[-1]
        try:
            return int(code)
        except ValueError:
            return None
