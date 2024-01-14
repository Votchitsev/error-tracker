dev:
	docker-compose -f docker-compose.dev.yml up --build

build:
	docker-compose up -d --build

down:
	docker-compose down
