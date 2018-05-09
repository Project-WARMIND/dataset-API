--postgresql
CREATE TABLE hosts (
  id SERIAL PRIMARY KEY,
  uuid VARCHAR(255) NOT NULL,
  hostname VARCHAR(255),
  detected_os VARCHAR(255),
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC') NOT NULL,
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC') NOT NULL
);
CREATE TABLE tokens (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  token VARCHAR(255) NOT NULL,
  scope VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC') NOT NULL
);
