import os
import unittest
from unittest.mock import patch, MagicMock

from ipstack import *


def get_env_variable(var_name):
    """
    Retrieve a variable from the environment or raise an exception.
    """
    try:
        return os.environ.get(var_name)
    except KeyError:
        error_msg = "Set the {} environment variable.".format(var_name)
        raise EnvironmentError(error_msg)


class IPTestCase(unittest.TestCase):
    ACCESS_KEY = get_env_variable('IPSTACK_ACCESS_KEY')
    TEST_IP_ADDRESS = "103.3.61.114"
    TEST_IP_ADDRESS2 = "231.34.31.102"

    def test_init(self):
        ip = IP(self.TEST_IP_ADDRESS, self.ACCESS_KEY)
        self.assertEqual(ip.continent_code, 'AS')
        self.assertEqual(ip.continent_name, 'Asia')
        self.assertEqual(ip.country_code, 'SG')
        self.assertEqual(ip.country_name, 'Singapore')
        self.assertEqual(ip.region_code, None)
        self.assertEqual(ip.region_name, None)
        self.assertEqual(ip.city, 'Singapore')
        self.assertEqual(ip.latitude, 1.2929)
        self.assertEqual(ip.longitude, 103.8547)
        self.assertEqual(ip.security, None)

    def test_get_ip_address_from_headers(self):
        headers = {'X-Forwarded-For': ",".join([self.TEST_IP_ADDRESS, self.TEST_IP_ADDRESS2])}
        ip_address = IP.get_ip_address_from_headers(headers)
        self.assertEqual(ip_address, self.TEST_IP_ADDRESS)

    def test_lookup_ip_info(self):
        json = IP.lookup_ip_info(self.TEST_IP_ADDRESS, self.ACCESS_KEY)
        self.assertIn('ip', json)
        self.assertEqual(json['ip'], self.TEST_IP_ADDRESS)

    @patch.object(requests, 'get')
    def test_lookup_ip_info__http_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=400)
        with self.assertRaises(requests.HTTPError):
            json = IP.lookup_ip_info(self.TEST_IP_ADDRESS, self.ACCESS_KEY)
