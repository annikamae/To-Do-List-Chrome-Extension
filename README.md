# To-Do List Chrome Extension

A lightweight Chrome extension for keeping a to-do list and notes in the browser. The popup uses HTML, CSS, and JavaScript.

## Features

- Add tasks to the list.
- Click a task to mark it complete; completed tasks are removed shortly afterward.
- Add notes, which are saved automatically.
- Keep tasks and notes in browser `localStorage` for the same browser profile.

## Project files

- `manifest.json` - Chrome Extension Manifest V3 metadata and popup configuration.
- `popup.html` - the extension popup, including its styles and interface.
- `popup.js` - task interactions and local storage.
- `app.py` - an earlier PyScript experiment; it is not loaded by the current popup.
- `To-Do-List-Chrome-Extension.code-workspace` - Visual Studio Code workspace settings.
- `LICENSE` - GNU General Public License, version 3.

## Requirements

- Google Chrome or another Chromium-based browser with Manifest V3 extension support.
- No build step or external runtime dependency is required.

## Install for development

1. Clone or download this repository.
2. Open `chrome://extensions` in Chrome.
3. Turn on **Developer mode**.
4. Choose **Load unpacked** and select the project folder.
5. Open the extension from the browser toolbar.

## License

This project is distributed under the GNU General Public License v3.0. See `LICENSE` for the full text.
