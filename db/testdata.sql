
INSERT INTO users (id, login) VALUES (1, 'user');

INSERT INTO games (id, user_id) VALUES (1, 1);

INSERT INTO units (user_id, game_id, type, coord_x, coord_z) VALUES
(1, 1, 'SUN', 0, 0),
(1, 1, 'PLANET', 13, 8),
(1, 1, 'PLANET', -8, 20),
(1, 1, 'PLANET', -20, 5),
(1, 1, 'RECON_DRONE', 8, 13);

