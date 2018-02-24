#!/bin/bash
sudo mount /dev/sda1 /mnt/usb
rm -rf /mnt/usb/images/
cp -r images /mnt/usb/
sudo umount /mnt/usb/
