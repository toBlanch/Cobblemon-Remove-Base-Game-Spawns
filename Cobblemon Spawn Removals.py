# import OS module
import os
# Get the list of all files and directories
path = "C:\\Users\prior\Downloads\CobblemonOriginalSpawnFiles"
dir_list = os.listdir(path)
for item in dir_list:
    file = open("SpawnFiles\\"+item,"w")
    file.write("{\n  \"enabled\": true,\n  \"neededInstalledMods\": [],\n  \"neededUninstalledMods\": [],\n  \"spawns\": []\n}")
    file.close()