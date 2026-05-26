"""Constants for the Update Action Tracker integration."""

from __future__ import annotations

from pathlib import Path

from homeassistant.const import Platform

DOMAIN = "update_action_tracker"
VERSION = "1.0.1"

PLATFORMS: list[Platform] = [Platform.TODO]

STORAGE_KEY = f"{DOMAIN}.items"
STORAGE_VERSION = 1

# Lovelace card
CARD_JS = "update-action-tracker-card.js"
CARD_URL = f"/{DOMAIN}/{CARD_JS}"
CARD_URL_VERSIONED = f"{CARD_URL}?v={VERSION}"
CARD_PATH = Path(__file__).parent / "www" / CARD_JS

# Service
SERVICE_UPDATE_AND_ACTION = "update_and_action"
