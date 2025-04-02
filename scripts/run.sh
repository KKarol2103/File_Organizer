#!/bin/bash

./delete_fs.sh; ./create_fs.sh; python3 ./file_organizer.py test/X test/Y1 test/Y2 test/Y3
