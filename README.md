***repositorio para la entrega del segundo proyecto de automatas:***

*IMPORTANTE, LEER EL ENUNCIADO PARA COMPRENDER BIEN LO REQUERIMIENTOS*

**automata.py:**

-clase para definir un automata, tiene estados, alfabeto, y transiciones, sus estados de termino y su estado de partida

  atributos:
    estados: lista con sus estados, pueden ser "q1", "q2", "A", "B", etc...
    alfabeto: lista con los characteres aceptados para ser transicion, por ejemplo, "0", "1", "a", "b", etc
    trancisiones: lista con tuplas asociadas a las transiciones del automata, las tuplas tienen el formato (ESTADO1, CHARACTER_DE_TRANSICION, ESTADO2) ej. ("A", "0", "B") SIGNIFICA LA SGTE TRANSICION: A 0 -> B

  metodos:
    print_self: printea en consola todos los atributos de la instancia del automata.


**read_from_file.py**

-script con la funcion para leer los archivos de ejemplos de input, esta funcion retorna un automata con los estados dados por el archivo'


**NFA-DFA** 

-archivo con el algoritmo para pasar de un NFA a un DFA, (todavia no implementado)

...

