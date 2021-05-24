include .env

########################
# commands
# ######################

active: ## :: Active virtual environment
	source ./venv/bin/activate

image: ## :: Generate Image
	sh generate-image.sh

start: ## :: Up iBolo-API 
	docker-compose up -d

logs: ## :: Logs iBolo-API 
	docker-compose -f docker-compose.yaml logs -f

stop: ## :: Stop iBolo-API
	docker-compose -f docker-compose.yaml stop

list:
	@ echo "Define scripts to run iBolo API  locally."
	@ echo " "
	@ echo "Usage:"
	@ echo "	make [COMMAND] [ARGS...]"
	@ echo " "
	@ echo "Options:"
	@ echo " "
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sed -n '	s/^\(.*\): \(.*\)##\(.*\)/\1\3/p'

