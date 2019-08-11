# Representación de Modelado

Los modelos de características, en adición de ser una herramienta visual para facilitar el entendimiento de una línea de productos, son un problema matemático. Un modelo de características tiene un conjunto de fórmulas matemáticas o booleanas que nos permiten analizar su correctitud, tanto a la hora de construcción del modelo, como al momento de configurarlo y crear productos a partir de este. Para expresar un modelo de características en su fórmula matemática se substituye sus restricciones por sus equivalentes en forma de ecuación. La siguiente tabla muestra la equivalencia que existe entre cada restricción y su representación matemática correspondiente.

<!-- Mirar como representar bien la cardinalidad en CNF -->
| Restricción  | Representación Booleana       | Representación Aritmética       |
| -            | -                             | -                               |
| Raíz         | $característica = verdadero$  | $característica = 1$            |
| Obligatoria  | $padre \Leftrightarrow hija$  | $padre = hija$                  |
| Opcional     | $padre \Rightarrow hija$      | $padre \leq hija$               |
| Requerida    | $origen \Rightarrow destino$  | $(1 - origen) + destino \geq 0$ |
| Exclusión    | $\sim(origen \wedge destino)$ | $origen \times destino = 0$     |
| Cardinalidad | $(c_1) or (c_1 and c_2) or ... or (c_1 and c_2 ... and c_n)$ | $cota\_inf * padre \leq \sum_{k}^{i=1} C_i \leq cota\_sup * padre$ |

Encontrar solución a este conjunto de ecuaciones matemáticas no es tarea sencilla, este tipo de problemas son conocidos como problemas de satisfacibilidad booleana cuando se utilizan las fórmulas en lógica proposicional, o problemas de satisfacibilidad de restricciones cuando se utilizan las fórmulas aritméticas, ambos de estos problemas se encuentran en el conjunto de NP-completo, haciéndolos del tipo de tareas más difíciles computacionalmente. Es por esta razón que un lenguaje de programación convencional no es la herramienta adecuada para solucionar el problema, en estos casos utilizamos herramientas llamadas "solvers" estos son softwares matemáticos que se encargan de encontrar soluciones a problemas matemáticos.

Existen múltiples formatos que los solvers entienden, en esta sección explicaremos las representaciones CNF que permite utilizar solvers de tipo satisfacibilidad booleana (o SAT por sus siglas en inglés), XCSP y MiniZinc que permiten expresar como un problema de satisfacción de restricciones (o CSP por sus siglas en inglés). Cada una de estas representaciones permite interactuar con una gama de solvers diferentes que también exploramos en los siguientes numerales.


## CNF
En lógica booleana, una fórmula está en forma normal conjuntiva (CNF de su nombre en inglés) si corresponde a una conjunción de cláusulas, donde una cláusula es una disyunción de literales (variables booleanas), y donde un literal y su complemento no pueden aparecer en la misma cláusula. Los únicos conectivos lógicos que pueden aparecer en una fórmula en CNF son la conjunción, disyunción y negación. El operador negación sólo puede aplicarse a un literal, y no a una cláusula completa, lo que significa que este sólo puede preceder a una variable proposicional o un símbolo de predicado.

Segùn esta definiciòn, las siguientes fórmulas están en CNF:

> **NOT** A **AND** (B **OR** C)

> (A **OR** B) **AND** (**NOT** B **OR** C **OR** **NOT** D) **AND** (D **AND** **NOT** E)

> A **AND** B

Las siguientes fórmulas no están en CNF:

>  **NOT** (A **OR** C)

> (**A** **AND** B) **OR** C

> A **AND** (B **OR** (D **AND** E))

Toda fórmula booleana puede ser el equivalente escrita en forma normal conjuntiva. En particular, este es el caso para los tres contraejemplos recién mencionados; que son, respectivamente, equivalentes a las siguientes tres fórmulas normales conjuntivas:

> **NOT** B **OR** **NOT** C

> (A **OR** C) **AND** (B **OR** C)

> A **AND** (B **OR** D) **AND** (B **OR** E)

Usualmente estas fórmulas se escriben en un archivo de texto plano para representar un problema de satisfacción de restricciones booleanas entre un conjunto de literales. Resolver un problema booleano consiste en encontrar un conjunto de valores que al ser asignados a los literales del problema hacen que cada una de las cláusulas del problema sea verdadera. Como el problema de satisfacciòn de relaciones booleanas es la conjunción de todas las cláusulas que conforman el problema, esto equivale a decir que resolver el problema consiste en encontrar un conjunto de valores que al ser asignados a los literales del problema hacen que la clàusula resultante sea verdadera.

CNF es un formato ASCII para representar estos problemas de SATisfacciòn (SAT) de restricciones o fòrmulas booleanas. La estructura de uno de estos archivos puede ser descrita de la siguiente forma:

1. El archivo puede comenzar con líneas de comentario. El primer carácter de cada comentario debe ser una letra “c” minúscula. Generalmente estos comentarios aparecen en una única sección en el encabezado del archivo, pero estos comentarios pueden estar en cualquier parte del archivo en realidad.

2. El archivo puede comenzar con líneas de comentario. El primer carácter de cada comentario debe ser una letra “c” minúscula. Generalmente estos comentarios aparecen en una única sección en el encabezado del archivo, pero estos comentarios pueden estar en cualquier parte del archivo en realidad.

3. El resto del archivo son enunciados o clàusulas; cada uno debe estar en una línea diferente del archivo.

4. Un literal se define por un número positivo que va desde 1 hasta N, donde N es el número de literales que tiene el problema, y la representación negativa de cada de uno de estos literales se hace con un “-” y representa la negación del literal. 

5. Cada enunciado o cláusula debe ser finalizado con un 0.

Por ejemplo, el archivo CNF correspondiente a nuestras primeras tres fòrmulas en CNF vistas previamente es el siguiente:

>c ejemplo de CNF correspondiente a las siguientes fòrmulas
>
>c NOT A AND (B OR C)}
>
>c (A OR B) AND (NOT B OR C OR NOT D) AND (D AND NOT E)
>
>c A AND B
>
>p cnf 5 3 
>
>1 -3  0 
>
>2  3 -1 0

En este caso "c ejemplo de CNF" y las lineas que empizan con "c" son comentarios, "p cnf 5 3" es la descripción del problema compuesto por 3 fórmulas y 5 literales, "1  -3  0" y "2  3 -1  0" son enunciados, en estos ultimos, los espacios representan una disyunción, el 0 seguido de un salto de línea significa una conjunción y el signo negativo representa una negación.

- **Opcional:**
- **Obligatoria:**
- **Cardinal Grupal:**
- **Requerida:**
- **Exclusión:**
- **Logicas:**

## XCSP
- **Opcional:**
- **Obligatoria:**
- **Cardinal Grupal:**
- **Requerida:**
- **Exclusión:**
- **Logicas:**

## MiniZinc
- **Opcional:**
- **Obligatoria:**
- **Cardinal Grupal:**
- **Requerida:**
- **Exclusión:**
- **Logicas:**

## GNUProlog
- **Opcional:**
- **Obligatoria:**
- **Cardinal Grupal:**
- **Requerida:**
- **Exclusión:**
- **Logicas:**
