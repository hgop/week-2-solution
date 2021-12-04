verify:
    ./scripts/verify_local_dev_environment.sh

venv:
    python3 -m venv --prompt hgop .venv

start:
	docker-compose down
	docker-compose rm
	docker-compose up --build

ssh-microk8s:
    ssh -i "~/.aws/keys/dreamteam.pem" ubuntu@dreamteam.hgopteam.com
