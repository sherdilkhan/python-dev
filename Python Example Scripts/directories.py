
#import classes from libraries / directories

#lets import a class "Path" from "pathlib" directory


from pathlib import Path

path = Path('HelloWorld')  # Path() means current directory whihc is "HelloWorld"

for file in path.glob('*.*'):
    print(file)

