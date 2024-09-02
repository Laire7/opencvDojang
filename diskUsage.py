import shutil
import os

diskLabel = 'c:/Users/SBA/openCVDojang'
# total, used, free = shutil.disk_usage(diskLabel)

# print(total)
# print(used)
# print(free)

print(os.path.getsize(diskLabel))