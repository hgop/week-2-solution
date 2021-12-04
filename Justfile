verify:
    ./scripts/verify_local_dev_environment.sh

venv:
    python3 -m venv --prompt hgop .venv

start:
	docker-compose down
	docker-compose rm
	docker-compose up --build

ssh-microk8s:
    ssh -i "~/.aws/keys/{{TEAM_NAME}}.pem" ubuntu@{{TEAM_NAME}}.hgopteam.com
