# Changelog

## 8.3

- Update Home Assistant CLI to 4.0.1
- Add backward compatibility with the hassio command
- Update Web terminal to ttyd 1.6.0 with Libwebsockets 3.2.2
- Rename HASSIO_TOKEN to SUPERVISOR_TOKEN in shell profile

## 8.2

- Fix creation of new tmux terminal windows
- Add add-on icon
- Update welcome logo
- Fix SSH folder issue with authorized keys

## 8.1

- Fix for non existing .bash_profile startup error
- Add current, short, path to command line prompt

## 8.0

- Add support for a web-based terminal via Ingress
- Upgrade Alpine Linux to 3.11
- Improve Hass.io API token handling
- Persist .ssh folder across restarts
- Add helper symlink folders to user home folder

## 7.1

- Update Hass.io CLI to 3.1.1

## 7.0

- Added bash_profile as a persistent file

## 6.4

- Changed logging from DEBUG -> INFO

## 6.3

- Update Hass.io CLI to 3.1.0

## 6.2

- Update Hass.io CLI to 3.0.0

## 6.1

- Update Hass.io CLI to 2.3.0

## 6.0

- Update and pin base image to Alpine 3.10

## 5.6

- Fixes crash when using authorized keys

## 5.5

- Rewrite add-on onto Bashio
- Added documentation to add-on repository
- Code styling improvements

## 5.4

- Update Hass.io CLI to 2.2.0

## 5.3

- Fix: User root not allowed because account is locked

## 5.2

- Update Hass.io CLI to 2.1.0

## 5.1

- Map all serial devices into container for manual adjustments

## 5.0

- Update Hass.io CLI to 2.0.1, include bash completion

## 4.0

- Update Hass.io CLI to 1.4.0
- Add new API role profile
- Update OpenSSH to 7.7

## 3.7

- Add YAML highlighting for nano

## 3.6

- Update Hass.io CLI to 1.3.1

## 3.5

- Update Hass.io CLI to 1.3.0

## 3.4

- Update Hass.io CLI to 1.2.1

## 3.3

- Update Hass.io CLI to 1.1.2

## 3.2

- Downgrade Hass.io CLI to 1.0.1

## 3.1

- Update Hass.io CLI to 1.1.1
- Change internal token handling for Hass.io API

## 3.0

- Use new base images
- Add hassio-cli version 1.0
- Use bash as default shell
