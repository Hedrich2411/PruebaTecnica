# PruebaTecnica

## Nota

Odoo V16

No olvide agregar a los grupos de Stock Report User y Stock Picking Email User para poder visualizar la pregunta 1 y 5.

## Pregunta 1

Crear una funcionalidad que agregue un botón al formulario principal del modelo stock.picking, al hacer click en el botón, se debe abrir un wizard que solicite la siguiente información:

a) Una nota informativa para el destinatario, informando del envío de los productos.

b) Un campo para adjuntar algún archivo adicional, que solo admita archivos de tipo imagen y PDF.

El wizard tendrá un botón que, al activarlo, enviará un email al partner vinculado al picking principal, se deberán hacer las validaciones básicas en el proceso, en caso el email no esté definido o no cumpla con el formato de una dirección de correo estándar.

#### Solución

Boton para enviar las notas:

![Pregunta1_1!](/img/pregunta1_1.png)

Agregamos contenido:

![Pregunta1_2!](/img/pregunta1_2.png)

Mensaje enviado:

![Pregunta1_3!](/img/pregunta1_3.png)

Archivo adjunto enviado:

![Pregunta1_4!](/img/pregunta1_4.png)

Validaciones:

![Pregunta1_5!](/img/pregunta1_5.png)

![Pregunta1_6!](/img/pregunta1_6.png)

## Pregunta 2

Explicar el proceso de conciliación contable en Odoo, mencionar las tablas y modelos implicados al generar una conciliación y una explicación breve sobre en qué consiste la conciliación contable.

#### Solución

Las conciliaciones contables en odoo son necesarias para garantizar que los registros contables coincidan con las trasacciones reales.

Una conciliación contable es el proceso de verificación de los montos registrados de la contabilidad de una empresa coincidan con los montos reales en sus cuentas bancarias.

##### 1.-Proceso :

**Configuracion de Diarios**:

Se tiene que configurar los diarios contables para habilitar la conciliacion.

**Extractos Bancarios**:

Se importan o ingresan manualmente en Odoo. Esto se puede hacer a través de la conexión directa con bancos o subiendo archivos en formatos estándar como CSV, etc.

**Conciliación**:

Generado los extractos y con previa revisión, Odoo concilia automáticamente las transacciones bancarias con las facturas, recibos de pago y otros registros contables.

##### 2.-Tablas y Modelos :

**account.bank.statement**:
Representa los extractos bancarios y cada línea del extracto bancario (account.bank.statement.line) se concilia con una transacción en Odoo.

**account.move**:
Representa las facturas (anteriormente los asientos contables -> v < 13).

**account.payment**:
Representa los pagos realizados.

**account.account**: 
Para las cuentas contables en el plan de cuentas.


## Pregunta 3

Agregar un campo adicional con la etiqueta “Responsable” en el formulario del wizard de generación de Notas de crédito o facturas rectificativas (botón disponible desde el formulario de facturas de proveedor o cliente), el campo debe ser una many to one, relacionado a el modelo de usuarios, asimismo, el mismo campo debe ser creado también en el modelo account.move. Una vez que el wizard ejecute su acción y genere una nota de crédito, el campo de responsable debe viajar desde el wizard a la nota de crédito generada.

#### Solución

Campo para ingresar el usuario:

![Pregunta3_1!](/img/pregunta3_1.png)

Factura rectificativa con el usuario ingresado:

![Pregunta3_2!](/img/pregunta3_2.png)

## Pregunta 4

Crear un campo computado de tipo Many2many (invoice_due_ids) en el modelo res.partner, este campo debe contener todas las facturas de cliente vencidas que estén vinculadas al partner en cuestión, considerar una factura vencida como una factura publicada/validada cuya fecha de vencimiento sea menor a la fecha actual, asimismo, agregar un botón en el formulario de partner (puede ser un smart-button, action, o botón de encabezado) que al presionarlo, nos redirija a una vista de tipo lista, mostrando las facturas vencidas que contenga el campo invoice_due_ids.

#### Solución

Cantidad de facturas vencidas:

![Pregunta4_1!](/img/pregunta4_1.png)

Vista con las facturas vencidas:

![Pregunta4_2!](/img/pregunta4_2.png)

## Pregunta 5

Crear un reporte en pantalla, usando un modelo con el atributo _auto = False, el reporte debe estar disponible en una vista de tipo lista y también una de tipo pivot, el reporte debe ser un consolidado de los saldos de stock físico disponible por cada almacén, deben contener como mínimo los campos de: Almacén/ubicación, producto, categoría de producto, unidad de medida, stock físico.

#### Solución

Reporte en el menú:

![Pregunta5_1!](/img/pregunta5_1.png)

Vista tree:

![Pregunta5_2!](/img/pregunta5_2.png)

Vista pivot:

![Pregunta5_3!](/img/pregunta5_3.png)


## Odoo v16
