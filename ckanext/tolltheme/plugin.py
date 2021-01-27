import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckan.lib.plugins import DefaultTranslation
from ckan.common import config
from collections import OrderedDict


class TollthemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.ITranslation)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'tolltheme')

    # IFacets

    def dataset_facets(self, facets_dict, package_type):
        # 'Stikkord' and 'Formater' in Norwegian.
        default_included_facets = ['tags', 'res_format']
        # Gets the facets from config properties, if property is defined. Otherwise sets to default values.
        included_facets = toolkit.aslist(config.get('tolltheme.dataset.filters', default_included_facets))
        if '*' in included_facets:
            return facets_dict

        facets = OrderedDict()
        for key, value in facets_dict.items():
            if key in included_facets or value in included_facets:
                facets[key] = value
        return facets
