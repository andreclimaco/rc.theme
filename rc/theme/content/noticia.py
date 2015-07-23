# -*- coding: utf-8 -*-

# Zope3 imports
from zope.interface import implements

# Security
from AccessControl import ClassSecurityInfo

# Archetypes & ATCT imports
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin

from rc.theme import config
from rc.theme import MessageFactory as _
from rc.theme.browser.interfaces import IRCNoticia

# Schema definition
schema = ATNewsItem.schema.copy()

schema['image'].sizes = {
    'large': (768, 768),
    'preview': (400, 400),
    'mini': (200, 200),
    'thumb': (128, 128),
    'tile': (64, 64),
    'icon': (32, 32),
    'listing': (16, 16),
    'slider_home': (940, 460),
    'sub_destaque_home': (200, 150),
    }

schemata.finalizeATCTSchema(schema)


class RCNoticia(ATNewsItem, HistoryAwareMixin):
    """Noticia
    """

    security = ClassSecurityInfo()
    implements(IRCNoticia)

    meta_type = 'Noticia'
    portal_type = 'Noticia'

    _at_rename_after_creation = True

    schema = schema

    # Metodos

atapi.registerType(RCNoticia, config.PROJECTNAME)
