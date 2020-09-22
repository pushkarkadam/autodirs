import os
import sys
import glob
import warnings


def _create_path_from_param(dir_name, root, path):
    """Returns the path based upon the parameters passed.

    :param dir_list: Name of the subdirectory.
    :param root: Root directory to contain subdirectories.
    :param path: Path where the root directory needs to be created.

    :returns final_path: The final path to the subdirectory.
    """

    if not root or not path:
        warnings.warn("Root folder or path not provided. This will create multiple folders in unexpected location!")
        response = input("Do you wish to continue?[y/n]: ")

        if response == 'n':
            sys.exit(1)

    if root and path:
        final_path = path + "/" + root + "/" + dir
    elif path and not root:
        final_path = path + "/" + dir
    elif root and not path:
        final_path = root + "/" + dir
    else:
        final_path = dir

    return final_path


def _sub_dir_files(dir_name):
    """Returns a list of the files in the given directory

    :param dir_name: Name of the directory where the text files are stored.

    :returns file_path: List of all the files present in {dir_name}
    :returns file_list: List of all the file titles present in {dir_name}

    :raises ValueError: Invalid input.
    """
    try:
        file_path = [f for f in glob.glob(dir_name + "**/*txt", recursive=True)]

        file_list = [f.rsplit('.',3)[0] for f in os.listdir(dir_name) if f.endswith('.txt')]
    except ValueError as e:
        print(e)
        raise

    return file_path, file_list


def create_directories(sub_dir_names, path=""):
    """Creates the sub directories inside a directory.

    :param sub_dir_names: A text file with the list of the sub directories.
    :param path: The file path to create the subdirectories from {sub_dir_list}  (Default="").

    :raises TypeError: Missing positional arguments.
    """

    with open(sub_dir_names) as f:
        sub_dir_list = f.read().splitlines()

    for sub_dir in sub_dir_list:
        dir = path + "/" + sub_dir
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
            else:
                print(f"Directory: {dir} already exists!")
        except TypeError as e:
            print(e)
            raise


def group_by_text_files(text_path, path=""):
    """Creates directory structure to the set path from a group of text files.
    The {text_path} file name forms the directory in the root of the {path}.
    The list inside the text files form the sub directories.

    :param text_path: path where the text files are located.
    :param path: path where the directories must be created.
    """

    file_path, file_list = _sub_dir_files(text_path)

    for file in file_path:
        final_path = path + "/" + file
        create_directories(file, final_path)


def create_directories_from_list(dir_list, root="", path=""):
    """Creates directory structure from the list provided.

    :param dir_list: List of the subdirectories.
    :param root: Root directory name.
    :param path: Path where the file structure must be created.
    """

    for dir in dir_list:
        final_path = _create_path_from_param(dir, root, path)
        try:
            if not os.path.exists(final_path):
                os.makedirs(final_path)
            else:
                print(f"Directory: {final_path} already exists!")
        except TypeError as e:
            print(e)
            raise
