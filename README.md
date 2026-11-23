# Actividad2-ComparaSolucionesAnaliticasYNumericas
Un programa sencillo en Python que compara dos formas de predecir cómo crece un fenómeno en el tiempo usando una fórmula matemática exacta frente a una aproximación paso a paso usando el método de Euler.


Este proyecto demuestra la diferencia practica, en codigo, entre resolver un problema matematic de forma exacta y hacerlo mediante aproximaciones numericas por computadora.

Para lograrlo, se toma como ejemplo el problema clasico de crecimiento acelerado (como el aumento de una poblacion de bacterias o el interes compuesto) partiendo desde un valor inicial conocido.

A traves de un script dde Python, el programa evalua el comportamiento del problema durante un intervalo de tiempo dividido en pequenos saltos. En cada paso calcula el resultado usando el metodo de Euler, que estima el futuro basandose unicamente en la inclinacion o velocidad actual del cambio. Y lo compara lado a lado contra el valore real obtenido mediante el metodo de separacion de variables.

Finalmente, muestra en pantalla la diferencia o margen de error entre ambos resultados, permitiendo visualizar como las aproximaciones van acumulando pequenas desviaciones conforme avanza el tiempo.


## En que consiste el problema?

El problema consiste en que tienes un cultivo que empieza con una unidad y conociendo que su velocidad de crecimiento siempre es el doble de su tamano actual. El objetivo es descubrir cuanto habra crecido al llegar al segundo numero 1, revisando su avance en saltos pequenos de 0.2.


### El camino exacto (Separacion de variables)

Consiste en ordenar la ecuacion original agrupando los datos de tamano de un lado y los datos del tiempo del otro. Al resolver esta operacion matematica podemos saber el valor exacto en cualquier momento sin margen de fallo y sin tener que calcular los pasos anteriores.

### El camino aproximado (Metodo de Euler)

Consiste en caminar en linea recta siguiendo la direccion actual durante un paso corto (0.2), detenerse, volver a mirar hacia donde apunta la curva y dar el siguiente paso. 
Aunque es muy facil de programar, se va generando un pequeno error que crece poco a poco.