import os
import requests
import json
import pathlib
import sys
import getpass
import time
import threading
import platform

ProgramGtaVersion = "1.0.231.0"

print(r"  ______ _______ _______      _______ _     _ _______ _______ _     _ _______  ______")
print(r" |  ____    |    |_____|      |       |_____| |______ |       |____/  |______ |_____/ ")
print(r' |_____|    |    |     |      |_____  |     | |______ |_____  |    \_ |______ |    \_ ')
print("")
print("Gta 5 File checker made by @IDname")
print("Made for educational purposes only, use at your own risk.")
print("Made for Gta version "+ ProgramGtaVersion )
try:
    response = requests.get("https://raw.githubusercontent.com/IDname-git/GTAVFilechecker/refs/heads/main/requestsdata.json", timeout=10)
    if response.status_code == 200:
        remote_data = response.json()
        if remote_data.get("show_message") and remote_data.get("message"):
            print(f"[INFO] {remote_data['message']}")
        if remote_data.get("show_discord_invite") and remote_data.get("discord_invite"):
            print(f"[INFO] {remote_data['discord_invite']}")
        if remote_data.get("gta_version"):
            print(f"[INFO] Latest GTA 5 version: {remote_data['gta_version']}")
    else:
        print("[WARNING] Could not fetch remote data (status code:", response.status_code, ")")
except Exception as e:
    print("[WARNING] Failed to fetch remote data:", str(e))
config_dir = os.path.join(os.getenv('APPDATA'), 'gta5filechecker')
config_path = os.path.join(config_dir, 'config.json')
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
else:
    config = {}

if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
else:
    config = {}

if not config.get("gtapath"):
    config["gtapath"] = input("Please enter your GTA 5 installation path: ")
    with open(config_path, 'w') as f:
        json.dump(config, f)
gtapath = config["gtapath"]
if not os.path.exists(gtapath):
    print("[INFO] The specified GTA 5 path does not exist. Please check the path and try again.")
    if os.path.exists(config_path):
        os.remove(config_path)
        print("[INFO] Config file deleted. Please restart the script.")
    input("Press Any key to exit...")
    sys.exit(1)
version_file = os.path.join(gtapath, "version.txt")
if not os.path.exists(version_file):
    print("[ERROR] version.txt not found in the GTA 5 directory.")
    input("Press Any key to exit...")
    sys.exit(1)

with open(version_file, "r") as vf:
    gta_version = vf.read().strip()

if gta_version == ProgramGtaVersion:
    print("[SUCCESS] GTA 5 version matches the expected version:", ProgramGtaVersion)
else:
    print(f"[WARNING] GTA 5 version mismatch! Found: {gta_version}, Expected: {ProgramGtaVersion}")
    if gta_version > ProgramGtaVersion:
        print("[INFO] You have a newer GTA 5 version. Please check the Github page for an Update.")
    else:
        print("[INFO] Your GTA 5 version is older and not supported by this script.")

if not config.get("display_mode"):
    print("Choose display mode for file checking:")
    print("1. Progress bar")
    print("2. Full displayed list")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        config["display_mode"] = "progress"
    else:
        config["display_mode"] = "list"
    with open(config_path, 'w') as f:
        json.dump(config, f)

display_mode = config["display_mode"]
settings = config 

if not settings.get("display_mode"):
    print("Choose display mode for file checking:")
    print("1. Progress bar")
    print("2. Full displayed list")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        settings["display_mode"] = "progress"
    if choice == "2":
        settings["display_mode"] = "list"
    else:
        print("Invalid choice, defaulting to progress bar.")
        settings["display_mode"] = "progress"    
    with open(config_path, 'w') as sf:
        json.dump(settings, sf)

display_mode = settings["display_mode"]

def print_progress_bar(iteration, total, prefix='', suffix='', length=50):
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

files_to_check = [
    {"filename": "common.rpf", "expected_size_kb": 27056},
    {"filename": "x64a.rpf", "expected_size_kb": 47566},
    {"filename": "x64b.rpf", "expected_size_kb": 145946}, 
    {"filename": "x64c.rpf", "expected_size_kb": 2144734},
    {"filename": "x64d.rpf", "expected_size_kb": 1762372},
    {"filename": "x64e.rpf", "expected_size_kb": 2066362},
    {"filename": "x64f.rpf", "expected_size_kb": 1004646},
    {"filename": "x64g.rpf", "expected_size_kb": 2492770},
    {"filename": "x64h.rpf", "expected_size_kb": 1659730},
    {"filename": "x64i.rpf", "expected_size_kb": 1745160},
    {"filename": "x64j.rpf", "expected_size_kb": 2060078},
    {"filename": "x64k.rpf", "expected_size_kb": 2310204},
    {"filename": "x64l.rpf", "expected_size_kb": 2517160},
    {"filename": "x64m.rpf", "expected_size_kb": 1764892},
    {"filename": "x64n.rpf", "expected_size_kb": 1600080},
    {"filename": "x64o.rpf", "expected_size_kb": 1717134},
    {"filename": "x64p.rpf", "expected_size_kb": 1395124},
    {"filename": "x64q.rpf", "expected_size_kb": 2757436},
    {"filename": "x64r.rpf", "expected_size_kb": 1671152},
    {"filename": "x64s.rpf", "expected_size_kb": 1607682},
    {"filename": "x64t.rpf", "expected_size_kb": 1879522},
    {"filename": "x64u.rpf", "expected_size_kb": 1322662},
    {"filename": "x64v.rpf", "expected_size_kb": 1896530},
    {"filename": "x64w.rpf", "expected_size_kb": 915372},
]

update_files_to_check = [
    {"filename": "update.rpf", "expected_size_kb": 1418782},
    {"filename": "update2.rpf", "expected_size_kb": 446690},  
    {"filename": os.path.join("x64", "dlcpacks", "mpheist", "dlc.rpf"), "expected_size_kb": 2981214},
    {"filename": os.path.join("x64", "dlcpacks", "mp2023_01", "dlc.rpf"), "expected_size_kb": 790454},
    {"filename": os.path.join("x64", "dlcpacks", "mp2023_01_g9ec", "dlc.rpf"), "expected_size_kb": 1430},
    {"filename": os.path.join("x64", "dlcpacks", "mp2023_02", "dlc.rpf"), "expected_size_kb": 1567130},
    {"filename": os.path.join("x64", "dlcpacks", "mp2023_02_g9ec", "dlc.rpf"), "expected_size_kb": 408},
    {"filename": os.path.join("x64", "dlcpacks", "mp2024_01", "dlc.rpf"), "expected_size_kb": 1151146},
    {"filename": os.path.join("x64", "dlcpacks", "mp2024_01_g9ec", "dlc.rpf"), "expected_size_kb": 22968},
    {"filename": os.path.join("x64", "dlcpacks", "mp2024_02", "dlc.rpf"), "expected_size_kb": 1156212},
    {"filename": os.path.join("x64", "dlcpacks", "mp2024_02_g9ec", "dlc.rpf"), "expected_size_kb": 54},
    {"filename": os.path.join("x64", "dlcpacks", "mp2025_01", "dlc.rpf"), "expected_size_kb": 1751276},
    {"filename": os.path.join("x64", "dlcpacks", "mp2025_01_G9EC", "dlc.rpf"), "expected_size_kb": 56},
    {"filename": os.path.join("x64", "dlcpacks", "mpairraces", "dlc.rpf"), "expected_size_kb": 80526},
    {"filename": os.path.join("x64", "dlcpacks", "mpapartment", "dlc.rpf"), "expected_size_kb": 622056},
    {"filename": os.path.join("x64", "dlcpacks", "mpassault", "dlc.rpf"), "expected_size_kb": 307074},
    {"filename": os.path.join("x64", "dlcpacks", "mpbattle", "dlc.rpf"), "expected_size_kb": 3887734},
    {"filename": os.path.join("x64", "dlcpacks", "mpbattle", "dlc1.rpf"), "expected_size_kb": 969040},
    {"filename": os.path.join("x64", "dlcpacks", "mpbiker", "dlc.rpf"), "expected_size_kb": 1752000},
    {"filename": os.path.join("x64", "dlcpacks", "mpchristmas2", "dlc.rpf"), "expected_size_kb": 62442},
    {"filename": os.path.join("x64", "dlcpacks", "mpchristmas2017", "dlc.rpf"), "expected_size_kb": 2349730},
    {"filename": os.path.join("x64", "dlcpacks", "mpchristmas2018", "dlc.rpf"), "expected_size_kb": 3171662},
    {"filename": os.path.join("x64", "dlcpacks", "mpchristmas3", "dlc.rpf"), "expected_size_kb": 1780148},
    {"filename": os.path.join("x64", "dlcpacks", "mpchristmas3_g9ec", "dlc.rpf"), "expected_size_kb": 118},
    {"filename": os.path.join("x64", "dlcpacks", "mpexecutive", "dlc.rpf"), "expected_size_kb": 782782},
    {"filename": os.path.join("x64", "dlcpacks", "mpg9ec", "dlc.rpf"), "expected_size_kb": 1804},
    {"filename": os.path.join("x64", "dlcpacks", "mpgunrunning", "dlc.rpf"), "expected_size_kb": 1835700},
    {"filename": os.path.join("x64", "dlcpacks", "mphalloween", "dlc.rpf"), "expected_size_kb": 102206},
    {"filename": os.path.join("x64", "dlcpacks", "mpheist", "dlc.rpf"), "expected_size_kb": 2981214},
    {"filename": os.path.join("x64", "dlcpacks", "mpheist3", "dlc.rpf"), "expected_size_kb": 2322110},
    {"filename": os.path.join("x64", "dlcpacks", "mpheist4", "dlc.rpf"), "expected_size_kb": 3371572},
    {"filename": os.path.join("x64", "dlcpacks", "mpheist4", "dlc1.rpf"), "expected_size_kb": 3388432},
    {"filename": os.path.join("x64", "dlcpacks", "mpheist4", "dlc2.rpf"), "expected_size_kb": 1320498},
    {"filename": os.path.join("x64", "dlcpacks", "mpimportexport", "dlc.rpf"), "expected_size_kb": 893858},
    {"filename": os.path.join("x64", "dlcpacks", "mpjanuary2016", "dlc.rpf"), "expected_size_kb": 145914},
    {"filename": os.path.join("x64", "dlcpacks", "mplowrider", "dlc.rpf"), "expected_size_kb": 1063294},
    {"filename": os.path.join("x64", "dlcpacks", "mplowrider2", "dlc.rpf"), "expected_size_kb": 326200},
    {"filename": os.path.join("x64", "dlcpacks", "mpluxe", "dlc.rpf"), "expected_size_kb": 220958},
    {"filename": os.path.join("x64", "dlcpacks", "mpluxe2", "dlc.rpf"), "expected_size_kb": 102642},
    {"filename": os.path.join("x64", "dlcpacks", "mppatchesng", "dlc.rpf"), "expected_size_kb": 427270},
    {"filename": os.path.join("x64", "dlcpacks", "mpreplay", "dlc.rpf"), "expected_size_kb": 419856},
    {"filename": os.path.join("x64", "dlcpacks", "mpsecurity", "dlc.rpf"), "expected_size_kb": 1932582},
    {"filename": os.path.join("x64", "dlcpacks", "mpsecurity", "dlc1.rpf"), "expected_size_kb": 1278198},
    {"filename": os.path.join("x64", "dlcpacks", "mpsmuggler", "dlc.rpf"), "expected_size_kb": 950850},
    {"filename": os.path.join("x64", "dlcpacks", "mpspecialraces", "dlc.rpf"), "expected_size_kb": 76610},
    {"filename": os.path.join("x64", "dlcpacks", "mpstunt", "dlc.rpf"), "expected_size_kb": 339890},
    {"filename": os.path.join("x64", "dlcpacks", "mpsum", "dlc.rpf"), "expected_size_kb": 957638},
    {"filename": os.path.join("x64", "dlcpacks", "mpsum2", "dlc.rpf"), "expected_size_kb": 1215984},
    {"filename": os.path.join("x64", "dlcpacks", "mpSum2_G9EC", "dlc.rpf"), "expected_size_kb": 244},
    {"filename": os.path.join("x64", "dlcpacks", "mptuner", "dlc.rpf"), "expected_size_kb": 3401240},
    {"filename": os.path.join("x64", "dlcpacks", "mptuner", "dlc1.rpf"), "expected_size_kb": 46422},
    {"filename": os.path.join("x64", "dlcpacks", "mpvalentines2", "dlc.rpf"), "expected_size_kb": 24486},
    {"filename": os.path.join("x64", "dlcpacks", "mpvinewood", "dlc.rpf"), "expected_size_kb": 1654804},
    {"filename": os.path.join("x64", "dlcpacks", "mpxmas_604490", "dlc.rpf"), "expected_size_kb": 44982},
    {"filename": os.path.join("x64", "dlcpacks", "patch2023_01", "dlc.rpf"), "expected_size_kb": 138218},
    {"filename": os.path.join("x64", "dlcpacks", "patch2023_01_g9ec", "dlc.rpf"), "expected_size_kb": 14},
    {"filename": os.path.join("x64", "dlcpacks", "patch2023_02", "dlc.rpf"), "expected_size_kb": 12046},
    {"filename": os.path.join("x64", "dlcpacks", "patch2024_01", "dlc.rpf"), "expected_size_kb": 345016},
    {"filename": os.path.join("x64", "dlcpacks", "patch2024_01_g9ec", "dlc.rpf"), "expected_size_kb": 40},
    {"filename": os.path.join("x64", "dlcpacks", "patch2024_02", "dlc.rpf"), "expected_size_kb": 233526},
    {"filename": os.path.join("x64", "dlcpacks", "patch2025_01", "dlc.rpf"), "expected_size_kb": 564616},
    {"filename": os.path.join("x64", "dlcpacks", "patchday10ng", "dlc.rpf"), "expected_size_kb": 91928},
    {"filename": os.path.join("x64", "dlcpacks", "patchday11ng", "dlc.rpf"), "expected_size_kb": 9722},
    {"filename": os.path.join("x64", "dlcpacks", "patchday12ng", "dlc.rpf"), "expected_size_kb": 151722},
    {"filename": os.path.join("x64", "dlcpacks", "patchday13ng", "dlc.rpf"), "expected_size_kb": 141360},
    {"filename": os.path.join("x64", "dlcpacks", "patchday14ng", "dlc.rpf"), "expected_size_kb": 90752},
    {"filename": os.path.join("x64", "dlcpacks", "patchday15ng", "dlc.rpf"), "expected_size_kb": 46366},
    {"filename": os.path.join("x64", "dlcpacks", "patchday16ng", "dlc.rpf"), "expected_size_kb": 11800},
    {"filename": os.path.join("x64", "dlcpacks", "patchday17ng", "dlc.rpf"), "expected_size_kb": 58570},
    { "filename": os.path.join("x64", "dlcpacks", "patchday18ng", "dlc.rpf"), "expected_size_kb": 4302},
    {"filename": os.path.join("x64", "dlcpacks", "patchday19ng", "dlc.rpf"), "expected_size_kb": 747686},
    {"filename": os.path.join("x64", "dlcpacks", "patchday1ng", "dlc.rpf"), "expected_size_kb": 456460},
    {"filename": os.path.join("x64", "dlcpacks", "patchday20ng", "dlc.rpf"), "expected_size_kb": 446416},
    {"filename": os.path.join("x64", "dlcpacks", "patchday21ng", "dlc.rpf"), "expected_size_kb": 1090692},
    {"filename": os.path.join("x64", "dlcpacks", "patchday22ng", "dlc.rpf"), "expected_size_kb": 677838},
    {"filename": os.path.join("x64", "dlcpacks", "patchday23ng", "dlc.rpf"), "expected_size_kb": 88570},
    {"filename": os.path.join("x64", "dlcpacks", "patchday24ng", "dlc.rpf"), "expected_size_kb": 375018},
    {"filename": os.path.join("x64", "dlcpacks", "patchday25ng", "dlc.rpf"), "expected_size_kb": 92732},
    {"filename": os.path.join("x64", "dlcpacks", "patchday26ng", "dlc.rpf"), "expected_size_kb": 516954},
    {"filename": os.path.join("x64", "dlcpacks", "patchday27g9ecng", "dlc.rpf"), "expected_size_kb": 256},
    {"filename": os.path.join("x64", "dlcpacks", "patchday27ng", "dlc.rpf"), "expected_size_kb": 322344},
    {"filename": os.path.join("x64", "dlcpacks", "patchday28g9ecng", "dlc.rpf"), "expected_size_kb": 6},
    {"filename": os.path.join("x64", "dlcpacks", "patchday28ng", "dlc.rpf"), "expected_size_kb": 172516},
    {"filename": os.path.join("x64", "dlcpacks", "patchday2bng", "dlc.rpf"), "expected_size_kb": 38622},
    {"filename": os.path.join("x64", "dlcpacks", "patchday2ng", "dlc.rpf"), "expected_size_kb": 786036},
    {"filename": os.path.join("x64", "dlcpacks", "patchday3ng", "dlc.rpf"), "expected_size_kb": 2200234},
    {"filename": os.path.join("x64", "dlcpacks", "patchday4ng", "dlc.rpf"), "expected_size_kb": 305116},
    {"filename": os.path.join("x64", "dlcpacks", "patchday5ng", "dlc.rpf"), "expected_size_kb": 7644},
    {"filename": os.path.join("x64", "dlcpacks", "patchday6ng", "dlc.rpf"), "expected_size_kb": 31160},
    {"filename": os.path.join("x64", "dlcpacks", "patchday7ng", "dlc.rpf"), "expected_size_kb": 42816},
    {"filename": os.path.join("x64", "dlcpacks", "patchday8ng", "dlc.rpf"), "expected_size_kb": 356766},
    {"filename": os.path.join("x64", "dlcpacks", "patchday9ng", "dlc.rpf"), "expected_size_kb": 156762},
    {"filename": os.path.join("x64", "dlcpacks", "patchdayg9ecng", "dlc.rpf"), "expected_size_kb": 16022},
    {"filename": os.path.join("x64", "dlcpacks", "vinewood", "dlc.rpf"), "expected_size_kb": 1654804},
]

faulty_files = []

def check_file(file_path, expected_size_kb, display_name):
    if os.path.exists(file_path):
        actual_size_kb = os.path.getsize(file_path) // 1024
        if actual_size_kb == expected_size_kb:
            if display_mode == "list":
                print(f"[SUCCESS] {display_name} size is correct: {actual_size_kb} KB")
        else:
            print(f"[WARNING] {display_name} size mismatch! Found: {actual_size_kb} KB, Expected: {expected_size_kb} KB")
            faulty_files.append(f"{display_name} (Found: {actual_size_kb} KB, Expected: {expected_size_kb} KB)")
    else:
        print(f"[ERROR] {display_name} not found in the GTA 5 directory.")
        faulty_files.append(f"{display_name} (Not found)")

total_files = len(files_to_check) + len(update_files_to_check)
current_file = 0

if display_mode == "progress":
    print_progress_bar(0, total_files, prefix='Checking files:', suffix='Complete', length=40)

for file_info in files_to_check:
    file_path = os.path.join(gtapath, file_info["filename"])
    expected_size_kb = file_info["expected_size_kb"]
    display_name = file_info["filename"]
    check_file(file_path, expected_size_kb, display_name)
    current_file += 1
    if display_mode == "progress":
        print_progress_bar(current_file, total_files, prefix='Checking files:', suffix='Complete', length=40)
    time.sleep(0.02)

for file_info in update_files_to_check:
    file_path = os.path.join(gtapath, "update", file_info["filename"])
    expected_size_kb = file_info["expected_size_kb"]
    display_name = f"update/{file_info['filename']}"
    check_file(file_path, expected_size_kb, display_name)
    current_file += 1
    if display_mode == "progress":
        print_progress_bar(current_file, total_files, prefix='Checking files:', suffix='Complete', length=40)
    time.sleep(0.02)

if faulty_files:
    print("\n========== Faulty Files ==========")
    for f in faulty_files:
        print(f"- {f}")
    print("==================================")
else:
    print("\nAll checked files are correct!")


statistics_path = os.path.join(config_dir, 'statistics.json')
if os.path.exists(statistics_path):
    with open(statistics_path, 'r') as sf:
        statistics = json.load(sf)
else:
    statistics = {
        "uses": 0,
        "last_used": "",
        "faulty_files_count": 0,
        "last_gta_version": "",
        "total_faulty_files": 0,
        "system_info": ""
    }
statistics["uses"] += 1
statistics["last_used"] = time.strftime("%Y-%m-%d %H:%M:%S")
statistics["last_gta_version"] = ProgramGtaVersion
statistics["system_info"] = platform.platform()

def save_statistics():
    statistics["faulty_files_count"] = len(faulty_files)
    statistics["total_faulty_files"] += len(faulty_files)
    with open(statistics_path, 'w') as sf:
        json.dump(statistics, sf, indent=2)
save_statistics()
affiliation_file_path = os.path.join(config_dir, 'readme.txt')
if not os.path.exists(affiliation_file_path):
    affiliation_text = (
        "All files created by this tool in this directory can be safely deleted at any time.\n"
        ""
        "This project is not affiliated with, endorsed by, or in any way officially connected to Rockstar Games, its subsidiaries, or affiliates.\n"
        "All trademarks, logos, and brand names are the property of their respective owners.\n"
        "This project is an independent, unofficial work and is not sponsored, approved, or authorized by Rockstar Games.\n"
        "made by @IDname\n" \
        "Updates and support: https://github.com/IDname-git/GTAVFilechecker \n"
        
    )
    with open(affiliation_file_path, 'w') as af:
        af.write(affiliation_text)
print("This project is not affiliated with, endorsed by, or in any way officially connected to Rockstar Games, its")
print("subsidiaries, or affiliates. All trademarks, logos, and brand names are the property of their respective owners.")
print("This project is an independent, unofficial work and is not sponsored, approved, or authorized by Rockstar Games.")

input("Press Any key to exit...")
sys.exit(0)
