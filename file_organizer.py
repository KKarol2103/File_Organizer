import os
from argparse import ArgumentParser
from pathlib import Path
from itertools import chain

def get_all_files_from_dir(dir_path: Path) -> Path:
    return [path for path in dir_path.glob('**/*') if path.is_file()]

def compare_two_files(file1: Path, file2: Path) -> bool:
    # TODO maybe think about readbytes
    with open(file1, 'rb') as file1_h, open(file2, 'rb') as file2_h:
        return file1_h.read() == file2_h.read()
    
def check_if_file_empty(file: Path) -> bool:
    return True if os.stat(file).st_size == 0 else False

def remove_empty_files_from_fs(empty_files: list[Path]):
    for e_file in list(empty_files):
        os.remove(e_file)

def organize_fs(dst_dir: Path, *args):
    dst_dir_files = get_all_files_from_dir(dst_dir)
    all_fs_files = [get_all_files_from_dir(dir) for dir in args]
    all_fs_files = list(chain.from_iterable(all_fs_files))
    all_fs_files.extend(dst_dir_files)
    empty_files = filter(check_if_file_empty, all_fs_files)
    remove_empty_files_from_fs(empty_files)


def main():
    print(Path.cwd())

if __name__ == "__main__":
    main()

