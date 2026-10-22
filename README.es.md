# 🦾 GrokBot 7 Agentes

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![GrokBot 7 Agentes](guia/assets/banner-es.jpg)](https://inematds.github.io/grokbot-7-agentes/guia/es/)

## Qué es

Es un kit con siete agentes listos para quienes usan GrokBot, el asistente de agentes de xAI. Cada agente viene en una ficha: un texto para pegar en GrokBot, lo que puede y no puede hacer por sí solo, tres pruebas para hacer antes de confiar y una rutina corta de seguimiento. Juntos, vigilan tu correo, verifican contratos, cuidan las redes, piden presupuestos, miran tus finanzas, guardan la memoria del equipo y coordinan todo. Para usarlo, basta con tener GrokBot y conectar las aplicaciones que indica cada ficha.

## 📖 Guía de uso

Guía completa (landing + paso a paso + instrucciones para copiar): **https://inematds.github.io/grokbot-7-agentes/guia/es/**

## Los 7 agentes

| # | Agente | Qué hace | Nivel | Cuándo corre |
|---|---|---|---|---|
| 1 | [🛡️ Escudo](agentes/es/01-escudo.md) | Rescata correo bueno del spam, señala estafas, encuentra tu teléfono en sitios de búsqueda de personas | N2 · prepara, tú apruebas | todos los días 7h |
| 2 | [🔍 Verificación](agentes/es/02-checagem.md) | Verifica a una persona/empresa en 4 lugares y lee la letra pequeña antes de que firmes | N1 · investiga y prepara | todos los días + a pedido |
| 3 | [📱 Redes](agentes/es/03-redes.md) | Tendencias en X, posts con tu voz, DM automático por palabra clave | N2 · prepara, tú apruebas | todas las mañanas + a pedido |
| 4 | [💸 Negociador](agentes/es/04-negociador.md) | Pide 3+ presupuestos por correo propio, compara y regatea | N2 · prepara, tú apruebas | a pedido |
| 5 | [📊 Financiero](agentes/es/05-financeiro.md) | Encuentra suscripciones duplicadas, gastos innecesarios, dinero olvidado y el costo de cada bot | N0 · solo mira | todos los días, panel el lunes |
| 6 | [🧠 Cerebro](agentes/es/06-cerebro.md) | Memoria compartida del equipo en una base de datos; los demás solo agregan informes, él organiza | N3 · ejecuta | a pedido |
| 7 | [🤝 Jefe de Gabinete](agentes/es/07-chefe-de-gabinete.md) | Coordina a los demás y te entrega el resumen de las 8h | N3 · ejecuta | todos los días 8h |

Cada ficha sigue el formato **Ficha del Agente** de INEMA ([7 principios](https://inematds.github.io/7pa/)): misión, contexto, datos, criterio de éxito, autonomía, observación y supervisión, más la **instrucción lista** para pegar, **3 pruebas** y el **checklist de supervisión**.

## El proceso, de principio a fin

Quién hace qué: 🧑 tú · ⚙️ GrokBot solo, en el horario · 🤖 el agente, cuando tú lo pides.

1. 🧑 **Elige el trabajo que más le quita tiempo a tu semana** (correo, contratos, redes, presupuestos o gastos) y abre su ficha en `agentes/es/`.
2. 🧑 **Copia la "Instrucción lista"** de la ficha (o con el botón copiar en la [guía](https://inematds.github.io/grokbot-7-agentes/guia/es/#agentes)).
3. 🧑 **Pégala en una conversación nueva en GrokBot** y cambia lo que está entre `[corchetes]` por tus datos. GrokBot confirma en 3 líneas lo que entendió.
4. 🧑 **Conecta las aplicaciones** que pide la ficha (`"Quiero conectar con [servicio]. ¿Qué necesitas?"`). La clave de API va en el campo seguro de GrokBot.
5. 🧑 **Ejecuta las 3 pruebas** de la ficha (información faltante, pedido prohibido, alarma). ¿Falló? Ajusta la regla y prueba de nuevo.
6. ⚙️ **El agente corre en el horario** de la ficha (Escudo 7h, Jefe 8h, Financiero con panel el lunes) y 🤖 a pedido.
7. 🧑 **2 minutos por día:** lee el informe y aprueba lo que espera tu OK. **10 minutos por semana:** ajusta una sola regla (en la conversación del bot: *"Cambia una regla: ..."*) y anota lo que falló en una planilla tuya, copiando la tabla "Registro de fallas" de la ficha.
8. 🧑 **Repite desde el paso 1** con el siguiente agente, una semana después.
9. 🧑 **Con 2+ agentes corriendo, monta el Cerebro** (una base de datos que se vuelve la memoria común) y **conecta la misma base en cada bot**: las instrucciones ya mandan a cada uno a guardar allí su propio informe. Después monta **el Jefe de Gabinete**, que lee esos informes y te resume a las 8h.
10. 🧑 **Cada mes:** revisa si el nivel de cada agente sigue siendo el correcto; sube solo cuando la ficha diga que se puede.

## Regla de los 3 motivos

Crea un bot separado solo si necesita **memoria propia**, **permiso diferente** o **reloj propio**. De lo contrario, pídeselo directamente al Jefe de Gabinete. Seis bots son seis conversaciones que seguir.

## Avisos

- Las fichas fueron escritas por INEMA a partir de una [clase pública sobre agentes en GrokBot](https://www.youtube.com/watch?v=2Vscrsz89MY) (en inglés), la "clase de referencia" citada en las fichas. No son los textos originales de la clase.
- No las probamos en todas las cuentas y planes de GrokBot: **ejecuta las 3 pruebas en el tuyo antes de confiar**.
- Las herramientas citadas en las fichas (programador de posts, billetera, base de datos) son ejemplos, no exigencia. Ninguna tiene vínculo con INEMA.
- Todo lo que toca dinero o habla con gente de afuera empieza en el nivel N2: **nada sale sin tu OK**.

## Para quien mantiene el kit

Las instrucciones de la página salen de las fichas. ¿Editaste una ficha (PT en `agentes/`, EN en `agentes/en/`, ES en `agentes/es/`) o la página (`guia/_src/<idioma>.html`)? Ejecuta:

```bash
python3 guia/build.py   # genera guia/index.html, guia/en/ y guia/es/
```

---

Kit abierto y gratuito · [INEMA.CLUB](https://inema.club)
