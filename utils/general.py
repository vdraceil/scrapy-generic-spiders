import re

from constants import Regex


class URLUtils(object):
    @staticmethod
    def get_domain_from_url(url):
        match = Regex.PT_DOMAIN_FROM_URL.match(url)
        if not match:
            raise InvalidArgumentError('Invalid URL: ' + url)
        # always filter by the complete domain name (including the prefix)
        # strip the domain prefix of the common prefixes 'www', 'www2', etc.
        domain_prefix = match.group(1) or ''
        if domain_prefix.startswith('www'):
            domain_prefix = domain_prefix[(domain_prefix.find('.')+1):]
        domain = '%s.%s' %(match.group(2), match.group(3))
        return domain_prefix + domain 

    @staticmethod
    def get_complete_url(url):
        # add '/' to the end of URLs which have no trailing path
        # for consistency
        match = Regex.PT_COMPLETE_URL.match(url)
        if match:
            if not match.group(1):
                url += '/'
        else:
            raise InvalidArgumentError('Invalid URL: ' + url)
        return url

    @staticmethod
    def simplify(uri):
        # eliminate any hash tag locations
        if '#' in uri:
            uri = uri[:uri.index('#')]
        # eliminate all numbers from the params
        # a measure to prevent us getting into spider traps
        if '?' in uri:
            index = uri.index('?')
            url = uri[:index]
            params = re.sub('\d', '', uri[index+1:])
            uri = '%s?%s' %(url, params)
        return uri


class InvalidArgumentError(Exception): pass