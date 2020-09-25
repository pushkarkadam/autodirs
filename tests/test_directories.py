import sys
import os
import pytest
import glob
sys.path.append('../')

from autodirs import directories as di

def test_create_directories_from_text():
    di.create_directories_from_text("tests/test_files.txt", "tests/test_dir/test_create_directories", with_text=True)

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_create_directories/") if dir.is_dir()]
    test_file_path = [
    "tests/test_dir/test_create_directories/GILDEROY LOCKHART",
    "tests/test_dir/test_create_directories/LUNA LOVEGOOD",
    "tests/test_dir/test_create_directories/ROWENA RAVENCLAW",
    "tests/test_dir/test_create_directories/THE GREY LADY"
    ]
    assert(file_path == test_file_path)


def test_group_by_text_files():
    di.group_by_text_files("tests", "tests/test_dir/test_group_by_text_files", with_text=True)

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_group_by_text_files/test_files/") if dir.is_dir()]

    test_file_path = [
    "tests/test_dir/test_group_by_text_files/test_files/GILDEROY LOCKHART",
    "tests/test_dir/test_group_by_text_files/test_files/LUNA LOVEGOOD",
    "tests/test_dir/test_group_by_text_files/test_files/ROWENA RAVENCLAW",
    "tests/test_dir/test_group_by_text_files/test_files/THE GREY LADY"
    ]
    assert(file_path == test_file_path)

def test_create_directories_from_list():
    ravenclaw = [
    "ROWENA RAVENCLAW",
    "LUNA LOVEGOOD",
    "GILDEROY LOCKHART",
    "THE GREY LADY"
    ]

    di.create_directories_from_list(ravenclaw, "tests/test_dir/test_create_directories_from_list", with_text=True)

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_create_directories_from_list/") if dir.is_dir()]

    test_file_path = [
    "tests/test_dir/test_create_directories_from_list/GILDEROY LOCKHART",
    "tests/test_dir/test_create_directories_from_list/LUNA LOVEGOOD",
    "tests/test_dir/test_create_directories_from_list/ROWENA RAVENCLAW",
    "tests/test_dir/test_create_directories_from_list/THE GREY LADY"
    ]

    assert(file_path == test_file_path)
