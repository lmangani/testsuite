'''
Copyright (C) 2013, Digium, Inc.
David M. Lee, II <dlee@digium.com>

This program is free software, distributed under the terms of
the GNU General Public License Version 2.
'''

import logging

logger = logging.getLogger(__name__)

id = None


def on_start(ari, event):
    logger.debug("on_start(%r)" % event)
    global id
    id = event['stasis_start']['channel']['uniqueid']
    ari.post('channels', id, 'continue')
    return True


def on_end(ari, event):
    global id
    logger.debug("on_end(%r)" % event)
    return id == event['stasis_end']['channel']['uniqueid']


def on_second_start(ari, event):
    global id
    logger.debug("on_second_start(%r)" % event)
    ari.delete('channels', id)
    return id == event['stasis_start']['channel']['uniqueid']
