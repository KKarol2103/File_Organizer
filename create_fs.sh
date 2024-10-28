#!/bin/bash
mkdir test/
cd test/
mkdir -p X/some_dir/photos
mkdir -p X/docs
mkdir -p Y1/trips
mkdir -p Y2/data
mkdir -p Y2/photos


mkdir Y3/

echo "Some_basic_file" > X/a.txt
touch X/some_dir/empty.dat
echo "Info about trip" > X/docs/trip.docx
echo "Photo1" > X/some_dir/photos/photo1.png
echo "Photo2" > X/some_dir/photos/photo2.png
echo "Photo3" > X/some_dir/photos/photo3.png

touch Y1/photo_cpy.png
touch Y1/trips/trip_to_US.docx
touch Y1/trips/Ncosts.txt

echo "Photo1" > Y1/photo_cpy.png
echo "Info about trip" > Y1/trips/trip_to_US.docx
echo "trip costs" > Y1/trips/Ncosts.txt

echo "Photo1" > Y2/photos/photo1.png
echo "Photo2" > Y2/photos/photo2.png
echo "Photo3" > Y2/photos/photo3.png
echo "Some_basic_file" > Y2/data/a.txt
echo "b txt info" > Y2/data/b.txt
echo "c txt info" > Y2/data/c.txt

touch Y3/empty.dat
touch Y3/empty1.dat
touch Y3/empty2.dat

echo "Test file System Created"
