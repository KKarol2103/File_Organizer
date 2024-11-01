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


