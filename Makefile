include .env
export $(shell sed 's/=.*//' .env)

mock:
	@psql postgresql://$(DB1_USER):$(DB1_PASSWORD)@$(DB1_HOST):$(DB1_PORT)/$(DB1_NAME) -f mocks/create_restaurants.sql
	@psql postgresql://$(DB1_USER):$(DB1_PASSWORD)@$(DB1_HOST):$(DB1_PORT)/$(DB1_NAME) -f mocks/create_open_close_times.sql
	@psql postgresql://$(DB1_USER):$(DB1_PASSWORD)@$(DB1_HOST):$(DB1_PORT)/$(DB1_NAME) -f mocks/create_groups.sql
	@psql postgresql://$(DB1_USER):$(DB1_PASSWORD)@$(DB1_HOST):$(DB1_PORT)/$(DB1_NAME) -f mocks/create_transactions_table.sql
	@python mocks/generate_transactions.py
	@psql postgresql://$(DB1_USER):$(DB1_PASSWORD)@$(DB1_HOST):$(DB1_PORT)/$(DB1_NAME) -f mocks/insert_transactions.sql