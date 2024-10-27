import os
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from itertools import chain

def get_all_files_from_dir(dir_path: Path) -> list[Path]:
    return [path for path in dir_path.glob('**/*') if path.is_file()]

def compare_two_files(file1: Path, file2: Path) -> bool:
    with open(file1, 'rb') as file1_h, open(file2, 'rb') as file2_h:
        return file1_h.read() == file2_h.read()
    
def check_if_file_empty(file: Path) -> bool:
    return True if os.stat(file).st_size == 0 else False

def find_empty_files(all_files: list[Path]) -> list[Path]:
    return filter(check_if_file_empty, all_files)

def find_duplicates(all_files: list[Path]) -> dict[Path, list[Path]]:
    duplicates = defaultdict(list)
    for index, file in enumerate(all_files):
        if file in list(chain.from_iterable(duplicates.values())):
            continue

        for another_file in all_files[index+1:]:
            if compare_two_files(file, another_file):
                duplicates[file].append(another_file)
    
    return duplicates

def remove_empty_files_from_fs(empty_files: list[Path]):
    for e_file in list(empty_files):
        os.remove(e_file)

def get_all_fs_files(dst_dir, *args) -> list[Path]:
    dst_dir_files = get_all_files_from_dir(dst_dir)
    other_dir_files = [get_all_files_from_dir(dir) for dir in args]
    all_fs_files = list(chain.from_iterable(other_dir_files))
    all_fs_files.extend(dst_dir_files)
    return all_fs_files

def find_empty_files_and_duplicates(all_fs_files: list[Path]) -> tuple:
    return find_empty_files(all_fs_files) , find_duplicates(all_fs_files)

def organize_fs(dst_dir: Path, *args):
    all_fs_files = get_all_fs_files(dst_dir, *args)
    empty_files, duplicates = find_empty_files_and_duplicates(all_fs_files)
    # TODO temp

    print("Empty files found: ")
    for index, e_file in enumerate(empty_files):
        print(f'{index}: at {Path.absolute(e_file)}')
     

def main():
    parser = ArgumentParser()
    parser.add_argument("dst_dir", help="Main dir where we want to organize our files into", type=Path)
    parser.add_argument("other_dir", help="Other dir", nargs='+', type=Path)
    args = parser.parse_args()

    other_dirs = args.other_dir[0] if len(args.other_dir) == 1 else args.other_dir

    print(f'Main Directory Selected: {args.dst_dir}')
    print(f'Other Directories: {args.other_dir}')

    print('Welcome to the file organizer!')
    print("Starting organizing!")
    print("Looking for empty files and duplicates")
    organize_fs(args.dst_dir, *other_dirs)

if __name__ == "__main__":
    main()

