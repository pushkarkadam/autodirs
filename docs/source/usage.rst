.. highlight:: shell

=====
Usage
=====

To use autodirs in a project or in python terminal ::

    import autodirs.directories as di

See the examples in the /examples folder on GitHub for how to use each function.

The basic idea is that the user wants to generate multiple folders.
It is difficult to manually create folders on a computer.
This project aims at providing an automatic way of creating the directories.

Create directories from a text file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a text file with the names of all the directories that need to be created.

The user can create multiple directory by using the following command in the python console. ::

    import autodirs.directories as di

    di.create_directories_from_text("text_files/gryffindor.txt", "sub/house", with_text=True)


Create multiple directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to create nested directories using text files bundle all the text files which include the name of directories you wish to create.

For example, if you want to create a group of directories such as::

    house/

    _gryffindor/

        _HARRY POTTER/

        _HERMOINE GRANGER/

    _hufflepuff/

        _HELGA HUFFLEPUFF/

        _BRIDGET WENLOCK/

To create a directory structure like the above, store the directory names inside a text file.

**Example**: gryffindor.txt file should contain the following directory names::

    HARRY POTTER

    HERMOINE GRANGER

**Example**: hufflepuff.txt should contain the following directory names::

    HELGA HUFFLEPUFF

    BRIDGET WENLOCK

Both the text files: gryffindor.txt and hufflepuff.txt must be stored inside house/ directory


Create directories from list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to create directories from the list use the following code::

    import autodirs.directories as di

    ravenclaw = [
    "ROWENA RAVENCLAW",
    "LUNA LOVEGOOD",
    "GILDEROY LOCKHART",
    "THE GREY LADY"
    ]

    di.create_directories_from_list(ravenclaw, path="house")

Checkout the examples for more details.


Create directories from nested dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function is beneficial if you are building a software architecture where you need a function
to create a directory structure.

To create a nested directory structure using a dictionary use the following code::

    import autodirs.directories as di

    dir_dict = {'sub1': {'sub1_sub1': [], 'sub1_sub2': []}, 'sub2': {'sub2_sub1': []}, 'sub3': []}

    di.create_dirs_from_dict(dir_dict, root_path='dirs_from_dict')


Create nested directories from a text file with indentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For an easy way to create a directory structure, prepare a text file with .txt extension.

The text file can contain a nested directory structure as follows::

    PLANETS
        TRANTOR
            MYCOGEN
            IMPERIAL
                PALACE
        TERMINUS
        ANACREON
    MAYORS

Then use the following code to create the above mentioned nested directory structure::

    import autodirs.directories as di
    autodirs.create_nested_dirs_from_text(text='textfile.txt', root_path='root')
