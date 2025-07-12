# GTAVFilechecker

Checks GTA V files for the right size!

## Description

**GTAVFilechecker** is a Python tool designed to verify the integrity of your Grand Theft Auto V installation by checking the sizes of key game files and downloadable content packs (DLCs). 

> **Note:** This project is not affiliated with, endorsed by, or in any way officially connected to Rockstar Games, its subsidiaries, or affiliates. All trademarks, logos, and brand names are the property of their respective owners. This project is an independent, unofficial work and is not sponsored, approved, or authorized by Rockstar Games.

## Features

- Checks core GTA V files and DLC packs for correct file sizes
- Supports automatic detection and input of GTA installation path
- Notifies users if files are missing, corrupted, or mismatched
- Fetches remote messages and the latest GTA version info from GitHub
- Configurable via a config file in your `APPDATA` folder

## Usage

1. **Install Requirements:**  
   Make sure you have Python 3 and the `requests` library installed.
   ```
   pip install requests
   ```

2. **Run the Script:**  
   Execute `main.py`:
   ```
   python main.py
   ```
   - On first run, you’ll be prompted to enter your GTA V installation path.
   - The tool will read the version file and compare it to the expected version.
   - It checks the presence and size of key `.rpf` files in the base and update folders.
   - At the end, it displays any files that are missing or mismatched.

## Example Output

```
[SUCCESS] x64a.rpf size is correct: 47566 KB
[WARNING] x64b.rpf size mismatch! Found: 140000 KB, Expected: 145946 KB
[ERROR] x64c.rpf not found in the GTA 5 directory.
========== Faulty Files ==========
- x64b.rpf (Found: 140000 KB, Expected: 145946 KB)
- x64c.rpf (Not found)
==================================
```

## Configuration

A config file (`config.json`) will be created in `APPDATA/gta5filechecker/`.  
You can update your GTA path by deleting this file and restarting the script.

