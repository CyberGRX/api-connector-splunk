VERSION := $(shell cat VERSION)

build:
	@echo Building $(VERSION)
	cp README.md README.txt

	# Remove the .tgz if it exists
	cd ../ && rm -f api-connector-splunk-$(VERSION).tgz
	cd ../ && rm -f api-connector-splunk-$(VERSION).tgz.sha

	# Remove the .spl if it exists
	cd ../ && rm -f api-connector-splunk-$(VERSION).spl
	cd ../ && rm -f api-connector-splunk-$(VERSION).spl.sha

	cd ../ && tar --exclude='.git' --exclude='docs' --exclude='README.md' --exclude='HOW-TO.md' --exclude='VERSION' --exclude='LICENSE' --exclude='Makefile' --exclude='.editorconfig' --exclude='.pre-commit-config.yaml' --exclude='setup.cfg' -zcvf api-connector-splunk-$(VERSION).tgz api-connector-splunk
	cd ../ && shasum -a 256 api-connector-splunk-$(VERSION).tgz > api-connector-splunk-$(VERSION).tgz.sha
	rm README.txt

release:
	@echo Releasing $(VERSION) Expecting to find spl file in ~/Downloads
	cd ../ && rm -f api-connector-splunk-$(VERSION).spl
	cd ../ && mv ~/Downloads/api-connector-splunk-$(VERSION).spl ./
	cd ../ && shasum -a 256 api-connector-splunk-$(VERSION).spl > api-connector-splunk-$(VERSION).spl.sha
	cd ../ && shasum -c api-connector-splunk-$(VERSION).tgz.sha
	cd ../ && shasum -c api-connector-splunk-$(VERSION).spl.sha

prep:
	rm -f README.txt
	rm -f metadata/local.meta
	python3.7 -m json.tool --sort-keys api-connector-splunk.aob_meta api-connector-splunk.aob_meta-proc && mv api-connector-splunk.aob_meta-proc api-connector-splunk.aob_meta
	python3.7 -m json.tool --sort-keys app.manifest app.manifest-proc && mv app.manifest-proc app.manifest
	cd appserver/static/js/build && python3.7 -m json.tool --sort-keys globalConfig.json globalConfig.json-proc && mv globalConfig.json-proc globalConfig.json
