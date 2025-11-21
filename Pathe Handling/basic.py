from pathlib import Path as ph

# assign a path name to a variable
#my_file=ph('my file.txt')
#new_folder=ph('my folder')
#BASE_DIR=ph(__file__).parent
#article_folder=BASE_DIR/'News' / 'Articles'

#article_folder.mkdir(parents=True, exist_ok=True)
#post_file=article_folder / 'post1.4.txt'
#post_file.write_text('Hello World!')

# create a new file, folder, file inside folder
#my_file.touch()
#new_folder.mkdir()
#ml_file= new_folder / "ML.py"
#ml_file.touch()

#templete = '''
#This is  file {number}{version} 
#import pandas as pds

#df = pds.DataFrame({{'name': ['Alex','Brian',25]}})
#'''
# write multiple files. 
#for i in range(1,6):
#    py_file=ph(f'py_file{i}.py')
#    py_file.write_text(templete.format(number=i, version=i+3))

#read a file in given dir
current_file=ph('.')
#print(current_file.resolve())
#for path in current_file.iterdir():
#    print(path.name)
#print()

# read all files inside dir and subdir
#for path in current_file.glob('**/*'):
#    print(path.name)

# Delete an existing file
#ph("my file.txt").unlink()

# Delete all same type of files
#for path in current_file.iterdir():
#    if 'py_file' in path.name:
#        path.unlink() 

# some cummon attributes and methods
file=ph('my file.txt')
file.touch()


file_name=file.name
file_suffix=file.suffix
file_stem=file.stem
file_create_datetime=file.stat().st_ctime

print(
    f'File name: {file_name}',
    f'File_suffix: {file_suffix}',
    f'File_stem: {file_stem}',
    f'File_Create_Datetime: {file_create_datetime}',
    sep='\n'
)