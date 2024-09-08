BEGIN;

INSERT INTO planets (name, diameter, mass, temperature, atmosphere, composition) VALUES ('Earth', 12742.0, 5.97, 288.0, 'nitrogenio, oxigenio', 'ferro, oxigenio, silicio');
INSERT INTO planets (name, diameter, mass, temperature, atmosphere, composition) VALUES ('Mars', 6779.0, 0.642, 210.0, 'carbono', 'carbono, silicio');
INSERT INTO stars (name, luminosity, age, mass, spectral_type) VALUES ('Sun', 1.0, 4.6, 1.0, 'G');
INSERT INTO moons (name, diameter, orbital_period, density) VALUES ('lua', 3474.0, 27.3, 3.34);
INSERT INTO moons (name, diameter, orbital_period, density) VALUES ('Phobos', 22.4, 0.319, 1.876);
INSERT INTO moons (name, diameter, orbital_period, density) VALUES ('Deimos', 12.4, 1.263, 1.471);

COMMIT;
