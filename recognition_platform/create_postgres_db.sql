CREATE DATABASE db;
CREATE USER test_user WITH PASSWORD 'password';
ALTER ROLE test_user SET client_encoding TO 'utf8';
ALTER ROLE test_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE test_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE db TO test_user;