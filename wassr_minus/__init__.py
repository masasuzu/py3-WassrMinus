#!python3
#coding: utf8

import json
import urllib.parse
import urllib.request
import wassr_minus.api_uri

REALM    = 'API Authentication'
LOCATION = 'http://api.wassr.jp:80'

class WassrMinus(object):
    '''
    ひんそーなクライアント
    '''

    def __init__(self, user=None, password=None, source='pyWassr'):
        self.user     = user
        self.password = password
        self.source   = source
        self._connect()

    def _connect(self):
        '''
        HTTPコネクションを張る
        '''
        auth_handler = urllib.request.HTTPBasicAuthHandler()
        auth_handler.add_password(
            realm  = REALM,
            uri    = LOCATION,
            user   = self.user,
            passwd = self.password
        )
        opener = urllib.request.build_opener(auth_handler)
        opener.addheaders = [('User-agent', 'Pyhon Wassr Client')]
        urllib.request.install_opener(opener)

    def user_timeline(self, id=None):
        if id != None:
            uri = wassr_minus.api_uri.USER_TIMELINE + '?id=%s' % id
        else:
            uri = wassr_minus.api_uri.USER_TIMELINE

        return self.get_status(uri)

    def friends_timeline(self):
        return self.get_status(wassr_minus.api_uri.FRIENDS_TIMELINE)

    def public_timeline(self):
        return self.get_status(wassr_minus.api_uri.PUBLIC_TIMELINE)

    def replies(self):
        return self.get_status(wassr_minus.api_uri.REPLIES)

    def show(self, id=None):
        if id != None:
            uri = wassr_minus.api_uri.SHOW + '?id=%s' % id
        else:
            uri = wassr_minus.api_uri.SHOW

        return self.get_status(uri)

    def get_status(self, uri):
        return json.loads(urllib.request.urlopen(uri).read().decode('utf8', 'ignore'))

    def update(self, comment=None):
        if comment == None:
            raise Exception('not defined comment')

        params = urllib.parse.urlencode({'source': self.source, 'status': comment})
        urllib.request.urlopen(wassr_minus.api_uri.UPDATE, params)


