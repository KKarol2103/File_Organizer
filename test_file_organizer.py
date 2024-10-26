import pytest
import os
from file_organizer import get_all_files_from_dir, check_if_file_empty, organize_fs, find_empty_files, Path
from pyfakefs.fake_filesystem_unittest import Patcher


@pytest.fixture
def messy_fs():
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

        patcher.fs.create_dir('Y2')
        patcher.fs.create_dir('Y2/data')
        patcher.fs.create_dir('Y2/photos')

        patcher.fs.create_file('Y2/photos/photo1.png', contents='Photo1')
        patcher.fs.create_file('Y2/photos/photo2.png', contents='Photo2')
        patcher.fs.create_file('Y2/photos/photo3.png', contents='Photo3')

        patcher.fs.create_file('Y2/data/a.txt', contents='Some_basic_file')
        patcher.fs.create_file('Y2/data/b.txt', contents='b txt info')
        patcher.fs.create_file('Y2/data/c.txt', contents='c txt info')

        patcher.fs.create_dir('Y3')
        patcher.fs.create_file('Y3/empty.dat')
        patcher.fs.create_file('Y3/empty1.dat')
        patcher.fs.create_file('Y3/empty2.dat')

        yield patcher.fs

def test_get_all_files_from_dir(messy_fs):
    files = get_all_files_from_dir(Path('Y1'))
    assert Path('Y1/photo_cpy.png') in files
    assert Path('Y1/trips/trip_to_US.docx') in files
    assert Path('Y1/trips/Ncosts.txt') in files
    assert len(files) == 3


def test_get_all_files_from_complex_dir(messy_fs):
    files = get_all_files_from_dir(Path('X'))
    assert Path('X/some_dir/photos/photo1.png') in files
    assert len(files) == 6

def test_if_file_is_empty(messy_fs):
    assert check_if_file_empty(Path('X/some_dir/empty.dat')) is True
    assert check_if_file_empty(Path('X/a.txt')) is False

def test_find_empty_files_in_fs(messy_fs):
    filesX = get_all_files_from_dir(Path('X'))
    filesY1 = get_all_files_from_dir(Path('Y1'))
    filesY2 = get_all_files_from_dir(Path('Y2'))
    filesY3 = get_all_files_from_dir(Path('Y3'))
    all_files = filesX + filesY1 + filesY2 + filesY3
    empty_files = list(find_empty_files(all_files))
    assert Path('X/some_dir/empty.dat') in empty_files
    assert Path('Y3/empty.dat') in empty_files
    assert Path('Y3/empty1.dat') in empty_files
    assert Path('Y3/empty2.dat') in empty_files
    assert len(empty_files) == 4



def test_remove_empty_files_from_fs(messy_fs):
    fs_size_before = len(get_all_files_from_dir(Path('X')) + get_all_files_from_dir(Path('Y1')) + get_all_files_from_dir(Path('Y3')))
    organize_fs(Path('X'), Path('Y1'), Path('Y3'))
    fs_size_after = len(get_all_files_from_dir(Path('X')) + get_all_files_from_dir(Path('Y1')) + get_all_files_from_dir(Path('Y3')))

    assert messy_fs.exists('X/some_dir/empty.dat') is False
    assert messy_fs.exists('Y3/empty1.dat') is False
    assert fs_size_after == fs_size_before - 4

