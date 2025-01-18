'1.'
CREATE DATABASE db_blackmounster;
CREATE USER blackmounster_user WITH PASSWORD 'blackmounster_pass';
ALTER ROLE blackmounster_user SET client_encoding TO 'utf8';
ALTER ROLE blackmounster_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE blackmounster_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE db_blackmounster TO blackmounster_user;
ALTER USER blackmounster_user WITH SUPERUSER;
\q