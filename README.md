# HACS Update Action Tracker

UPDATE: This functionality has been incorporated into the existing [Custom Component Monitor integration](https://github.com/loryanstrant/HA-CustomComponentMonitor).


## Overview

A replacement for the regular HACS update entities card in Home Assistant. Instead of just showing updates and letting you install them, **Update Action Tracker** gives you three clear choices for each pending HACS update:

- **Skip** – Dismiss the update (marks it as skipped in HA)
- **Update** – Install the update normally
- **Update & Action** – Install the update *and* create a to-do item with the release notes so you can review what changed and take any follow-up action

This is particularly useful when HACS updates include breaking changes, new features that need configuration, or deprecations that require attention.

## Screenshots
**List of components to update**
<img width="494" height="764" alt="image" src="https://github.com/user-attachments/assets/454e5eaa-478c-4245-8f9a-3fb6ba6a3c1d" />

**Item added to to-do list**
<img width="861" height="327" alt="image" src="https://github.com/user-attachments/assets/144a539f-07b5-4ac1-86d9-5e516d54cdc7" />

**To-do item details**
<img width="564" height="468" alt="image" src="https://github.com/user-attachments/assets/89634899-2daf-4744-bfd4-719d4e761613" />



## Features

📋 **Smart Update Card**
- Lists all pending HACS integration updates in a clean Lovelace card
- Shows entity icon, current version, and available version
- Expandable release notes for each update (fetched directly from the integration)
- Link to the GitHub release page for each update

🔄 **Real-time Progress Tracking**
- Shows installation progress bar during updates (determinate with percentage when available, animated pulse when indeterminate)
- Buttons are disabled during active installations to prevent conflicts
- Automatic polling during updates for responsive UI feedback

✅ **Todo List Integration**
- "Update & Action" creates a to-do item in Home Assistant's native todo list
- Each item includes:
  - Update date
  - Release URL link
  - Entity reference
  - Full release notes
- Track which updates need follow-up action and mark them as done when reviewed

🎨 **Polished UI**
- Visual editor for card title
- Badge showing count of pending updates (or "Up to date" when clear)
- Themed to match your Home Assistant UI
- Markdown rendering for release notes (headings, lists, links, code blocks, alerts)

## Installation

### HACS (Recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=loryanstrant&repository=HACS-Update-Action-Tracker&category=integration)

1. Open HACS in your Home Assistant instance
2. Click the three dots in the top right corner and select **Custom repositories**
3. Add this repository URL: `https://github.com/loryanstrant/HACS-Update-Action-Tracker`
4. Select **Integration** as the category
5. Click **Add**
6. Search for "Update Action Tracker" in HACS and install it
7. Restart Home Assistant

### Manual Installation

1. Download the latest release from the [Releases page](https://github.com/loryanstrant/HACS-Update-Action-Tracker/releases)
2. Copy the `custom_components/update_action_tracker` folder to your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

## Configuration

### Setting Up the Integration

1. Go to **Settings** > **Devices & Services**
2. Click **+ Add Integration**
3. Search for **Update Action Tracker**
4. Click to add it (no configuration options required)

The integration will automatically:
- Create a todo list entity: `todo.hacs_update_actions`
- Register the custom Lovelace card
- Register the `update_action_tracker.update_and_action` service

### Adding the Card to Your Dashboard

**IMPORTANT:** Before adding the card, make sure you restart HA *after* you've configured the integration. Once HA has restarted, perform a force refresh (Ctrl+F5) on your browser.
1. Edit your dashboard
2. Click **+ Add Card**
3. Search for **HACS Update Action Tracker**
4. Optionally customise the card title
5. Save

Alternatively, add it manually via YAML:

```yaml
type: custom:update-action-tracker-card
title: HACS Update Tracker
```

## Service

### `update_action_tracker.update_and_action`

Installs a HACS update and creates a to-do item to track follow-up actions.

| Parameter | Required | Description |
|-----------|----------|-------------|
| `entity_id` | Yes | The update entity to install (e.g., `update.my_integration_update`) |
| `version` | No | Specific version to install. If omitted, installs the latest version |

The to-do item created includes:
- **Summary**: `{Integration name} updated to {version} ({date})`
- **Description**: Update date, release URL, entity reference, and full release notes

## Todo Entity

The integration creates a persistent todo list entity (`todo.hacs_update_actions`) that supports:
- Creating items (via the service or manually)
- Updating item status (mark as completed when you've reviewed the changes)
- Deleting items
- Viewing descriptions with release notes

Items persist across Home Assistant restarts using local storage.

## Development Approach

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-GitHub%20Copilot-blue?logo=github" alt="Built with GitHub Copilot">
</p>

This integration was developed with the assistance of GitHub Copilot, guided by human expertise in Home Assistant integration design and HACS ecosystem best practices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have feature requests, please [open an issue](https://github.com/loryanstrant/HACS-Update-Action-Tracker/issues).
