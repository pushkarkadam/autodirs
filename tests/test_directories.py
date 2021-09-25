import sys
import os
import pytest
import glob
sys.path.append('../')

import autodirs

def test_create_directories_from_text():
    autodirs.create_directories_from_text("tests/test_files.txt", "tests/test_dir/test_create_directories", with_text=True)

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_create_directories/") if dir.is_dir()]
    test_file_path = [
    "tests/test_dir/test_create_directories/GILDEROY LOCKHART",
    "tests/test_dir/test_create_directories/LUNA LOVEGOOD",
    "tests/test_dir/test_create_directories/ROWENA RAVENCLAW",
    "tests/test_dir/test_create_directories/THE GREY LADY"
    ]
    assert(set(file_path) == set(test_file_path))


def test_group_by_text_files():
    autodirs.group_by_text_files("tests", "tests/test_dir/test_group_by_text_files", with_text=True)

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_group_by_text_files/test_files/") if dir.is_dir()]

    test_file_path = [
    "tests/test_dir/test_group_by_text_files/test_files/GILDEROY LOCKHART",
    "tests/test_dir/test_group_by_text_files/test_files/LUNA LOVEGOOD",
    "tests/test_dir/test_group_by_text_files/test_files/ROWENA RAVENCLAW",
    "tests/test_dir/test_group_by_text_files/test_files/THE GREY LADY"
    ]
    assert(set(file_path) == set(test_file_path))

def test_create_directories_from_list():
    ravenclaw = [
    "ROWENA RAVENCLAW",
    "LUNA LOVEGOOD",
    "GILDEROY LOCKHART",
    "THE GREY LADY"
    ]

    autodirs.create_directories_from_list(ravenclaw, "tests/test_dir/test_create_directories_from_list", with_text=True)

    file_path = [dir.path for dir in os.scandir("tests/test_dir/test_create_directories_from_list/") if dir.is_dir()]

    test_file_path = [
    "tests/test_dir/test_create_directories_from_list/GILDEROY LOCKHART",
    "tests/test_dir/test_create_directories_from_list/LUNA LOVEGOOD",
    "tests/test_dir/test_create_directories_from_list/ROWENA RAVENCLAW",
    "tests/test_dir/test_create_directories_from_list/THE GREY LADY"
    ]

    assert(set(file_path) == set(test_file_path))

def test_dir_path_list():
    dir_dict = {'sub1': {'sub1_sub1': [], 'sub1_sub2': []}, 'sub2': {'sub2_sub1': []}, 'sub3': []}

    result_list = autodirs.dir_path_list(dir_dict, root_path='test_dir/dir_path_list')

    expected_list = ['test_dir/dir_path_list/sub1/sub1_sub1',
                     'test_dir/dir_path_list/sub1/sub1_sub2',
                     'test_dir/dir_path_list/sub2/sub2_sub1',
                     'test_dir/dir_path_list/sub3']

    assert(result_list == expected_list)
