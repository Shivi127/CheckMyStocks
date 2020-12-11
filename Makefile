IMAGE_NAME=stocks

# Getting the absolute path of this file so that we can run it from anywhere
# NOTE: these are makefile specific commands
CURR_PATH=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
MAKEFILE_PATH=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

build :
	docker build -f $(CURR_PATH)/Dockerfile -t $(IMAGE_NAME) .

run : build
	docker run -p 127.0.0.1:8080:8000 --rm $(IMAGE_NAME) /Stocks/startserver.sh

hop-in: 
	docker run -v $(MAKEFILE_PATH):/stocks/ -it $(IMAGE_NAME) /bin/bash