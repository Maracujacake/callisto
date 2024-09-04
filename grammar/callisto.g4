grammar callisto;

SYSTEM: 'System';
STAR: 'Star';
PLANET: 'Planet';
MOON: 'Moon';
ORBIT: 'Orbit';
CENTRALSTAR: 'centralStar';
PLANETS: 'planets';

SPECTRAL_TYPE: 'O' | 'B' | 'A' | 'F' | 'G' | 'K' | 'M';
NAME: ('a'..'z'|'A'..'Z')+;
NUMBER: ('0'..'9')+ ('.' ('0'..'9')+)?;
STRING: '"' ( ~('"' | '\r' | '\n') )* '"';
WS: (  '\n' | '\r' | '\t' )+ -> skip;

program: system+ EOF;

system: SYSTEM NAME '{' 'centralStar' ':' star ',' 'planets' ':' planetList '}';

planetList: '[' (planet (',' planet)*)? ']';

planet
    : PLANET NAME '{' 'diameter' ':' NUMBER ',' 'mass' ':' NUMBER ',' 'temperature' ':' NUMBER ',' 'atmosphere' ':' STRING ',' 'composition' ':' STRING ',' 'orbit' ':' orbit ',' 'moons' ':' moonList '}'
    ;

moonList: '[' (moon (',' moon)*)? ']';

moon
    : MOON NAME '{' 'diameter' ':' NUMBER ',' 'orbitPeriod' ':' NUMBER ',' 'density' ':' NUMBER ',' 'surfaceType' ':' STRING '}'
    ;

star
    : STAR NAME '{' 'spectralType' ':' SPECTRAL_TYPE ',' 'luminosity' ':' NUMBER ',' 'age' ':' NUMBER ',' 'mass' ':' NUMBER '}'
    ;

orbit
    : ORBIT '{' 'semiMajorAxis' ':' NUMBER ',' 'eccentricity' ':' NUMBER '}'
    ;
