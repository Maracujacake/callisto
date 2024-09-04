grammar callisto;


NAME: [a-zA-Z]+;
NUMBER: [0-9]+ ('.' [0-9]+)?;
SPECTRAL_TYPE: 'O' | 'B' | 'A' | 'F' | 'G' | 'K' | 'M';
STRING: '"' (~["\r\n])* '"';
WS: [ \t\n\r]+ -> skip;

program: system+;

system: 'System' NAME '{' 'centralStar' ':' star ',' 'planets' ':' planetList '}';

centralStar: 'centralStar' ':' star;

planetList: '[' (planet (',' planet)*)? ']';


planet
    : 'Planet' NAME '{' 'diameter' ':' NUMBER ',' 'mass' ':' NUMBER ',' 'temperature' ':' NUMBER ',' 'atmosphere' ':' STRING ',' 'composition' ':' STRING ',' 'orbit' ':' orbit ',' 'moons' ':' moonList '}'
    ;


moonList: '[' (moon (',' moon)*)? ']';


moon
    : 'Moon' NAME '{' 'diameter' ':' NUMBER ',' 'orbitPeriod' ':' NUMBER ',' 'density' ':' NUMBER ',' 'surfaceType' ':' STRING '}'
    ;


star
    : 'Star' NAME '{' 'spectralType' ':' SPECTRAL_TYPE ',' 'luminosity' ':' NUMBER ',' 'age' ':' NUMBER ',' 'mass' ':' NUMBER '}'
    ;


orbit
    : 'Orbit' '{' 'semiMajorAxis' ':' NUMBER ',' 'eccentricity' ':' NUMBER '}'
    ;

