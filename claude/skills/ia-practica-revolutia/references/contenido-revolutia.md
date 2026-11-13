# Cómo hace los reels @revolutia.ai y qué copiar

Datos de 217 reels (172 guiones distintos), del 14-ene al 14-sep-2026. Instagram no expone las reproducciones, así que todo va en **likes**: indican lo que gustó, no cuánto se vio. Lo de abajo es correlación en una sola cuenta, grado C. Sirve para formular hipótesis y probarlas en nuestras cuentas, no para citarlo como prueba ante un cliente.

## Las cifras

- Publica 1,7 reels al día en los días que publica (128 días con al menos uno).
- Duración: mediana de 58 s (la mitad entre 50 y 75 s). Unas 190 palabras por guion, a ritmo rápido.
- Likes por guion: mediana de 366; el 10 % mejor pasa de 3.970. El máximo es 81.480 («Google acaba de lanzar silenciosamente 7 herramientas de IA 100 % gratuitas»).
- 17 guiones son cortes del podcast, con «link en bio al episodio completo».

## La fórmula del gancho

Abre con una novedad de una marca que todo el mundo conoce y un beneficio gratis:

- «[Google / Anthropic / NVIDIA / Microsoft] acaba de lanzar [X]». Aparece en 44 de los 172 guiones. Mediana de 1.088 likes, el triple que el conjunto.
- «Gratis», «100 % gratuito», «cero euros»: 23 ganchos.
- Un villano o una víctima: «deja en ridículo a las agencias que cobran 3.000 €», «acaba de matar a muchas empresas», «tu plan de 20 € se funde en dos días».
- Un personaje famoso metido con calzador: «Elon acaba de recibir una llamada…» (24.442 likes).
- Experimento propio con resultado y plazo: «Le pedí a Claude que reescribiera mi currículum y conseguí entrevistas en 24 horas» (8.369).

Después el cuerpo va siempre igual: qué es, por qué importa (problema que resuelve con una cifra), 2-4 pasos de uso enseñados en pantalla y el CTA.

## El CTA: comenta una palabra

106 de los 172 guiones cierran con «comenta [PALABRA] y te envío…». La palabra cambia por reel (NVIDIA, TURBO, REPO, CURRÍCULUM, IA) y lo que manda es la guía, el enlace o el prompt exacto, a veces con la invitación a un evento gratuito o a la comunidad. Es un ManyChat por palabra clave: cada comentario es un lead que entra por DM, y además el comentario empuja el alcance.

## Republicar los ganadores

20 guiones los publicó varias veces, hasta 7 cada uno. Republica solo lo que ya funcionó: la mediana del mejor intento de esos 20 es 2.530 likes, frente a 334 de los que solo publicó una vez. La primera versión fue la mejor en 16 de los 20. Aun así, la sexta publicación del guion de los PDF dio 13.776 likes cuando las anteriores no llegaban a 6.000, y la segunda del de MoneyPrinter subió de 8.763 a 12.017. Republicar cuesta cero y de vez en cuando vuelve a explotar.

## Qué copiar para ECSSTUDIO (con ojo)

1. **Republicar ganadores** (sí, ya). Los reels de Diego y de clientes que pasen del percentil 90 de su cuenta se vuelven a subir a las 3-6 semanas, con otro gancho en pantalla y el mismo cuerpo. Cuadra con la nota de memoria feedback-duplicar-con-prueba-social. Mide por reproducciones y envíos, no por likes.
2. **CTA de palabra clave en todos los reels con algo que entregar.** Ya existe en stories («comenta CONTRATO»). Pasarlo a reels con un recurso concreto por pieza y un flujo de ManyChat o del IA Setter por palabra.
3. **Gancho de novedad con marca conocida**, pero solo para contenido de herramientas (Custom Soft Lab, la parte de IA de ECS). Para vender Sprint 360 a pymes no encaja: el ICP no compra porque Google haya lanzado algo, compra por dinero que entra. Ahí sirve más su fórmula de experimento propio con resultado y plazo, con un caso real de cliente.
4. **No copiar** la exageración («deja en ridículo», «máquina de imprimir dinero», cifras redondas sin fuente). Para una agencia que vende un bien de confianza, una promesa inflada resta más de lo que suma (`kb-mercado/10`). Y las cifras de sus guiones no van a propuestas ni guiones sin fuente primaria.

Los ganchos tal cual están en `~/Claude/docs/revolutia/analisis/contenido.json` (solo en el Mac de Diego). Para escribir uno nuevo se traducen con `anti-patrones-ia-redaccion.md` y `voz-diego-marca.md`, igual que los del banco de hooks.
