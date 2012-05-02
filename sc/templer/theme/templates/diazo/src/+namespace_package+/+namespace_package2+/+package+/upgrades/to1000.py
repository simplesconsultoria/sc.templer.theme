# -*- coding: utf-8 -*-

import logging
from collective.grok import gs


@gs.upgradestep(title=u'Initial upgrade step',
                description=u'Upgrade step run at install time',
                source='0.0', destination='1000', sortkey=1,
                profile='beyondskins.cerelatino.site:default')
def to1000(context):
    """ Upgrade from Zero to version 1000
    """
    pass
