import sys
sys.path.append('../')

from autodirs import directories as di

di.create_nested_dirs_from_text(text="nested_example.txt", root_path="nested")
