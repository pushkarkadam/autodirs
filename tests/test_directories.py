import sys
import os
import pytest
import glob
sys.path.append('../')

from autodirs import directories as di

def test_create_directories():
    di.create_directories("tests/test_files.txt", "tests/test_dir/test_create_directories")

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_create_directories/") if dir.is_dir()]
    test_file_path = [
    "tests/test_dir/test_create_directories/GILDEROY LOCKHART",
    "tests/test_dir/test_create_directories/LUNA LOVEGOOD",
    "tests/test_dir/test_create_directories/ROWENA RAVENCLAW",
    "tests/test_dir/test_create_directories/THE GREY LADY"
    ]
    assert(file_path == test_file_path)
