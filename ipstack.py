"""
Small python library for the request and response to ipstack.com
https://ipstack.com/documentation
"""

from typing import Optional

import requests


class IP():

    def __init__(self, ip_address: str, ip_stack_api_key: str, include_security=True):
        """
            :exception
                KeyError, ValueError
        """
        self.ip_address = ip_address
        result = self.lookup_ip_info(ip_address, ip_stack_api_key)

        self.continent_code: Optional[str] = result['continent_code']
        self.continent_name: Optional[str] = result['continent_name']
        self.country_code: Optional[str] = result['country_code']
        self.country_name: Optional[str] = result['country_name']
        self.region_code: Optional[str] = result['region_code']
        self.region_name: Optional[str] = result['region_name']
        self.city: Optional[str] = result['city']
        self.zip: Optional[str] = result['zip']
        self.latitude: Optional[float] = result['latitude']
        self.longitude: Optional[float] = result['longitude']

        self.security: Optional[SecurityModule] = None
        if include_security and 'security' in result:
            self.security = SecurityModule(result)

        self.raw = result

    @staticmethod
    def get_ip_address_from_headers(headers: dict) -> Optional[str]:
        """
        Helper method to get ip address from the XFF header.

            :param
                headers: a dictionary object keyed by http header

            :exception
                KeyError if the ip address cannot be parsed from the header
        """
        try:
            return headers['X-Forwarded-For'].split(',')[0]
        except KeyError:
            return None

    @staticmethod
    def lookup_ip_info(ip_address: str, ip_stack_api_key: str, include_security=True) -> dict:
        """
        Looks up ip information from ip stack.

            :exception
                ValueError if the response cannot be json serialized
                HTTPError if ipstack does not return a 200 ok result
        """
        endpoint = "https://api.ipstack.com/{}?access_key={}".format(ip_address, ip_stack_api_key)
        if (include_security):
            endpoint += "&security=1"

        response = requests.get(endpoint)

        if (response.status_code != 200):
            raise requests.exceptions.HTTPError(response=response)

        return response.json()


class SecurityModule():

    def __init__(self, ip_info):
        security_data = ip_info['security']

        self.is_proxy: bool = security_data['is_proxy']
        self.proxy_type: Optional(str) = security_data['proxy_type']
        self.is_crawler: bool = security_data['is_crawler']
        self.crawler_name: Optional(str) = security_data['crawler_name']
        self.crawler_type: Optional(str) = security_data['crawler_type']
        self.is_tor: bool = security_data['is_tor']
        self.threat_level: Optional(str) = security_data['threat_level']
        self.threat_types: list = security_data['threat_types']


class ProxyTypes():
    CGI = "cgi"
    WEB = "web"
    VPN = "vpn"


class CrawlerTypes():
    UNRECOGNIZED = "unrecognized"
    SEARCH_ENGINE_BOT = "search_engine_bot"
    SITE_MONITOR = "site_monitor"
    SCREENSHOT_CREATOR = "screenshot_creator"
    LINK_CHECKER = "link_checker"
    WEARABLE_COMPUTER = "wearable_computer"
    WEB_SCRAPER = "web_scraper"
    VULNERABILITY_SCANNER = "vulnerability_scanner"
    VIRUS_SCANNER = "virus_scanner"
    SPEED_TESTER = "speed_tester"
    FEED_FETCHER = "feed_fetcher"
    TOOL = "tool"
    MARKETING = "marketeing"


class ThreatLevels():
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ThreatTypes():
    TOR = "tor"
    FAKE_CRAWLER = "fake_crawler"
    WEB_SCRAPER = "web_scraper"
    ATTACK_SOURCE = "attack_source"
    ATTACK_SOURCE_HTTP = "attack_source_http"
    ATTACK_SOURCE_MAIL = "attack_source_mail"
    ATTACK_SOURCE_SSH = "attack_source_ssh"
