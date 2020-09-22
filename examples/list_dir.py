import sys
sys.path.append('../')

from autodirs import directories as di

ravenclaw = [
"ROWENA RAVENCLAW",
"LUNA LOVEGOOD",
"GILDEROY LOCKHART",
"THE GREY LADY"
]

di.create_directories_from_list(ravenclaw, root="ravenclaw")
