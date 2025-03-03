import requests
import sys
import json

class Zetalytics(object):
    """
    You can preconfigure all services globally with a ``config`` dict.
    Example::
        zl = Zetalytics(token='AABBCCDDEEFFGG')
    """

    def __init__(self, **kwargs):
        self.requester = requests.session()
        self.config = {
            'base_url': 'https://zonecruncher.com/api/v2/'
        }
        self.config.update(kwargs)
        if len(self.config.get('token')) != 32:
            #TODO: Figure out server response for wrong API token
            raise ValueError("Incorrect API token provided")
        self.set_token(self.config.get('token'))
        self.__set_params(self.config)

    def set_token(self, token):
        if token:
            self.requester.params['token'] = token

    def __set_params(self, config):
        if config.get('verbose'):
            self.requester.config = {'verbose': config['verbose']}
        if config.get('timeout'):
            self.requester.timeout = config['timeout']

    def check_integrity(self, arg_dict, **params):
        for k, v in params.items():
            if k not in arg_dict and v['required']:
                raise ValueError("Missing required parameter " + k)
            elif k not in arg_dict:
                raise ValueError("Unknown parameter " + k)
            elif k in arg_dict:
                #print(arg_dict[k])
                if arg_dict[k]['constraints']:
                    for _k, _v in arg_dict[k]['constraints'].items():
                        if _k == 'length':
                            if not len(v) == _v:
                                raise ValueError("Parameter " + k + " does not have a length of " + str(_v['length']))
                        if _k == 'range':
                            if not _v[0] <= int(v) <= _v[1]:
                                raise ValueError(
                                    "Parameter " + k + " is not in allowed range of " + str(_v[0]) + "-" + str(_v[1]))
                        if _k == 'multi':
                            #print(v)
                            #print(_v)
                            if v not in _v:
                                raise ValueError("Parameter " + v + " in " + k + " is not an allowed value")
        return True

    def dateToEpoch(self, date):
        pass

    def cname2qname(self, **params):
        """
            Params;
            q: Domain name
            toBaseDomain: Boolean, if true convert to base domain
            noSubdomains: Exclude subdomain matches
            size: Result size
            start: Epoch time to start search from
            end: Epoch time to end search at
            tsfield: Shows first seen, last seen, or both 'multi': ["first_seen", "first_ts", "last_seen", "last_ts", "all"]
        """
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain_zone_activity(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2aaaa(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2cname(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2d8s(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'live': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'fast': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2ip(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2mx(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2ns(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2nsglue(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2ptr(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2rrtypes(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'rrtypes': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2txt(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def domain2whois(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 1000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def email_address(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def email_domain(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def email_user(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def hostname(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def ip(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_seen", "last_ts", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def ip2nsglue(self, **params):
        params.update(token=self.config.get('token'))
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def ip2pwhois(self, **params):
        params.update(token=self.config.get('token'))
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def liveDNS(self, **params):
        params.update(token=self.config.get('token'))
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def mx2domain(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'noSubdomains': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def ns_zone_activity(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_','-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def ns2domain(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }
        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    def subdomains(self, **params):
        endpoint = sys._getframe().f_code.co_name
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'active': {'type': 'Integer', 'constraints': None, 'required': False},
                        'days': {'type': 'Integer', 'constraints': None, 'required': False},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'v': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'vv': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'vvv': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'sort': {'type': 'String',
                                 'constraints': {'multi': ["first", "last", "first:desc", "last:asc"]},
                                 'required': False},
                        't': {'type': 'String',
                              'constraints': {
                                  'multi': ["a", "aaaa", "cname", "mx", "name", "ns", "ptr", "soa_email", "soa_server",
                                            "txt"]},
                              'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {'multi': ["first_seen", "first_ts", "last_seen", "last_ts", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            if 'endpoint' in params:
                return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)
            else:
                return json.loads(self.requester.get(self.config['base_url'] + endpoint, params=params).text)

    # FIXME - Document function name, which does not match api 1k-maps-term
    def one_k_maps_term(self, **params):
        #endpoint = sys._getframe().f_code.co_name
        endpoint = '1k-maps-term'
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'domain': {'type': 'String', 'constraints': None, 'required': False},
                        'ns': {'type': 'String', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def arin_ips(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def arin_originAS(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def cert_domain(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                    'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def cert_fingerprint(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                        'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def cert_full_text_domain(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                        'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def dname2ns_intersection(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'v': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'noActive': {'type': 'Boolean', 'constraints': None, 'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def full_text_rname(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def ip2torexit(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'flags': {'type': 'String', 'constraints': None, 'required': False},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def name2torexit(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'flags': {'type': 'String', 'constraints': None, 'required': False},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def ns_intersection(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'domain': {'type': 'String', 'constraints': None, 'required': False},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'v': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'first_seen_start': {'type': 'String', 'constraints': None, 'required': False},
                        'first_seen_end': {'type': 'String', 'constraints': None, 'required': False},
                        'last_seen_start': {'type': 'String', 'constraints': None, 'required': False},
                        'last_seen_end': {'type': 'String', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def owner2whois(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def ptr_by_ip(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                        'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def ptr_by_term(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                        'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def soa_dname(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'noActive': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                    'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def soa_qname(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'toBaseDomain': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'noActive': {'type': 'Boolean', 'constraints': None, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                    'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)

    def soa_rname(self, **params):
        endpoint = sys._getframe().f_code.co_name.replace('_', '-')
        args_allowed = {'q': {'type': 'String', 'constraints': None, 'required': True},
                        'token': {'type': 'String', 'constraints': {'length': 32}, 'required': True},
                        'size': {'type': 'Integer', 'constraints': {'range': [0, 100000]}, 'required': False},
                        'start': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'end': {'type': 'Epoch', 'constraints': None, 'required': False},
                        'endpoint': {'type': 'String', 'constraints': None, 'required': True},
                        'tsfield': {'type': 'String',
                                    'constraints': {
                                        'multi': ["first_seen", "first_ts", "date", "last_ts", "last_seen", "all"]},
                                    'required': False}
                        }

        if (self.check_integrity(args_allowed, **params)):
            return json.loads(self.requester.get(params['endpoint'] + endpoint, params=params).text)