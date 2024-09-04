cd .\grammar\

java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 callisto.g4

cd ..

python .\TokenGenerator.py .\teste.cal