# -*- coding: utf-8 -*-

from ..base import ComponentAPI


class CollectionsF5BIGIP(object):
    """Collections of SOPS APIS"""

    def __init__(self, client):
        self.client = client

        self.ltm = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi/f5_bigip/ltm/',
            description=u'f5'
        )
