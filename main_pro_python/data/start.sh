#!/bin/sh
echo "starting project...."
x-terminal-emulator --working-directory='/home/kabir/codes/python/face/main_pro/check/' -e python /home/kabir/codes/python/face/main_pro/check/hi.py

x-terminal-emulator --working-directory='/home/kabir/codes/python/face/main_pro/data/' -e python /home/kabir/codes/python/face/main_pro/data/check.py

x-terminal-emulator --working-directory='/var/www/html/main_pro/upload/' -e python /var/www/html/main_pro/upload/move.py

x-terminal-emulator --working-directory='/var/www/html/main_pro/' -e python /var/www/html/main_pro/move.py

x-terminal-emulator --working-directory='/var/www/html/main_pro/' -e python /var/www/html/main_pro/delete_data.py

echo "done"
