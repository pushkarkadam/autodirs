import sys
sys.path.append('../')

from source.directories import Directories as Di

dir = Di("sub/houses")

dir.group_by_text_files("text_files")
