# GTA 5 File Checker

## Disclaimer
This project is not affiliated with, endorsed by, or in any way officially connected to Rockstar Games, its subsidiaries, or affiliates.
All trademarks, logos, and brand names are the property of their respective owners.
This project is an independent, unofficial work and is not sponsored, approved, or authorized by Rockstar Games.

## Description

This script checks whether the installed GTA 5 matches the expected version and verifies key game files for correct sizes. It supports two display modes: progress bar or detailed list.

---

## Usage

1. Run the script.  
2. Enter the GTA 5 installation path if not already saved.  
3. Choose the display mode (progress bar or list).  
4. The script verifies the version and files, then outputs the results.

---

## Important Notes

- The `version.txt` file in the game directory is compared to the script’s version (1.0.231.0).  
- If `version.txt` is missing or the path is incorrect, the script will exit with an error.  
- File sizes are checked in kilobytes to ensure integrity.  
- Official file updates or changes may cause false positives.  
- This tool is **for educational purposes only** and is provided without any warranty. Use at your own risk.

---

## Installation and Configuration

- The script saves the GTA path and display mode in `config.json` located at `%APPDATA%\gta5filechecker\`.  
- Delete the config file to reset the path and display mode input if needed.

---

## Example output

```
[SUCCESS] update/x64\dlcpacks\mplowrider\dlc.rpf size is correct: 1063294 KB
[SUCCESS] update/x64\dlcpacks\mplowrider2\dlc.rpf size is correct: 326200 KB
[SUCCESS] update/x64\dlcpacks\mpluxe\dlc.rpf size is correct: 220958 KB
[SUCCESS] update/x64\dlcpacks\mpluxe2\dlc.rpf size is correct: 102642 KB
[SUCCESS] update/x64\dlcpacks\mppatchesng\dlc.rpf size is correct: 427270 KB
[SUCCESS] update/x64\dlcpacks\mpreplay\dlc.rpf size is correct: 419856 KB
[SUCCESS] update/x64\dlcpacks\mpsecurity\dlc.rpf size is correct: 1932582 KB
[SUCCESS] update/x64\dlcpacks\mpsecurity\dlc1.rpf size is correct: 1278198 KB
[SUCCESS] update/x64\dlcpacks\mpsmuggler\dlc.rpf size is correct: 950850 KB
[SUCCESS] update/x64\dlcpacks\mpspecialraces\dlc.rpf size is correct: 76610 KB
[SUCCESS] update/x64\dlcpacks\mpstunt\dlc.rpf size is correct: 339890 KB
[SUCCESS] update/x64\dlcpacks\mpsum\dlc.rpf size is correct: 957638 KB
[SUCCESS] update/x64\dlcpacks\mpsum2\dlc.rpf size is correct: 1215984 KB
[SUCCESS] update/x64\dlcpacks\mpSum2_G9EC\dlc.rpf size is correct: 244 KB
[SUCCESS] update/x64\dlcpacks\mptuner\dlc.rpf size is correct: 3401240 KB
[SUCCESS] update/x64\dlcpacks\mptuner\dlc1.rpf size is correct: 46422 KB
[SUCCESS] update/x64\dlcpacks\mpvalentines2\dlc.rpf size is correct: 24486 KB
[SUCCESS] update/x64\dlcpacks\mpvinewood\dlc.rpf size is correct: 1654804 KB
[SUCCESS] update/x64\dlcpacks\mpxmas_604490\dlc.rpf size is correct: 44982 KB
[SUCCESS] update/x64\dlcpacks\patch2023_01\dlc.rpf size is correct: 138218 KB
[SUCCESS] update/x64\dlcpacks\patch2023_01_g9ec\dlc.rpf size is correct: 14 KB
[SUCCESS] update/x64\dlcpacks\patch2023_02\dlc.rpf size is correct: 12046 KB
[SUCCESS] update/x64\dlcpacks\patch2024_01\dlc.rpf size is correct: 345016 KB
[SUCCESS] update/x64\dlcpacks\patch2024_01_g9ec\dlc.rpf size is correct: 40 KB
[SUCCESS] update/x64\dlcpacks\patch2024_02\dlc.rpf size is correct: 233526 KB
[SUCCESS] update/x64\dlcpacks\patch2025_01\dlc.rpf size is correct: 564616 KB
[SUCCESS] update/x64\dlcpacks\patchday10ng\dlc.rpf size is correct: 91928 KB
[SUCCESS] update/x64\dlcpacks\patchday11ng\dlc.rpf size is correct: 9722 KB
[SUCCESS] update/x64\dlcpacks\patchday12ng\dlc.rpf size is correct: 151722 KB
[SUCCESS] update/x64\dlcpacks\patchday13ng\dlc.rpf size is correct: 141360 KB
[SUCCESS] update/x64\dlcpacks\patchday14ng\dlc.rpf size is correct: 90752 KB
[SUCCESS] update/x64\dlcpacks\patchday15ng\dlc.rpf size is correct: 46366 KB
[SUCCESS] update/x64\dlcpacks\patchday16ng\dlc.rpf size is correct: 11800 KB
[SUCCESS] update/x64\dlcpacks\patchday17ng\dlc.rpf size is correct: 58570 KB
[SUCCESS] update/x64\dlcpacks\patchday18ng\dlc.rpf size is correct: 4302 KB
[SUCCESS] update/x64\dlcpacks\patchday19ng\dlc.rpf size is correct: 747686 KB
[SUCCESS] update/x64\dlcpacks\patchday1ng\dlc.rpf size is correct: 456460 KB
[SUCCESS] update/x64\dlcpacks\patchday20ng\dlc.rpf size is correct: 446416 KB
[SUCCESS] update/x64\dlcpacks\patchday21ng\dlc.rpf size is correct: 1090692 KB
[SUCCESS] update/x64\dlcpacks\patchday22ng\dlc.rpf size is correct: 677838 KB
[SUCCESS] update/x64\dlcpacks\patchday23ng\dlc.rpf size is correct: 88570 KB
[SUCCESS] update/x64\dlcpacks\patchday24ng\dlc.rpf size is correct: 375018 KB
[SUCCESS] update/x64\dlcpacks\patchday25ng\dlc.rpf size is correct: 92732 KB
[SUCCESS] update/x64\dlcpacks\patchday26ng\dlc.rpf size is correct: 516954 KB
[SUCCESS] update/x64\dlcpacks\patchday27g9ecng\dlc.rpf size is correct: 256 KB
[SUCCESS] update/x64\dlcpacks\patchday27ng\dlc.rpf size is correct: 322344 KB
[SUCCESS] update/x64\dlcpacks\patchday28g9ecng\dlc.rpf size is correct: 6 KB
[SUCCESS] update/x64\dlcpacks\patchday28ng\dlc.rpf size is correct: 172516 KB
[SUCCESS] update/x64\dlcpacks\patchday2bng\dlc.rpf size is correct: 38622 KB
[SUCCESS] update/x64\dlcpacks\patchday2ng\dlc.rpf size is correct: 786036 KB
[SUCCESS] update/x64\dlcpacks\patchday3ng\dlc.rpf size is correct: 2200234 KB
[SUCCESS] update/x64\dlcpacks\patchday4ng\dlc.rpf size is correct: 305116 KB
[SUCCESS] update/x64\dlcpacks\patchday5ng\dlc.rpf size is correct: 7644 KB
[SUCCESS] update/x64\dlcpacks\patchday6ng\dlc.rpf size is correct: 31160 KB
[SUCCESS] update/x64\dlcpacks\patchday7ng\dlc.rpf size is correct: 42816 KB
[SUCCESS] update/x64\dlcpacks\patchday8ng\dlc.rpf size is correct: 356766 KB
[SUCCESS] update/x64\dlcpacks\patchday9ng\dlc.rpf size is correct: 156762 KB
[SUCCESS] update/x64\dlcpacks\patchdayg9ecng\dlc.rpf size is correct: 16022 KB
[SUCCESS] update/x64\dlcpacks\vinewood\dlc.rpf size is correct: 1654804 KB


````
---

## Support & Updates

- The script fetches the latest info and updates from GitHub on startup.  
- Updated versions are available on the GitHub repository.

---

## License

For private and educational use only. No liability for damages or data loss.
