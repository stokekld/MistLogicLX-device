C=dpkg-deb --build
PROJECT=mistlogic
VERSION=0.1
REVISION=1
PACKAGE=$(PROJECT)_$(VERSION)-$(REVISION)

DEBIAN_DIR=$(PACKAGE)/DEBIAN/
PROJECT_DIR=$(PACKAGE)/etc/$(PROJECT)
SYSTEMD_DIR=$(PACKAGE)/lib/systemd/system/

all: $(PACKAGE)

$(PACKAGE):
	mkdir -p $(DEBIAN_DIR)
	mkdir -p $(PROJECT_DIR)
	mkdir -p $(SYSTEMD_DIR)
	cp control $(DEBIAN_DIR)
	cp -r ../mistlogic/* $(PROJECT_DIR)
	cp mistlogic.service $(SYSTEMD_DIR)

	pip install -t mistlogic_0.1-1/etc/mistlogic/lib/ -r mistlogic_0.1-1/etc/mistlogic/front-end/requeriments.txt

	$(C) $(PACKAGE)

clean:
	rm -rf $(PACKAGE)

