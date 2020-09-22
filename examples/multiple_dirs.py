import sys
sys.path.append('../')

from autodirs import directories as di

di.group_by_text_files("text_files", path="sub/hogwarts")
