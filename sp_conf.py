from saml2.entity_category.edugain import COC
from saml2 import BINDING_HTTP_REDIRECT
from saml2 import BINDING_HTTP_POST
from saml2.saml import NAME_FORMAT_URI

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None


if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin","/usr/local/bin"])
else:
    xmlsec_path = '/usr/local/bin/xmlsec1'

# Make sure the same port number appear in service_conf.py
BASE = "http://localhost:8000"

CONFIG = {
    "entityid": "%s/esa-sso/metadata/" % BASE,
    'entity_category': [COC],
    "description": "Example SP",
    "service": {
        "sp": {
            "want_response_signed": False,
            "authn_requests_signed": False,
            "logout_requests_signed": False,
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/esa-sso/acs/" % BASE, BINDING_HTTP_POST)
                ],
                "single_logout_service": [
                    ("%s/accounts/sso_logout/" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/accounts/sso_logout/" % BASE, BINDING_HTTP_POST),
                ],
            }
        },
    },
    "key_file": "pki/mykey.pem",
    "cert_file": "pki/mycert.pem",
    "xmlsec_binary": xmlsec_path,
    "metadata": {"local": ["idp.xml"]},
    "name_form": NAME_FORMAT_URI,
}
