import pytest
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