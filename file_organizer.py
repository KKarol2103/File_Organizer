import os
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from itertools import chain

def get_all_files_from_dir(dir_path: Path) -> list[Path]:
    return [path for path in dir_path.glob('**/*') if path.is_file()]


def get_all_fs_files(dst_dir, *args) -> list[Path]:
    dst_dir_files = get_all_files_from_dir(dst_dir)
    other_dir_files = [get_all_files_from_dir(dir) for dir in args]
    all_fs_files = list(chain.from_iterable(other_dir_files))
    all_fs_files.extend(dst_dir_files)
    return all_fs_files


def compare_two_files(file1: Path, file2: Path) -> bool:
    with open(file1, 'rb') as file1_h, open(file2, 'rb') as file2_h:
        return file1_h.read() == file2_h.read()
    
def check_if_file_empty(file: Path) -> bool:
    return True if os.stat(file).st_size == 0 else False

def find_empty_files(all_files: list[Path]) -> list[Path]:
    return list(filter(check_if_file_empty, all_files))

def find_duplicates(all_files: list[Path]) -> dict[Path, list[Path]]:
    duplicates = defaultdict(list)
    for index, file in enumerate(all_files):
        if file in list(chain.from_iterable(duplicates.values())):
            continue

        for another_file in all_files[index+1:]:
            if compare_two_files(file, another_file):
                duplicates[file].append(another_file)
    
    return duplicates

def find_empty_files_and_duplicates(all_fs_files: list[Path]) -> tuple:
    return find_empty_files(all_fs_files) , find_duplicates(all_fs_files)


def check_if_file_is_newer_ver_of_other(file1: Path, file2: Path) -> bool:
    return os.stat(file1).st_ctime >= os.stat(file2).st_ctime 

def find_newer_ver_of_file(all_files: list[Path]):
    newer_ver = defaultdict(list)
    for index, file in enumerate(all_files):
        if file in list(chain.from_iterable(newer_ver.values())):
            continue

        for another_file in all_files[index+1:]:
            if check_if_file_is_newer_ver_of_other(file, another_file):
                newer_ver[file].append(another_file)
    
    return newer_ver


def remove_files_from_fs(files_to_remove: list[Path]):
    for file in list(files_to_remove):
        os.remove(Path.absolute(file))

def show_empty_files(empty_files: list[Path]):
    print("Empty files found: ")
    for index, e_file in enumerate(empty_files):
        print(f'{index}: at {Path.absolute(e_file)}')

def show_duplicates(duplicates: defaultdict[Path, list[Path]]):
    print("\nDuplicates found \n")
    index = 0
    for key, val in duplicates.items():
        print(f'{index}. Original file: {key}')
        print('Duplicates: ')
        for dup in val:
            print(f'Location: {dup}')
        index += 1
        print('\n')
    
    print("Now decide what to do with duplicates")
    print("1. Delete all duplicates outside main dir")
    print("2. Leave all duplicates")




def get_decision_from_user()->int:
    print("Decide what to do with empty files:")
    print('1. Remove all empty files')
    print('2. Leave all empty files')
    print('3. Remove only selected files')
    return int(input("Decision:"))


def perform_action(decision: int, empty_files:list[Path]):
    if decision == 1:
        print("Removing empty files...")
        remove_files_from_fs(empty_files)
        print("Done")

    if decision == 3:
        remove_mode = True
        while(remove_mode):
            print("Type file number to remove")
            f_number = int(input('File number: '))
            remove_files_from_fs([empty_files[f_number]])
            print('File removed')
            dec = input("Would You like to remove other files? [y/n]")
            remove_mode = True if dec == 'y' else False

def organize_fs(dst_dir: Path, *args):
    all_fs_files = get_all_fs_files(dst_dir, *args)
    empty_files, duplicates = find_empty_files_and_duplicates(all_fs_files)
    if empty_files:
        show_empty_files(empty_files)
        dec = get_decision_from_user()
        perform_action(dec, empty_files)
    if duplicates:
        show_duplicates(duplicates)
        
     

def main():
    parser = ArgumentParser()
    parser.add_argument("dst_dir", help="Main dir where you want to organize your files", type=Path)
    parser.add_argument("other_dir", help="Other dirs", nargs='+', type=Path)
    args = parser.parse_args()


    absolute_paths = [Path.absolute(dir) for dir in args.other_dir]

    print(f'Main Directory Selected: {args.dst_dir}')
    print(f'Other Directories: {args.other_dir}')

    print('Welcome to the file organizer!')
    print("Starting organizing!")
    organize_fs(args.dst_dir.absolute(), *absolute_paths)

if __name__ == "__main__":
    main()

