IMAGENAME=stocks
# Getting the absolute path of this file so that we can run it from anywhere
# NOTE: these are makefile specific commands
CURR_PATH=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

build :
	docker build -f $(CURR_PATH)/Dockerfile -t $(IMAGENAME) .

run :
	docker run $(IMAGENAME) /Stocks/startserver.sh