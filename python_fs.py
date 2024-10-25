from pyfakefs.fake_filesystem_unittest import Patcher

def create_fs():
    with Patcher(allow_root_user=False) as patcher:
        patcher.fs.create_dir('X')
        patcher.fs.create_dir('X/docs')
        patcher.fs.create_dir('X/some_dir')
        patcher.fs.create_dir('X/some_dir/photos')

        patcher.fs.create_file('X/a.txt', contents='Some_basic_file')
        patcher.fs.create_file('X/some_dir/empty.dat')
        patcher.fs.create_file('X/docs/trip.docx', contents='Info about trip')
        patcher.fs.create_file('X/some_dir/photos/photo1.png', contents='Photo1')
        patcher.fs.create_file('X/some_dir/photos/photo2.png', contents='Photo2')
        patcher.fs.create_file('X/some_dir/photos/photo3.png', contents='Photo3')


        patcher.fs.create_dir('Y1')
        patcher.fs.create_dir('Y1/trips')
        
        patcher.fs.create_file('Y1/photo_cpy.png', contents='Photo1')
        patcher.fs.create_file('Y1/trips/trip_to_US.docx', contents='Info about trip')
        patcher.fs.create_file('Y1/trips/Ncosts.txt', contents='trip costs')

        return patcher.fs
    

def print_fs_tree(messy_fs, path='X', level=0):
    """Recursively print the structure of the fake filesystem."""
    indent = '  ' * level
    for name in messy_fs.listdir(path):
        print(f"{indent}{name}")
        if messy_fs.isdir(messy_fs.joinpaths(path, name)):
            print_fs_tree(messy_fs, messy_fs.joinpaths(path, name), level + 1)

print_fs_tree(create_fs())