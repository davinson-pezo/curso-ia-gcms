# Notas del Orador — Curso IA GC-MS

> Notas para el presentador. **No** se proyecta — son indicaciones para el speaker.
> Tiempos en minutos desde el inicio de cada bloque.

## Bloque 0 — Apertura (10 min)

**Slide 1 (Portada):** 0:00 — 0:30
- Saluda con energía. "Buenos días/tardes, bienvenidos al curso..."
- NO leas el título. Haz una pregunta al aire: "¿Quién ha usado ChatGPT? ¿Y Antigravity?"
- El objetivo es interacción, no monólogo.

**Slide 2 (Qué vais a saber):** 0:30 — 3:00
- Estos 4 outcomes son el **contrato con la audiencia**.
- Enfatiza: "Nada de marketing. Honestidad ante todo."
- Si alguien tiene prisa, este es el bloque donde decidir quedarse o no.

**Slide 3 (Agenda):** 3:00 — 5:00
- Lee los bloques sin entrar en detalle.
- Pide feedback al final: "¿Algún bloque que queráis que profundicemos más?"
- Pista: el bloque 9 (embriones) es el corazón — 90 min, 1/3 del tiempo total.

**Slide 4 (Por qué IA en ciencia):** 5:00 — 7:30
- El mensaje clave: **la IA no reemplaza al científico, lo augmenta**.
- "Si no entendéis el resultado, no lo presentéis." ← regla de oro.

**Slide 5 (Panorama 2026):** 7:30 — 9:00
- Menciona hitos sin profundizar. La cronología es para contexto.
- "Hace 6 meses esto no existía. Hace 18 meses, ni idea."

**Slide 6 (4 capas del stack):** 9:00 — 11:00
- Analogía: "Como una cebolla. Si falla algo, sabéis dónde."
- **"Los datos son tuyos, los modelos son intercambiables"** ← repetidlo.

**Slide 7 (Qué NO es la IA):** 11:00 — 14:00
- Esta slide es **la más importante del bloque 1**. El alumno debe salir sabiendo los límites.
- "Las IAs alucinan. Si no verificas DOIs, mientes a tus pares."

**Slide 8 (El caso real):** 14:00 — 20:00
- Ahora el contexto del bloque 9: 90 min sobre embriones.
- "No es un ejemplo de juguete. Es un proyecto real con datos crudos."
- Título del informe: "DQ-TR-2026-002" — es real.

---

## Bloque 2 — Antigravity (25 min)

**Slide 9 (Qué es):** 25:00 — 28:00
- "Google Antigravity es un **ecosistema de 4 productos** sobre el mismo motor de IA."
- Lanzado nov-2025, 2.0 en mayo 2026.

**Slide 10 (Historia):** 28:00 — 32:00
- Cronología visual. Pasa rápido.
- Enfatiza: "Gemini 3 → 3.5 Flash en 6 meses. El ritmo es brutal."

**Slide 11 (Las 3 superficies):** 32:00 — 36:00
- "Editor: tu taller. Manager: tu oficina. Browser: los ojos del agente en internet."

**Slide 12 (Artifacts):** 36:00 — 39:00
- "Si no puedo ver qué hizo el agente, no confío en él."
- Importante para ciencia: trazabilidad = rigor.

**Slide 13 (Modelos):** 39:00 — 42:00
- 3.5 Flash por defecto, Claude 4.6 para profundidad, GPT-OSS para reproducibilidad.
- "Multi-modelo en paralelo" es lo poderoso.

**Slide 14 (1 motor, 4 puertas):** 42:00 — 45:00
- Diagrama central de la charla. Repite el mensaje.
- "¿Preguntas hasta aquí?"

---

## Bloque 3 — Diferenciar 2.0 vs IDE vs CLI (15 min)

(Por generar — placeholder de notas)

- La regla: **2.0 para investigación, IDE para programar, CLI para batch, SDK para custom**.
- Cuando use el IDE: coding iterativo. Cuando use CLI: pipelines largos, batch, servidores.
- Demo en vivo del CLI: `antigravity run "analyze embryo CDF data"`.

---

## Bloque 4 — Antigravity 2.0 + Science Skills (20 min)

(Por generar — placeholder)

- Novedades I/O 2026: Gemini 3.5 Flash, Science Skills, 4 nuevos productos Gemini for Science.
- **Demo en vivo de AlphaFold** ← momento clave de la clase. Reservar 5 min.
- Caso AK2: ejemplo de Google. Mutación rara, antes semanas, ahora minutos.

---

## Bloque 5 — Prompts (25 min)

(Por generar — placeholder)

- 4 patrones: zero-shot, few-shot, chain-of-thought, decomposition.
- **Prompts para ciencia** ≠ prompts para chat. Estructura: rol, contexto, objetivo, formato.
- Ejercicios prácticos: 10 min hands-on.

---

## Bloque 6 — MCP (20 min)

(Por generar — placeholder)

- "MCP es el USB-C de los LLMs."
- Demo: instalar EcoLab RAG como MCP server.
- Caso de uso real: ClayOMics, EcoLab RAG, Zotero.

---

## Bloque 7-8 — NotebookLM + combo (20 min)

(Por generar — placeholder)

- NotebookLM = "bibliotecario". Antigravity = "analista".
- Cuándo usar cada uno. Cuándo combinar.
- Demo: subir 5 papers de VOC, pedir resumen estructurado, luego Antigravity ejecuta el experimento inspirado en el gap.

---

## Bloque 9 — CASO EMBRIONES (90 min) ⭐

**Esta es la pieza central de la clase. No escatimes tiempo.**

### Estructura interna:

- 9.1-9.3 Portada + objetivo biológico + datos (15 min)
  - Slide 1: "COVs como biomarcadores no invasivos..."
  - Slide 2: Problema económico de la infertilidad bovina
  - Slide 3: HS-SPME-GC-MS como técnica

- 9.4-9.7 Pipeline (20 min)
  - Slide 4: Diagrama del pipeline
  - Slide 5: ASLS baseline correction
  - Slide 6: Peak detection
  - Slide 7: Alignment + filtrado

- 9.8-9.11 EDA + Estadística (25 min)
  - Slide 8: TIC overlay por grupos
  - Slide 9: EIC m/z 49 — el hallazgo clave
  - Slide 10: EIC m/z 84 — confirmación
  - Slide 11: PLS-DA score plot

- 9.12-9.14 Biomarcadores (15 min)
  - Slide 12: VIP scores, top 10
  - Slide 13: m/z 49 y 84 validados
  - Slide 14: Identificación NIST tentativa

- 9.15-9.16 Conclusiones + honestidad (15 min)
  - Slide 15: 10 hallazgos, con caveat
  - Slide 16: Limitaciones explícitas (n, variabilidad, R² negativo)

### Notas críticas:

- **Sé honesto sobre el R² negativo.** Es parte del aprendizaje, no un fracaso.
- **Pausa y pregunta** cada 3-4 slides: "¿Alguien ha tenido R² negativo en su análisis?"
- **Muestra scripts reales**, no slides bonitas. Los alumnos necesitan ver el código.
- **Si falla una demo**, ten el PDF de backup. No improvises.

---

## Bloque 10-11 — Pipeline + Referencias + Informe (25 min)

(Por generar — placeholder)

- Estructura del pipeline de análisis (genérico).
- Cómo buscar bibliografía: PubMed, Crossref, NotebookLM, EcoLab RAG.
- IMRaD structure para el informe final.

---

## Bloque 12 — Cierre (15 min)

(Por generar — placeholder)

- Recap de 4 outcomes.
- Recursos: este repo, slides, datos sintéticos, guión.
- Contacto: info@dataquorum.net
- Q&A

---

## 🎯 Tips generales para el orador

- **Habla con la audiencia, no leas.** Las slides son tu apoyo, no tu guion.
- **Pide feedback** cada 2-3 bloques. "¿Vamos bien? ¿Demasiado rápido?"
- **Si alguien pregunta y no sabes, dilo.** "Buena pregunta, no lo sé, lo investigo y os lo mando."
- **Lleva agua.** 4 horas hablando es agotador.
- **Respeta los tiempos.** Si un bloque se alarga, recorta el bloque 10-11 (el menos importante).
- **Ten el guión de alumnos abierto** por si alguien pregunta detalles.
