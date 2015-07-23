# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize
from Products.CMFCore.utils import getToolByName
from zope.site.hooks import getSite


class PaginaInicialView(BrowserView):
    """ view da pagina inicial
    """

    __call__ = ViewPageTemplateFile('templates/paginainicial.pt')

    @memoize
    def getDestaques(self):
        catalog = getToolByName(self, 'portal_catalog')
        destaque_forlder = getSite().absolute_url_path() + '/eventos'
        items = catalog(path=destaque_forlder,
                            portal_type="Noticia",
                            review_state="published",
                            sort_on="getObjPositionInParent")
        if items:
            return items

    @memoize
    def getSubDestaques(self):
        catalog = getToolByName(self, 'portal_catalog')
        destaque_forlder = getSite().absolute_url_path() + '/eventos'
        items = catalog(path=destaque_forlder,
                            portal_type="Noticia",
                            review_state="published",
                            sort_on="getObjPositionInParent")
        if items:
            return items[:4]