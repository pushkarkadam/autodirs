import sys
sys.path.append('../')

from source.directories import Directories as Di

dir = Di("sub/houses")

dir.create_directories("text_files/gryffindor.txt")

print(dir.sub_dir_list)
