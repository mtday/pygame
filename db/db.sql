
-- For local development, you can create the PostgreSQL database, user, and password with:
--
-- CREATE DATABASE mygame;
-- CREATE USER mygame WITH PASSWORD 'password';
-- ALTER ROLE mygame WITH CREATEDB;
--

CREATE TABLE users (
    id                SERIAL         NOT NULL,
    login             VARCHAR(100)   NOT NULL,

    CONSTRAINT users_pk PRIMARY KEY (id),
    CONSTRAINT users_uniq_login UNIQUE (login)
);


CREATE TABLE games (
    id                SERIAL         NOT NULL,
    user_id           INTEGER        NOT NULL,

    CONSTRAINT games_pk PRIMARY KEY (id),
    CONSTRAINT games_fk_user_id FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);


CREATE TABLE units (
    id                SERIAL         NOT NULL,
    user_id           INTEGER        NOT NULL,
    game_id           INTEGER        NOT NULL,
    type              VARCHAR(30)    NOT NULL,
    coord_x           INTEGER        NOT NULL,
    coord_z           INTEGER        NOT NULL,

    CONSTRAINT units_pk PRIMARY KEY (id),
    CONSTRAINT units_fk_user_id FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    CONSTRAINT units_fk_game_id FOREIGN KEY (game_id) REFERENCES games (id) ON DELETE CASCADE
);

