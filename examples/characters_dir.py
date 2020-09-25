import sys
sys.path.append('../')

from autodirs import directories as di


di.create_directories_from_text("text_files/gryffindor.txt", "sub/house", with_text=True)
