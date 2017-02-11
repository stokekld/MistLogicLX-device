
DIR_DIST=./dist
NEWHOSTNAME=mist

PACKAGES=net-tools,iw,hostapd,wpasupplicant,isc-dhcp-client,isc-dhcp-server,python2.7
PACKAGES_DEV=$(PACKAGES),vim

NOPACKAGE=acl,adduser,gcc-4.8-base:armhf,gcc-4.9-base:armhf,grep,gzip,perl-base,sed,tar,zlib1g:armhf

sys:
	debootstrap --arch=armhf --variant=minbase --exclude=$(NOPACKAGE) --include=$(PACKAGES) --foreign jessie $(DIR_DIST) http://ftp.us.debian.org/debian

sys_dev:
	debootstrap --arch=armhf --variant=minbase --include=$(PACKAGES_DEV) --foreign jessie $(DIR_DIST) http://ftp.us.debian.org/debian

drivers:
	cp -rv drivers/* $(DIR_DIST)/lib

fstab:
	cat files/fstab > $(DIR_DIST)/etc/fstab

host:
	echo "$(NEWHOSTNAME)" > $(DIR_DIST)/etc/hostname

hostapd:
	mkdir $(DIR_DIST)/etc/hostapd
	cp files/hostapd.conf $(DIR_DIST)/etc/hostapd

dist:		sys fstab host drivers hostapd

dist_dev:	sys_dev fstab host drivers hostapd

clean:
	rm -rf $(DIR_DIST)

.PHONY: drivers
