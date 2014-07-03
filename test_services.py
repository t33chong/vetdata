from nlp_services.caching import use_caching
from nlp_services.syntax import WikiToPageHeadsService
from nlp_services.discourse.entities import WikiPageToEntitiesService
from pprint import pprint

use_caching(shouldnt_compute=True)


def heads(wid):
    #pprint(WikiToPageHeadsService().get_value(wid, {}))
    return WikiToPageHeadsService().get_value(wid, {})


def entities(wid):
    #pprint(WikiPageToEntitiesService().get_value(wid, {}))
    return WikiPageToEntitiesService().get_value(wid, {})
