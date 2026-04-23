import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.core import HomeAssistant
from .const import DOMAIN, PLATFORMS, CONF_ENTRY_INDEX
from .coordinator import EG4DataCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up EG4 Inverter via configuration.yaml (if required in future)."""
    _LOGGER.info("EG4 Inverter integration async_setup() called")
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate old config entries to include entry index without breaking entities."""
    data = dict(entry.data)
    if CONF_ENTRY_INDEX not in data:
        # Backfill the first (legacy) entry as index=1
        data[CONF_ENTRY_INDEX] = 1
        hass.config_entries.async_update_entry(entry, data=data)
        _LOGGER.info("EG4 Inverter: Migrated entry %s to include entry_index=1", entry.entry_id)
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    coordinator = EG4DataCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
