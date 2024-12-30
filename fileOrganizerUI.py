from collections import defaultdict
from pathlib import Path

class FileOrganizerUI:
    @staticmethod
    def show_empty_files(empty_files: list[Path]):
        print("Empty files found: ")
        for index, e_file in enumerate(empty_files):
            print(f'{index}: at {Path.absolute(e_file)}')

    @staticmethod
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

    @staticmethod
    def show_files_with_bad_names(files_with_bad_names: list[Path]):
        print("\nBad Names found \n")
        for i, bad_file in enumerate(files_with_bad_names):
            print(f'{i} {bad_file}')

    @staticmethod
    def get_decision_from_user()->int:
        print("Decide what to do with empty files:")
        print('1. Remove all empty files')
        print('2. Leave all empty files')
        print('3. Remove only selected files')
        return int(input("Decision:"))

    @staticmethod
    def ask_what_to_do_with_duplicates(main_dir: Path) -> int:
        print("Decide what to do with duplicates")
        print(f'1. Delete all duplicates outside main dir (outside {main_dir})')
        print("2. Leave all duplicates")
        return int(input("Decision:"))
    
    @staticmethod
    def ask_what_to_do_with_bad_f_names() -> int:
        print("Decide what to do with these bad names")
        print("1. Replace all bad symbols in file names with given char (Default char: '_' )")
        print("2. Do nothing")
        return int(input("Decision:"))

    @staticmethod
    def ask_which_files_to_remove() -> list[int]:
        f_numbers_as_str = input('File number: ').split()
        f_numbers = [int(f_str) for f_str in f_numbers_as_str]
        return f_numbers


    @staticmethod
    def show_action(decision: int):
        if decision == 1:
            print("Removing empty files...")

        if decision == 3:
            print("Type file numbers to remove - SEPARATE BY SPACE")

            


