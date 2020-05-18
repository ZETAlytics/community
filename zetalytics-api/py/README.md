# zetalytics-api

A straightforward python library for the Zetalytics Zonecruncher API.  For a list of all endpoints and query parameters, refer to the [API documentation](https://zonecruncher.com/api-v1-docs/).

Use of the Zetalytics API and zetalytics-api client requires a user token.  You can request one [here](https://zetalytics.com/feb20/hands-on.html).

## Installation

To install zetalytics-api, use Pypi via pip.

```
pip install zetalytics-api
```


## Initialization

```
from zetalytics import Zetalytics

zeta = Zetalytics(token=[YOUR USER TOKEN])
```

## Examples

### domain2ns
Search passive dns by domain for NS records
```
query = {'q': 'example.com'}
zeta.domain2ns(**query)
```

### email_address
Search for domains sharing a registration email address or SOA email from passive
```
query = {'q': 'johndoe@example.com', 'size': 10}
zeta.email_address(**query)
```

###
Search passive dns by IP, CIDR, or Range (v6 compatible)
```
query = {'q': '1.2.3.4', 'tsfield': 'first_seen', 'start': '2019-01-01', 'size': 100}
zeta.ip(**query)
```

## License
This project is licensed under the GNU General Public License v3.0.