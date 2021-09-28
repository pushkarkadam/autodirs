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

def test_create_dirs_from_dict():
    dir_dict = {'sub1': {'sub1_sub1': [], 'sub1_sub2': []}, 'sub2': {'sub2_sub1': []}, 'sub3': []}

    autodirs.create_dirs_from_dict(dir_dict, root_path='tests/test_dir/dir_from_dict')

    file_path_sub = [dir.path for dir in os.scandir("tests/test_dir/dir_from_dict/") if dir.is_dir()]
    file_path_sub1 = [dir.path for dir in os.scandir("tests/test_dir/dir_from_dict/sub1") if dir.is_dir()]
    file_path_sub2 = [dir.path for dir in os.scandir("tests/test_dir/dir_from_dict/sub2") if dir.is_dir()]

    sub_contents = ['tests/test_dir/dir_from_dict/sub1',
                    'tests/test_dir/dir_from_dict/sub2',
                    'tests/test_dir/dir_from_dict/sub3']

    sub1_contents = ['tests/test_dir/dir_from_dict/sub1/sub1_sub1',
                     'tests/test_dir/dir_from_dict/sub1/sub1_sub2',]

    sub2_contents = ['tests/test_dir/dir_from_dict/sub2/sub2_sub1']

    assert(set(file_path_sub) == set(sub_contents))
    assert(set(file_path_sub1) == set(sub1_contents))
    assert(set(file_path_sub2) == set(sub2_contents))

def test_create_nested_dirs_from_text():
    autodirs.create_nested_dirs_from_text(text="tests/nested_test_file.txt", root_path="tests/test_dir/nested")

    # Gets: PLANETS, MAYORS
    file_path_sub1 = [dir.path for dir in os.scandir("tests/test_dir/nested/") if dir.is_dir()]

    # Gets: PLANETS/TRANTOR, PLANETS/TERMINUS, PLANETS/ANACREON
    file_path_sub2 = [dir.path for dir in os.scandir("tests/test_dir/nested/PLANETS") if dir.is_dir()]

    # Gets: PLANETS/TRANTOR/MYCOGEN, PLANETS/TRANTOR/IMPERIAL
    file_path_sub3 = [dir.path for dir in os.scandir("tests/test_dir/nested/PLANETS/TRANTOR") if dir.is_dir()]

    # Gets: PLANETS/TRANTOR/IMPERIAL/PALACE
    file_path_sub4 = [dir.path for dir in os.scandir("tests/test_dir/nested/PLANETS/TRANTOR/IMPERIAL") if dir.is_dir()]

    sub1_contents = ["tests/test_dir/nested/PLANETS", "tests/test_dir/nested/MAYORS"]
    sub2_contents = ["tests/test_dir/nested/PLANETS/TRANTOR", "tests/test_dir/nested/PLANETS/TERMINUS", "tests/test_dir/nested/PLANETS/ANACREON"]
    sub3_contents = ["tests/test_dir/nested/PLANETS/TRANTOR/MYCOGEN", "tests/test_dir/nested/PLANETS/TRANTOR/IMPERIAL"]
    sub4_contents = ["tests/test_dir/nested/PLANETS/TRANTOR/IMPERIAL/PALACE"]

    assert(set(file_path_sub1) == set(sub1_contents))
    assert(set(file_path_sub2) == set(sub2_contents))
    assert(set(file_path_sub3) == set(sub3_contents))
    assert(set(file_path_sub4) == set(sub4_contents))
