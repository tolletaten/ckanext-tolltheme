import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import uuid

from ckan.lib.plugins import DefaultTranslation
from ckan.common import config
from collections import OrderedDict

# Token that can be added as parameter to static resources, to force the browser to refresh them after a ckan restart.
token = uuid.uuid4().hex


# Adds a version token to a URL.
def url_with_version_token(url):
    return url + ('?' if '?' not in url else '&') + 'v=' + token


class TollthemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.ITemplateHelpers)

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

    # ITemplateHelpers
    def get_helpers(self):
        return {'tolltheme_url_with_version_token': url_with_version_token}
