# -*- coding: utf-8 -*-
"""Html5 Video player plugin."""

import re

import requests
from urllib import parse

from video_xblock.backends.html5 import Html5Player


class TrowebPlayer(Html5Player):
    """
    TrowebPlayer is used for videos by providing direct URL.
    """

    # url_re = url_re = re.compile(r'^(?P<protocol>https?|ftp)://[^\s/$.?#].[^\s]*.(?P<extension>mpeg|mp4|ogg|webm)')
    url_re = re.compile(r"(.+)\.(troweb.app\/api\/v1\/blob)\/(?P<media_id>.*)")

    def get_direct_link(self):
        response = requests.request("HEAD", self.xblock.href, allow_redirects=False)
        return response.headers.get("Location")

    def get_type(self, href):
        """
        Get file extension for video.js type property.
        """
        url = self.get_direct_link()
        qs = parse.parse_qs(parse.urlsplit(url).query)
        return qs.get('response-content-type')[0]
