def generate_sql_output(file_name, details):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("BEGIN;\n\n")
        
        # Inserindo planetas
        for planet in details['planets']:
            # Certifique-se de que cada item em details['planets'] é um dicionário
            if isinstance(planet, dict):
                file.write(
                    f"INSERT INTO planets (name, diameter, mass, temperature, atmosphere, composition) "
                    f"VALUES ('{planet.get('name', '')}', {planet.get('diameter', 0)}, {planet.get('mass', 0)}, {planet.get('temperature', 0)}, "
                    f"'{planet.get('atmosphere', '')}', '{planet.get('composition', '')}');\n"
                )
        
        # Inserindo estrelas
        for star in details['stars']:
            if isinstance(star, dict):
                file.write(
                    f"INSERT INTO stars (name, luminosity, age, mass, spectral_type) "
                    f"VALUES ('{star.get('name', '')}', {star.get('luminosity', 0)}, {star.get('age', 0)}, {star.get('mass', 0)}, "
                    f"'{star.get('spectral_type', '')}');\n"
                )
        
        # Inserindo luas
        for moon in details['moons']:
            if isinstance(moon, dict):
                file.write(
                    f"INSERT INTO moons (name, diameter, orbital_period, density) "
                    f"VALUES ('{moon.get('name', '')}', {moon.get('diameter', 0)}, {moon.get('orbital_period', 0)}, {moon.get('density', 0)});\n"
                )

        file.write("\nCOMMIT;\n")
