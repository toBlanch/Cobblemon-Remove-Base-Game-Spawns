import os
from pathlib import Path

output_dir = Path('SpawnFiles')
output_dir.mkdir(parents=True, exist_ok=True)

path = ""
if path == "":
    path = input("Input the directory containing the original spawn files: ")

dir_list = os.listdir(path)
for item in dir_list:
    file_path = output_dir / item
    with file_path.open('w') as file:
        file.write(
            "{\n  \"enabled\": true,\n  \"neededInstalledMods\": [],\n  \"neededUninstalledMods\": [],\n  \"spawns\": []\n}"
        )