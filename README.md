# Ejercicios diapositivas

Yo trabaje en esto ejercicios de una manera conjunta donde se encuentren todos en el mismo archivo en el cual accedemos a cada ejercicio mediante una estructura de if que funciona como un menu. Como se muestra en la siguiente imagen:

![imagen uno](https://github.com/user-attachments/assets/2fd17e81-8394-47f2-893c-e21c5379ab55)


Este "menu" funciona mediante una entrada de un número del 1-7 perteneciedo cada uno de estos a un ejercicio en especifico y ademas si introduzco un valor distinto a este conjunto me saldrá que la opción no es valida.

## Ejercicio volumen sólidos.

Establezca el modelo matemático (función matemática) que permita calcular el volumen del sólido mostrado a continuación.


![imagen dos](https://github.com/user-attachments/assets/b249ac31-26fb-48ce-a7f1-e8d6dea2c917)


Lo primero que debes saber es que para acceder a este ejercicio en el menu debemos introducir el valor 1, ya definido esto pasamos a la definición de las tres funciones utilizadas, una para el cubo del radio, otra para el cuadrado del otro radio y por ultimo una para calcuar el voumen del solido (cabe resaltar que las funciones de cubo y cuadrado seran utilizadas mas adelante)


![imagen tres](https://github.com/user-attachments/assets/6e65d579-9fca-409a-b019-a6762cfea3b2)


Con este planteamiento comprobamos que funciona mediante la siguiente demostración:


![Ejemplo uno](https://github.com/user-attachments/assets/1914c1d3-2311-4839-9689-ecb13d164ca5)

## Ejercicio area figura 1

Como es de suponerse el valor asigando en el menu para este ejercicio es el 2, pasando al planteamiento de este ejercicio nos piden hallar el area superficial del vagón representado en la siguiente figura:

![figura cuatro](https://github.com/user-attachments/assets/f1d16d4c-68cf-458c-8887-7991de9e5faa)

Para resolver este ejercicio reutilizamos la funcion del cuadrado para añadirle la operación del area del rectángulo de la siguiente manera:

![Codigo eje2](https://github.com/user-attachments/assets/e74ccc02-03b6-41dc-8ee0-07261f0730c8)

Demostramos que el código funciona mediante la siguiente imagen:

![Ejemplo dos](https://github.com/user-attachments/assets/b3512941-0fdb-4920-8367-83e8457196a4)

## Ejercicio area figura 2

Para este ejercicio el valor asignado en el menu es el 3, centrandonos en el ejercicio nos pide hallar el area superficial de la parte lateral de un carro mediante un codigo en python, la figura se muestra a continuación:

![imagen cinco](https://github.com/user-attachments/assets/69a1f1e3-2a55-45d1-96bb-fdbe30b55aa8)

Para este ejercicio utilice la función del area_figura1, pero renombrada ya que para este ejercicio solo necesito la parte matemática (con una ligera modificación al momento de hallar el aera total) de esta misma, area_figura0 es la función renombrada para cumplir el objetivo la utilice dos veces atando una rueda a un rectángulo sin importar cuales sean ya que al momento de hallar el area total esto facilita mucho el proceso.

![codigo eje3](https://github.com/user-attachments/assets/8d649a08-dff2-4ef9-91cd-68dc29a7a133)

Para comprobar todo lo dicho y mostrado en e código esta la ejecución del mismo:

![Ejemplo tres](https://github.com/user-attachments/assets/7352d1c5-d630-45c6-be4f-3dbe13f9a3a8)

## Ejecicio 4

"Diseñe una funci+on que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente."

Para completar este ejercicio solo necesite de una función que me pida la cantidad de gallinas. gallos y pollitos y leugo con una operación matemática simple hallo la cantidad de kilos de carne de aves que hay. (cabe aclarar que el valor asignado en el menu de este ejercicio es 4)

![Codigo eje4](https://github.com/user-attachments/assets/8d31909e-3c44-4d04-9ccb-fbf3e7ab89d9)

Se le adjunta su debida ejecución para verificar su corrector funcinamiento:

![Ejemplo cuatro](https://github.com/user-attachments/assets/eddb9fd9-128e-4dbf-849d-7d2ed081966f)

## Ejercicio 5

"Mi mamá me manda a comprar P panes a $ 300 cada uno, M bolsas de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos".

Para este ejercicio repliclamo un poco lo de ejercicio anterior, pero a la función le agrego una codición para saber cuanto tenemos que dar de vueltos. si es que tenemos que hacerlo, cuanto le hace falta para competar el pago o si simplemente entrego el mismo valor a pagar. Este condicional lo conocemos como if, que no es muy útil desde el incio de código.

![Codigo eje 5](https://github.com/user-attachments/assets/8dd0d2db-90eb-49b6-8cee-41d5ce099824)

Para asegurarnos que funciona te enseñare todos los posibles casos:

###### Caso donde nos dan vueltos:

![caso 1](https://github.com/user-attachments/assets/e65a4792-46e6-43d1-8df2-5b0b640542ea)

###### Caso donde nos hace falta dinero: 

![caso 2](https://github.com/user-attachments/assets/c414e5f6-273e-4faf-9c7c-c1931ae1a56d)

###### Caso donde pagamos lo suficiente: 

![caso 3](https://github.com/user-attachments/assets/4b376012-8a01-46fb-9633-51788e9f7353)

## Ejercicio 6

"Si pido prestados P cantidad de pesos para pagarlos en dos meses, si el inter ́es del préstamo es del 3%. ¿Cu ́anto se debe pagar al final del segundo mes si el inter ́es es compuesto mensualmente?".

Para este ejercicio utilizo una función con dos variables una que es el dinero que pedí prestado y la segunda es para saber la cantidad de meses que tuve el dinero y me cobraron intereses (yo quise un poco más alla por esta razón le agregue esto).

![codigo eje6](https://github.com/user-attachments/assets/f4a857c8-a2de-44fd-b782-8f2bd277925b)

Comprobamos con la ejecución:

![ejemplo seis](https://github.com/user-attachments/assets/9cbefc82-d02f-42e4-ba69-893b131ca14c)

## Ejercicio 7
"El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C".

Para este ejercicio lo único nuevo que agregamos que no hallamos visto a lo largo de los ejercicios es la condición while que funciona como un ciclo el cual utilizamos para hacer la operación de la potenciación al cuadrado de los casos diarios, lo entenderemos mejor viendo e código:

![codigo eje7](https://github.com/user-attachments/assets/1810d5f7-5967-469b-97fd-acfd3a3a3ff6)

Comprobamos con a ejecución:

![ejemplo siete](https://github.com/user-attachments/assets/07872c6a-01b5-49ec-b86e-de8ab52a723e)

## Dato importante

Como mencione al inicio si al inicio en el menu introduzco un número distinto a conjunto 1-7 me arrojara la siguiente respuesta:

![ultima](https://github.com/user-attachments/assets/343601fb-4af0-47b0-b772-103fd8a26251)

### Bibliografia de los ejercicios:

Gómez Perdomo, J., Rodríguez, A., Cubides, C., & Sierra, C. A. (n.d.). Funciones de uno o varios parámetros. Universidad Nacional de Colombia.




  











