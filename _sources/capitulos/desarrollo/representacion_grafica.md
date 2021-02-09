# Representación Gráfica

El manejo de la variabilidad de cientos de componentes y la posible derivación de miles de productos hace de las líneas de productos un problema complejo. Hemos podido aprender de la historia del desarrollo software y sistemas, que la abstracción de todas estas complejidades juega un papel fundamental para poder trabajar efectivamente en este tipo de problemas. La conceptualización de requisitos comunes y variables de una colección de productos y su organización en un modelo, puede ser una buena opción para gestionar la complejidad de la línea de productos. 

Los modelos de características (o por sus siglas en inglés FM) son una técnica gráfica popular de modelado de variabilidad, son una representación de todos los posibles productos que pueden ser derivados de una línea de productos de software en términos de sus características. Estos modelos son utilizados a lo largo del desarrollo de una línea de producto de software, sirviendo como insumo para otros procesos y funcionan para la generación de arquitecturas, documentos e incluso código. 

Los FM están compuestos por caracteristicas, definidas como los atributos que agregan valor a un cliente y distinguen un producto de sus competidores en el mercado. y se representan con una caja con el nombre de la característica en su interior. Y restricciones, que son las relaciones que existen entre productos, muestran las formas en las que estos se pueden asociar para generar un articulo de una linea de productos, estas se representan con flechas que salen de una característica y se dirigen a otra, con algunos signos espaciales que permiten clasificarla.

Los feature models pueden ser utilizados para derivar todo tipo de producto, en este documento presentaremos como ejemplo canónico un feature model para la derivación de teléfonos celulares. {cite}`TORO_2017`

<br/>

![FM](../../images/capitulos/desarrollo/FM-Cellphone.png)

<br/>

A pesar de las ventajas de la representación gráfica, estas no pueden ser analizadas directamente por un computador, tampoco son ideales para ser reutilizadas en otros proyectos o incluso otras herramientas de manejo de líneas de producto de software. La transformación de este tipo de modelos a representaciones más adecuada para estos trabajos será un tema que será explorado en los siguientes capítulos.


## FM en VariaMos

Existen diversos tipos de modelos de características, estos se diferencian dependiendo de las relaciones que se pueden hacer entre los atributos del modelo. En el caso de VariaMos se utilizan modelos basados en cardinalidad, estos permiten expresar con más exactitud casos en que los productos requieren cierta cantidad de componentes delimitada de forma numérica. Para el caso de VariaMos estos son los tipos de restricciones que soporta el modelo:

- **Raíz:** Esta es una relación implícita, esto quiere decir no existe una flecha que la denote. Esta restricción es especialmente importante, ya que indica desde donde inicia el modelo y siempre debe estar seleccionada, ya que si no lo está será imposible derivar productos, adicional en un modelo debe existir una y solo una raíz.

- **Opcional:** Es una relación entre una característica padre y una hija, hace referencia que cuando la característica padre pertenece a un producto, la característica hija puede o no hacer parte del mismo producto.

- **Obligatoria:** Es una relación jerárquica entre un padre y un hijo, quiere decir que cuando el padre hace parte de un producto entonces necesariamente la característica hija también tiene que hacer parte del producto.

- **Cardinal Grupal:** Esta relaciona un padre con múltiples hijos, adicional a las flechas que tradicionalmente vemos en otras restricciones, estas tienen una dupla de números, el primero representa la cantidad mínima de hijos que deben estar en el producto cuando el padre hace parte de él mismo, mientras que el segundo se refiere a la cantidad máxima de hijos seleccionados en el mismo escenario.

- **Requerida:** Es una relación entre dos características, una de origien y una de destino, estas no necesariamente deben tener la estructura jerárquica de padre he hija como en las restricciones anteriores, representa la necesidad de elegir la característica de destino cuando la de origen hace parte del producto a derivar.

- **Exclusión:** La exclusión también es una relación de origen y destino, esta expresa la imposibilidad de que tanto la característica de origen y la de destino hagan parte de un mismo producto.

- **Logicas:** Son restricciones que permiten utilizar operadores de lógica proposicional, como AND, OR, XOR. Estas se crean entre una característica padre y múltiples características hijas.

En VariaMos podemos construir modelos con un menú "drag and drop" que permite ubicar fácilmente características y crear las relaciones entre estas, se representa en VariaMos de la siguiente forma.


<!-- TODO: Añadir algo acerca de las características concretas y abstractas. -->

<br/>

![FM](../../images/capitulos/desarrollo/FM-Cellphone-VariaMos.png)

<br/>

Los modelos de características son construidos utilizando MXGraph, esta tecnología nos permite poder integrar fácilmente componentes gráficos a librerías modernas de desarrollo frontend como es Vue.js haciendo fácil diseñar una UX/UI adecuada para quienes deseen utilizar la herramienta. MXGraph utiliza XML para generar su representación interna, es esta la que nos permite poder armar, construir y mostrar los FM de forma exitosa. Es importante entender cómo se representan cada uno de los componentes del feature model en esta representación.

<!-- TODO: Agregar texto -->
- **Raíz:**

```xml
<root label="Mobile Phone" type="root" id="1">
  <mxCell style="strokeWidth=3" vertex="1" parent="feature">
    <mxGeometry x="195" width="100" height="35" as="geometry"/>
  </mxCell>
</root>
```

- **Característica Concreta:**

```xml
<concrete label="GPS" type="concrete" selected="false" id="7">
  <mxCell style="" vertex="1" parent="feature">
    <mxGeometry y="135" width="100" height="35" as="geometry"/>
  </mxCell>
</concrete>
```

- **Característica Abstracta:**

```xml
<abstract label="Screen" type="abstract" id="4">
  <mxCell style="strokeWidth=2" vertex="1" parent="feature">
    <mxGeometry x="260" y="135" width="100" height="35" as="geometry"/>
  </mxCell>
</abstract>
```

- **Bundle:**
```xml
<bundle label="bundle" type="bundle" bundleType="RANGE" lowRange="1" highRange="1" id="6">
  <mxCell style="shape=ellipse" vertex="1" parent="feature">
    <mxGeometry x="582.265625" width="35" height="35" as="geometry"/>
  </mxCell>
</bundle>
```

- **Relación Con Bundle:**
```xml
<rel_concrete_bundle type="relation" id="0.17">
  <mxCell style="noEdgeStyle=1;orthogonal=1;" edge="1" parent="feature" source="14" target="12">
    <mxGeometry relative="1" as="geometry">
      <Array as="points">
        <mxPoint x="1090" y="123"/>
        <mxPoint x="970.265625" y="47"/>
      </Array>
    </mxGeometry>
  </mxCell>
</rel_concrete_bundle>
```

- **Relación Opcional:**
```xml
<rel_concrete_root type="relation" relType="optional" id="0.7">
  <mxCell style="noEdgeStyle=1;orthogonal=1;" edge="1" parent="feature" source="7" target="1">
    <mxGeometry relative="1" as="geometry">
      <Array as="points">
        <mxPoint x="50" y="123"/>
        <mxPoint x="211.25" y="47"/>
      </Array>
    </mxGeometry>
  </mxCell>
</rel_concrete_root>
```

- **Relación Obligatoria:**
```xml
<rel_abstract_root type="relation" relType="mandatory" id="0.3">
  <mxCell style="noEdgeStyle=1;orthogonal=1;" edge="1" parent="feature" source="4" target="1">
    <mxGeometry relative="1" as="geometry">
      <Array as="points">
        <mxPoint x="287.5" y="123"/>
        <mxPoint x="256.25" y="49"/>
      </Array>
    </mxGeometry>
  </mxCell>
</rel_abstract_root>
```

<!-- TODO: Añadir requerida y excluye. -->

