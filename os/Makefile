
DIR_DIST=./dist
HOSTNAME=mist

PACKAGES=net-tools,wireless-tools,hostapd
PACKAGES_DEV=$(PACKAGES),vim

sys:
	debootstrap --arch=armhf --variant=minbase --include=$(PACKAGES) --foreign jessie $(DIR_DIST) http://ftp.us.debian.org/debian

sys_dev:
	debootstrap --arch=armhf --variant=minbase --include=$(PACKAGES_DEV) --foreign jessie $(DIR_DIST) http://ftp.us.debian.org/debian

fstab:
	cat files/fstab > $(DIR_DIST)/etc/fstab

host:
	echo "$(HOSTNAME)" > $(DIR_DIST)/etc/hostname

drivers:
	cp -rv drivers/* $(DIR_DIST)/lib/

dist:		sys fstab host drivers

dist_dev:	sys_dev fstab host drivers

clean:
	rm -rf $(DIR_DIST)
