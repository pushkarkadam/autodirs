import sys
sys.path.append('../')

from directories import directories as di

di.group_by_text_files("text_files", path="sub/hogwarts")
