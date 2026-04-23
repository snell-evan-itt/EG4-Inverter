[![GitHub Release](https://img.shields.io/github/release/snell-evan-itt/EG4-Inverter.svg?style=for-the-badge&color=blue)](https://github.com/snell-evan-itt/EG4-Inverter/releases)
[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/snell-evan-itt/EG4-Inverter/total?style=for-the-badge)](https://github.com/snell-evan-itt/EG4-Inverter/releases/latest)
[![HACS Default](https://img.shields.io/badge/HACS-default-blue.svg?style=for-the-badge)](https://hacs.xyz) [![Community forum discussion](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=for-the-badge&color=yellow)](https://community.home-assistant.io/t/custom-component-ecoflow-cloud-api-for-us-users/799962)

# Home Assistant EG4 Inverter Integration

![EG4 Monitor Banner](docs/images/eg4_banner.png)

This is a custom Home Assistant integration for monitoring EG4 inverter systems. It connects to the EG4 web portal to fetch real-time data about your solar system.

## Installation

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?category=integration&repository=EG4-Inverter&owner=snell-evan-itt)

- Click above to install as a custom repository via HACS
- Restart Home Assistant
- Once restart is done, use Add Integration -> EG4 Inverter.

## Features

- Retrieves status and production metrics from an EG4 Inverter.
- Allows you to expose the inverter’s data to Home Assistant sensors.
- Easy setup and configuration via UI.

<p align="center">
  <a href="docs/images/01.png" target="_blank">
    <img src="docs/images/01.png" alt="EG4 Inverter Integration Selection" height="300"/>
  </a>
  <a href="docs/images/02.png" target="_blank">
    <img src="docs/images/02.png" alt="EG4 Configuration" height="300"/>
  </a>
  <a href="docs/images/03.png" target="_blank">
    <img src="docs/images/03.png" alt="EG4 Added" height="300"/>
  </a>
  <a href="docs/images/04.png" target="_blank">
    <img src="docs/images/04.png" alt="EG4 Entities" height="300"/>
  </a>
  <a href="docs/images/05.png" target="_blank">
    <img src="docs/images/05.png" alt="EG4 Energy Dashboard" height="300"/>
  </a>
</p>

## Multiple Inverters Support

This integration supports adding multiple EG4 Inverter devices to Home Assistant (e.g., “EG4 Inverter”, “EG4 Inverter 2”, “EG4 Inverter 3”, …)

Behavior:
- Each setup creates its own config entry and device in Home Assistant.
- The integration auto-assigns an index for each new entry:
  - The first (existing or first created) entry is index 1 and displays as “EG4 Inverter”.
  - Subsequent entries display as “EG4 Inverter {index}”.
- Entities keep their unique IDs based on the config entry ID, preserving history for existing users.
- Entity friendly names remain unchanged; use the device name to distinguish between inverters in the UI.

How to add multiple inverters:
1. Go to Settings → Devices & Services → Add Integration → “EG4 Inverter”.
2. Enter credentials and (optionally) serial number and other options as before.
3. Repeat the process to add a second or third inverter. The integration will automatically name them “EG4 Inverter 2”, “EG4 Inverter 3”, etc.

Migration for existing users:
- Existing installations are automatically migrated. The first entry is assigned index 1; device and entities remain intact.
- No manual steps are required.

Troubleshooting:
- If adding an additional inverter fails due to a duplicate error, update to the latest version and restart Home Assistant.
- Check Home Assistant logs for “EG4 Inverter” messages for details.

## Configuration

The integration requires your EG4 portal credentials:
- Username
- Password


## Contributors

- [Trixanna](https://github.com/Trixanna)
- []()