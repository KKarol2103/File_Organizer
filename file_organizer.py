import os
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from file_finder import FileSysFinder
from file_comparision import FileComparision

class FileOrganizer:
    def __init__(self, main_dir: Path, *args: tuple[Path]):
        self._main_dir = main_dir
        self._other_directories = list(args)
        self.file_finder = FileSysFinder(self._other_directories + [main_dir])


    def organize_fs(self):
        all_fs_files = self.file_finder.files
        empty_files, duplicates = self.file_finder.find_empty_files(), self.file_finder.find_duplicates()
        if empty_files:
            show_empty_files(empty_files)
            dec = get_decision_from_user()
            perform_action(dec, empty_files)
        if duplicates:
            show_duplicates(duplicates)
            dec = ask_what_to_do_with_duplicates(self._main_dir)
            if dec == 1:
                self.remove_duplicates(self._main_dir, duplicates)


    def remove_files_from_fs(self, files_to_remove: list[Path]):
        for file in list(files_to_remove):
            os.remove(Path.absolute(file))
        self.file_finder.update()
    

    def remove_duplicates(self, main_dir: Path, duplicates: defaultdict[Path, list[Path]]):
        for file, f_duplicates in duplicates.items():
            duplicates_together = f_duplicates + [file]
            for dup in duplicates_together:
                if str(main_dir) not in str(dup):
                    os.remove(dup)
        self.file_finder.update()


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


def get_decision_from_user()->int:
    print("Decide what to do with empty files:")
    print('1. Remove all empty files')
    print('2. Leave all empty files')
    print('3. Remove only selected files')
    return int(input("Decision:"))


def ask_what_to_do_with_duplicates(main_dir: Path) -> int:
    print("Decide what to do with duplicates")
    print(f'1. Delete all duplicates outside main dir (outside {main_dir})')
    print("2. Leave all duplicates")
    return int(input("Decision:"))
        



def perform_action(decision: int, empty_files:list[Path]):
    if decision == 1:
        print("Removing empty files...")
        # TODO think about it
        # remove_files_from_fs(empty_files)
        print("Done")

    if decision == 3:
        remove_mode = True
        while(remove_mode):
            print("Type file number to remove")
            f_number = int(input('File number: '))
            # remove_files_from_fs([empty_files[f_number]])
            print('File removed')
            dec = input("Would You like to remove other files? [y/n]")
            remove_mode = True if dec == 'y' else False



        
     

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
    file_organizer = FileOrganizer(args.dst_dir.absolute(), *absolute_paths)
    file_organizer.organize_fs()

if __name__ == "__main__":
    main()

