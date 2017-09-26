"""Mapping hass.io options.json into configurator config."""
import json
from pathlib import Path
import sys

hassio_options = Path("/data/options.json")

# Read hass.io options
with hassio_options.open('r') as json_file:
    options = json.loads(json_file.read())

configurator = {
    'BASEPATH': "/config",
    'HASS_API': options['homeassistant_api'],
    'HASS_API_PASSWORD': options['homeassistant_password'],
    'CREDENTIALS': options['credentials'],
    'SSL_CERTIFICATE': options['certfile'] if options['ssl'] else None,
    'SSL_KEY': options['keyfile'] if options['ssl'] else None,
    'ALLOWED_NETWORKS': options['allowed_networks'],
    'BANNED_IPS': options['banned_ips'],
    'IGNORE_PATTERN': options['ignore_pattern'],
}

with Path(sys.argv[1]).open('w') as json_file:
    json_file.write(json.dumps(configurator))
