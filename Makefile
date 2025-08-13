VENV_DIR = venv
REQUIREMENTS = req.txt

start:
	@docker build -t install_biz .
	@docker-compose up -d

stop:
	@docker-compose down

test:
	@docker-compose down
	@docker stop test_postgres || exit 0
	@docker pull postgres:17
	@docker run --rm --name test_postgres \
	    -e POSTGRES_PASSWORD=postgress \
	    -e POSTGRES_USER=postgres \
	    -e POSTGRES_DB=auth_test_db \
	    -d -p 5432:5432 postgres:17
	@container_name=test_postgres; \
	pattern="ready to accept connections"; \
	while ! docker logs "$$container_name" | grep -q "$$pattern"; do \
	  echo "Waiting for PostgreSQL container to be ready..."; \
	  sleep 0.1; \
	done; \
	echo "PostgreSQL container is ready"
	@MODE=TEST alembic upgrade head
	@python -m pytest
	@docker stop test_postgres

migrate:
	@docker-compose run web alembic upgrade head

venv:
	@if [ ! -d $(VENV_DIR) ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
	fi

install: venv
	@$(VENV_DIR)/bin/pip install --upgrade pip
	@$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

clean:
	@rm -rf $(VENV_DIR)

.PHONY: start stop test migrate venv install clean