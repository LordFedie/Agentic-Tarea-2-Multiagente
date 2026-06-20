# Agentic-Tarea-2-Multiagente

Asistente educativo personal implementado como sistema multiagente local con Python y Ollama. El sistema recibe consultas en lenguaje natural, las enruta a agentes especializados y muestra la traza de ejecucion en consola.

## Arquitectura

El proyecto incluye los siguientes agentes:

- `CoordinatorAgent`: analiza la consulta, detecta subtareas, decide el agente adecuado y consolida la respuesta.
- `CalculatorAgent`: resuelve calculos exactos usando herramientas matematicas locales.
- `OrganizerAgent`: administra eventos en un calendario persistente almacenado en `data/calendar.json`.
- `ExpertAgent`: responde preguntas conceptuales apoyandose en una busqueda web abierta.
- `CriticAgent`: valida la respuesta final de cada subtarea y puede forzar un reintento automatico.

## Tecnologias utilizadas

- Python
- Ollama como motor local del modelo
- Modelo por defecto: `gemma3:4b`
- Busqueda web con `ddgs`
- Persistencia local en JSON

## Requisitos previos

Antes de ejecutar el proyecto necesitas tener instalado:

1. Python 3.10 o superior
2. Ollama
3. El modelo `gemma3:4b` descargado en Ollama

## Instalacion

1. Clona o descarga este repositorio.
2. Entra a la carpeta del proyecto.
3. Crea y activa un entorno virtual.
4. Instala las dependencias.

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Linux o macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuracion de Ollama

Descarga el modelo configurado en [config.py](C:/Users/dsanm/OneDrive/Escritorio/Universidad/AgenticAI/Tarea2/Agentic-Tarea-2-Multiagente/config.py:1):

```bash
ollama pull gemma3:4b
```

Verifica que Ollama este instalado y funcionando:

```bash
ollama list
```

Si quieres usar otro modelo, cambia la constante `OLLAMA_MODEL` en [config.py](C:/Users/dsanm/OneDrive/Escritorio/Universidad/AgenticAI/Tarea2/Agentic-Tarea-2-Multiagente/config.py:1).

## Ejecucion

Ejecuta el programa principal:

```bash
python main.py
```

El sistema pedira una consulta por consola:

```text
Consulta: Calcula 25 x (4 + 6)
```

## Ejemplos de uso

### Calculador

```text
Consulta: Cual es el resultado de dividir 1024 entre 8?
Consulta: Calcula 25 x (4 + 6)
```

### Organizador

```text
Consulta: Agrega una reunion de estudio de Fisica el 10 de junio de 2026 a las 15:00 horas.
Consulta: Tengo algun evento programado para el 10 de junio de 2026?
```

### Experto

```text
Consulta: Que es la entropia en termodinamica?
Consulta: Explicame que es el ciclo de Krebs de forma sencilla.
```

### Consultas compuestas

```text
Consulta: Calcula 25 x (4 + 6) y agrega una reunion de estudio de Fisica el 10 de junio de 2026 a las 15:00 horas.
Consulta: Que es la entropia en termodinamica? Luego agrega un evento llamado Repasar Entropia el 12 de junio de 2026 a las 18:00.
```

## Estructura del proyecto

```text
agents/
  calculator.py
  coordinator.py
  critic.py
  expert.py
  organizer.py
  prompts/
tools/
  calendar_tools.py
  math_tools.py
  search_tools.py
utils/
  calculator_parser.py
  date_utils.py
  ollama_client.py
  organizer_parser.py
  query_decomposer.py
data/
  calendar.json
main.py
config.py
requirements.txt
```

## Persistencia

Los eventos se almacenan localmente en [data/calendar.json](C:/Users/dsanm/OneDrive/Escritorio/Universidad/AgenticAI/Tarea2/Agentic-Tarea-2-Multiagente/data/calendar.json). El archivo se mantiene entre ejecuciones y funciona como calendario persistente del asistente.

## Trazas de ejecucion

El sistema imprime en consola:

- la consulta recibida por el coordinador
- la subtarea detectada
- el agente seleccionado
- la herramienta utilizada
- la evaluacion del critic
- el posible reintento si la respuesta es invalidada
- la respuesta final consolidada

Esto permite cumplir con el requisito de mostrar pasos intermedios durante la ejecucion.

## Dependencias del proyecto

El archivo [requirements.txt](C:/Users/dsanm/OneDrive/Escritorio/Universidad/AgenticAI/Tarea2/Agentic-Tarea-2-Multiagente/requirements.txt) contiene las dependencias necesarias:

- `ollama`
- `ddgs`

## Notas importantes

- La arquitectura actual usa orquestacion propia en Python sobre Ollama.
- Google ADK no esta integrado aun en esta version del proyecto.
- El modelo debe estar disponible localmente en Ollama antes de ejecutar el sistema.
- La busqueda web del `ExpertAgent` depende de conectividad a internet.

## Problemas comunes

### `ModuleNotFoundError`

Activa el entorno virtual e instala las dependencias otra vez:

```bash
pip install -r requirements.txt
```

### `ollama` no responde

Verifica que Ollama este instalado y que el modelo exista:

```bash
ollama list
```

### El modelo configurado no existe

Descargalo manualmente:

```bash
ollama pull gemma3:4b
```

### El experto falla al buscar informacion

Revisa tu conexion a internet, ya que `ddgs` necesita acceso web para recuperar resultados.
