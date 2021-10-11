import sys
sys.path.append('../')

from autodirs import directories as di

dir_dict = {'sub1': {'sub1_sub1': [], 'sub1_sub2': []}, 'sub2': {'sub2_sub1': []}, 'sub3': []}

di.create_dirs_from_dict(dir_dict, root_path='dirs_from_dict')
