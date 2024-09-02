grammar callisto;

prog:   (statement)* ;

statement
    : expr ';'           # printStatement
    | 'fn' ID '(' params? ')' 'do' statement* 'end'  # functionDeclaration
    | ID '=' expr ';'   # variableDeclaration
    | expr ';'          # expressionStatement
    ;

params: ID (',' ID)* ;

expr
    : expr '+' expr      # addExpr
    | expr '-' expr      # subExpr
    | expr '*' expr      # mulExpr
    | expr '/' expr      # divExpr
    | NUMBER             # numberExpr
    | STRING             # stringExpr
    | ID                 # variableExpr
    | '(' expr ')'       # parensExpr
    | ID '(' (expr (',' expr)*)? ')' # functionCallExpr
    | '[' (expr (',' expr)*)? ']'  # arrayExpr
    | '{' (ID ':' expr (',' ID ':' expr)*)? '}'  # dictExpr
    ;

NUMBER: [0-9]+ ;
STRING: '"' [a-zA-Z0-9 ]* '"' ;
ID: [a-zA-Z_] [a-zA-Z_0-9]* ;
WS: [ \t\r\n]+ -> skip ;
