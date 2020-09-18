import os
import glob


class Directories:
    """Creates the directories for storing the sub directories."""

    def __init__(self, path):
        """Instantiate a directories object with a name.

        :param path: Path where the directories need to be created.
        """

        self.path = path
        self.sub_dir_list = []

    def create_directories(self, sub_dir_names, dir_name=""):
        """Creates the sub directories inside a directory.

        :param sub_dir_names: a text file with the list of the sub directories.
        :param dir_name: name of the directory inside which the sub directories will be created (Default="").

        :raises TypeError: Missing positional arguments.
        """

        with open(sub_dir_names) as f:
            self.sub_dir_list = f.read().splitlines()

        if dir_name:
            dir_path = self.path + "/" + dir_name + "/"
        else:
            dir_path = self.path + "/"

        for i in range(len(self.sub_dir_list)):
            dir = dir_path + self.sub_dir_list[i]
            try:
                if not os.path.exists(dir):
                    os.makedirs(dir)
                else:
                    print(f"Directory: {dir} already exists!")
            except TypeError as e:
                print(e)
                raise

    def sub_dir_files(self, dir_name):
        """Returns a list of the files in the given directory

        :param dir_name: Name of the directory where the text files are stored.

        :returns file_path: List of all the files present in {dir_name}
        :returns file_list: List of all the file titles present in {dir_name}

        :raises ValueError: Invalid input.
        """
        try:
            file_path = [f for f in glob.glob("text_files" + "**/*txt", recursive=True)]

            file_list = [f.rsplit('.',3)[0] for f in os.listdir("text_files") if f.endswith('.txt')]
        except ValueError as e:
            print(e)
            raise

        return file_path, file_list

    def group_by_text_files(self, text_path):
        """Creates directory structure within the {self.path}.
        The {text_path} file name forms the directory in the root of the path.
        The list inside the text files form the sub directories.

        :param text_path: path where the text files are located.
        """

        file_path, file_list = self.sub_dir_files(text_path)

        for i in range(len(file_path)):
            self.create_directories(file_path[i], file_list[i])
