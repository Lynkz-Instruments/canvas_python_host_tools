# Canvas Software Suite Tools

This repo hosts various software tools that can be used with devices running Canvas Software Suite firmware.

## Prerequisites

- Install Python 3.9 to 3.11. Python 3.12 is not supported.
- A board running Canvas Software Suite firmware.
  - Sera NX040
  - Lyra 24 series
  - MG100
  - BL5340 DVK
  - Pinnacle 100 DVK
  - BL654 DVK
  - BL654 USB Dongle
  - BT510
  - BT610

## Setup

### Checkout the Firmware

```
git clone --recurse-submodules https://github.com/LairdCP/canvas_software_suite_tools.git
```

### Install Python Dependencies

Before running any tools, be sure to install the Python dependencies:

```
pip3 install -r requirements.txt
```
