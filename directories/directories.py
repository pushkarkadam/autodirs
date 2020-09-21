import os
import glob


def create_directories(sub_dir_names, path=""):
    """Creates the sub directories inside a directory.

    :param sub_dir_names: A text file with the list of the sub directories.
    :param path: The file path to create the subdirectories from {sub_dir_list}  (Default="").

    :raises TypeError: Missing positional arguments.
    """

    with open(sub_dir_names) as f:
        sub_dir_list = f.read().splitlines()

    for i in range(len(sub_dir_list)):
        dir = path + "/" + sub_dir_list[i]
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
            else:
                print(f"Directory: {dir} already exists!")
        except TypeError as e:
            print(e)
            raise

def sub_dir_files(dir_name):
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

def group_by_text_files(text_path, path=""):
    """Creates directory structure to the set path from a group of text files.
    The {text_path} file name forms the directory in the root of the {path}.
    The list inside the text files form the sub directories.

    :param text_path: path where the text files are located.
    :param path: path where the directories must be created.
    """

    file_path, file_list = sub_dir_files(text_path)

    for i in range(len(file_path)):
        final_path = path + "/" + file_list[i]
        create_directories(file_path[i], final_path)
