BEGIN;

INSERT INTO planets (name, diameter, mass, temperature, atmosphere, composition) VALUES ('BetaPrime', 4500.0, 0.92, -15.0, 'aluminio, hidrogenio', 'ferro, niquel, silicio');
INSERT INTO stars (name, luminosity, age, mass, spectral_type) VALUES ('BetaStar', 0.3, 9.7, 0.6, 'K');

COMMIT;
