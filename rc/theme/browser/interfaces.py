# -*- coding: utf-8 -*-
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IRCTheme(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Tema RC" theme, this interface must be its layer
       (in theme/viewlets/configure.zcml).
    """


class IRCNoticia(Interface):
    """Marker interface
    """
