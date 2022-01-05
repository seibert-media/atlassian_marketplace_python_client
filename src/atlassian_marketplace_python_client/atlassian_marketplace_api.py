import logging
import requests
import json

from atlassian_marketplace_python_client.settings import ATLASSIAN_MARKETPLACE_VENDOR_URL


logger = logging.getLogger(__name__)


class AtlassianMarketplaceTimeoutException(Exception):

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return f'Timeout {self.response.status_code} - {self.response.text} beim Zugriff auf {self.response.url}'


class AtlassianMarketplaceNotFound(Exception):

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return f'Couldn\'t find Entity {self.response.status_code} - {self.response.text} while requesting {self.response.url}'


class AtlassianMarketplaceAPI:

    def __init__(self):
        self.session = requests.Session()

    def _get_request(self, url):
        response = []

        try:
            response = self.session.get(url)

            if response.status_code == requests.codes.TIMEOUT:
                raise AtlassianMarketplaceTimeoutException(response)

        except AtlassianMarketplaceTimeoutException as marketplace_timeout:
            logger.log(40, str(marketplace_timeout))

        return response

    def _get_and_parse_products_to_json(self, url):
        products = self._get_request(url)
        products_as_json = json.loads(products.content)

        return products_as_json

    def get_all_products_of_vendor(self, vendor_id):
        products = []

        all_products_as_json = self._get_and_parse_products_to_json(ATLASSIAN_MARKETPLACE_VENDOR_URL + str(vendor_id))
        product_count = all_products_as_json.get('count', 0)

        if all_products_as_json:

            for i in range(0, product_count, 10):
                all_products_as_json.update(
                    self._get_and_parse_products_to_json(
                        ATLASSIAN_MARKETPLACE_VENDOR_URL +
                        str(vendor_id) + '?offset=' +
                        str(i)
                    )
                )
                products.extend(all_products_as_json['_embedded']['addons'])

        return products

    def get_all_product_names_of_vendor(self, vendor_id):
        product_names = []

        all_products = self.get_all_products_of_vendor(vendor_id)

        for product in all_products:
            if 'name' in product:
                product_names.append(product['name'])

        return product_names
