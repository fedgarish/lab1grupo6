<p align="center">
  <img src="Evidencias/logo-uide.webp" width="220" alt="Logo UIDE">
</p>

<h1 align="center">Laboratorio 1 - Grupo 6</h1>

<p align="center">
  <b>MCIB-B</b><br>
  Trabajo grupal enfocado en el desarrollo, contenerización y despliegue de un API funcional.
</p>
<h2>Integrantes</h2>

<ul>
  <li>AMAGUA OSCAR</li>
  <li>OJEDA ALAN</li>
  <li>SUNTAXI DIEGO</li>
</ul>
<hr>

<h2>Introducción</h2>
<p>
El presente proyecto tiene como objetivo el diseño, construcción, contenerización y despliegue de una API funcional orientada al análisis de seguridad de archivos. La solución desarrollada permite autenticar usuarios mediante tokens JWT, procesar solicitudes a través de endpoints REST (GET y POST), y consumir servicios externos, específicamente la API de VirusTotal, con el fin de obtener información sobre posibles amenazas asociadas a un hash de archivo.

La API actúa como un intermediario inteligente que no solo consulta información externa, sino que también aplica lógica propia para interpretar los resultados, generando un veredicto simplificado y un indicador de riesgo. De esta manera, se simula el funcionamiento de sistemas utilizados en entornos reales de ciberseguridad, como centros de operaciones de seguridad (SOC), donde es necesario analizar rápidamente archivos sospechosos y tomar decisiones informadas.

Adicionalmente, el proyecto incorpora buenas prácticas de desarrollo de software, incluyendo el uso de control de versiones con GitHub para la gestión colaborativa del código, la contenerización mediante Docker para asegurar la portabilidad y consistencia del entorno de ejecución, la validación de endpoints utilizando herramientas como curl, y el despliegue en la nube a través de servicios como Google Cloud, garantizando así la disponibilidad y accesibilidad del servicio.

En conjunto, esta solución no solo cumple con los requerimientos técnicos planteados, sino que también representa una aproximación práctica al desarrollo de APIs modernas, seguras y escalables, integrando múltiples tecnologías y servicios en un flujo de trabajo completo desde el desarrollo hasta el despliegue en producción.
</p>

<hr>

<h2>Objetivo</h2>
<p>
  Diseñar, construir, contenerizar y desplegar un API funcional, aplicando buenas prácticas de desarrollo, versionamiento, pruebas y despliegue en la nube.
</p>

<hr>

<h2>Parte 1 – Construcción del API</h2>

<h3>Repositorio del proyecto</h3>
<ul>
  <li>Código fuente del API</li>
  <li>README documentado</li>
  <li>Dockerfile funcional</li>
  <li>requirements.txt</li>
</ul>

<h3>API funcional</h3>
<ul>
  <li>Flask</li>
  <li>FastAPI</li>
  <li>Otro framework Python aprobado</li>
</ul>

<h3>Funcionalidades mínimas</h3>
<ul>
  <li>Endpoint <b>GET</b></li>
  <li>Endpoint <b>POST</b></li>
  <li>Validación básica de datos</li>
  <li>Respuestas en formato JSON</li>
</ul>

<h3>Creatividad</h3>
<ul>
  <li>Integración con APIs externas</li>
  <li>Sistema de scoring</li>
  <li>Procesamiento de datos</li>
  <li>Logs estructurados</li>
  <li>Autenticación básica</li>
</ul>

<h3>Evidencia</h3>
<h5>Codigo API</h5>
<p align="center">
  <img src="Evidencias/parte1-1.png" width="500">
  <img src="Evidencias/parte1-2.jfif" width="500">
</p>
<h5>Estructura del codigo de la API</h5>
<p align="center">
  <img src="Evidencias/parte1-3.png" width="500">
</p>
<h5>Codigo Requirements</h5>
<p align="center">
  <img src="Evidencias/parte1-4.jfif" width="500">
</p>
<h5>Codigo Dockerfile</h5>
<p align="center">
  <img src="Evidencias/parte1-5.png" width="500">
</p>
<h5>Codigo de gitignore</h5>
<p align="center">
  <img src="Evidencias/parte1-6.png" width="500">
</p>
<h5>Codigo de dockerignore</h5>
<p align="center">
  <img src="Evidencias/parte1-7.png" width="500">
</p>
<h5>Codigo de Env</h5>
<p align="center">
  <img src="Evidencias/parte1-8.png" width="500">
</p>
<h3>Comentario</h3>
<p>
  En esta fase se desarrolló la estructura base del API, implementando endpoints GET y POST con validaciones básicas. 
  Se utilizó FastAPI por su facilidad de uso y documentación automática.
</p>

<hr>

<h2>Parte 2 – Uso de Branches</h2>

<p>
  Se desarrollaron funcionalidades en ramas independientes y luego se integraron a la rama principal <code>main</code>.
</p>

<ul>
  <li><code>feature/geolocalizacion</code></li>
  <li><code>feature/scoring</code></li>
  <li><code>feature/auth</code></li>
</ul>

<h3>Evidencia</h3>
<h5>Historial de cambios en ramificaciones</h5>
<p align="center">
  <img src="Evidencias/parte2-1.png" width="500">
</p>
<h5>Estructura de ramificaciones de git</h5>
<p align="center">
  <img src="Evidencias/parte2-2.png" width="500">
</p>

<h3>Comentario</h3>
<p>
  El uso de branches permitió trabajar de manera organizada y evitar conflictos en el código principal, facilitando la integración continua.
</p>

<hr>

<h2>Parte 3 – Contenerización</h2>

<ul>
  <li>Dockerfile funcional</li>
  <li>Imagen construida sin errores</li>
  <li>Contenedor ejecutando correctamente</li>
</ul>

<h3>Evidencia</h3>
<h5>Creación del docker</h5>
<p align="center">
  <img src="Evidencias/parte3-1.png" width="500">
</p>
<h5>Estructura del docker</h5>
<p align="center">
  <img src="Evidencias/parte3-2.png" width="500">
</p>
<h5>Prueba de creacion del docker sin error</h5>
<p align="center">
  <img src="Evidencias/parte3-3.jfif" width="500">
</p>

<h3>Comentario</h3>
<p>
  Se logró contenerizar el API correctamente, permitiendo su ejecución en cualquier entorno sin dependencias externas.
</p>

<hr>

<h2>Parte 4 – Pruebas con curl</h2>

<ul>
  <li>GET funcionando</li>
  <li>POST funcionando</li>
  <li>Manejo de errores</li>
</ul>

<h3>Evidencia</h3>
<h5>Prueba de funcionalidad endpoints GET y POST con Curl</h5>
<p align="center">
  <img src="Evidencias/parte4-1.png" width="500">
</p>
<h5>Prueba de funcionalidad validación errores con Curl</h5>
<p align="center">
  <img src="Evidencias/parte4-2.png" width="500">
</p>


<h3>Comentario</h3>
<p>
  Las pruebas con curl permitieron validar el correcto funcionamiento de los endpoints y el manejo adecuado de errores.
</p>

<hr>

<h2>Parte 5 – Despliegue en Cloud</h2>

<ul>
  <li>Cloud Run</li>
  <li>Compute Engine</li>
  <li>Otro servicio cloud</li>
</ul>

<h3>Evidencia</h3>
<h5>Proceso de despliegue en Google Cloud</h5>
<p align="center">
  <img src="Evidencias/parte5-1.png" width="500">
  <img src="Evidencias/parte5-2.png" width="500">
</p>
<h5>Verificación de funcionalidad de endpoints</h5>
<p align="center">
  <img src="Evidencias/parte5-3.png" width="500">
</p>
<h5>Verificación de metricas generadas de la API</h5>
<p align="center">
  <img src="Evidencias/parte5-4.png" width="500">
</p>
<h5>Eliminación del despliegue</h5>
<p align="center">
  <img src="Evidencias/parte5-5.png" width="500">
</p>

<h3>Comentario</h3>
<p>
  El despliegue en la nube permitió acceder al API de forma remota, garantizando disponibilidad y escalabilidad.
</p>

<hr>
<h3>Preguntas trabajo final</h3>

<p>
  <strong>1. ¿Cómo podrían mejorar la lógica de interpretación de resultados para que el “veredicto simplificado” sea más transparente, explicable y confiable para el usuario?</strong>
</p>

<p>
Para mejorar la interpretación de resultados y hacer el veredicto más transparente, explicable y confiable, se propone enriquecer la lógica actual basada en el <code>risk_score</code> y el número de detecciones obtenidas desde la API de VirusTotal.
</p>

<p>
En lugar de mostrar únicamente un resultado binario como <b>"AMENAZA DETECTADA"</b>, se puede implementar un sistema más descriptivo que incluya:
</p>

<ul>
  <li>Clasificación por nivel de riesgo (Bajo, Medio, Alto, Crítico)</li>
  <li>Porcentaje de detección en relación al total de motores analizados</li>
  <li>Explicación clara del resultado obtenido</li>
  <li>Recomendaciones para el usuario según el nivel de riesgo</li>
</ul>

<p>
Adicionalmente, se puede definir una lógica de clasificación basada en rangos:
</p>

<ul>
  <li>0 detecciones → Seguro</li>
  <li>1–10 detecciones → Bajo riesgo</li>
  <li>11–30 detecciones → Sospechoso</li>
  <li>31–60 detecciones → Alto riesgo</li>
  <li>Más de 60 detecciones → Crítico / Amenaza detectada</li>
</ul>

<p>
Ejemplo de respuesta mejorada del API:
</p>

<pre><code class="language-json">
{
  "hash": "275a021bbfd6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "veredicto": "ALTO RIESGO",
  "nivel": "CRITICO",
  "confianza": "88%",
  "detalle": {
    "detecciones": 67,
    "total_motores": 76,
    "porcentaje_deteccion": 88
  },
  "resumen": "El archivo ha sido identificado como malicioso por múltiples motores de análisis.",
  "recomendacion": "Se recomienda no ejecutar el archivo y proceder con su eliminación."
}
</code></pre>

<p>
Con estas mejoras, el sistema no solo entrega un resultado, sino que también proporciona contexto, facilitando la toma de decisiones por parte del usuario y aumentando la confianza en el análisis.
</p>

<hr>
<h3>Conclusiones</h3>
<ul>
  <li>La correcta configuración de las variables globales de Git es fundamental para identificar adecuadamente los commits y mantener un historial limpio en trabajos colaborativos.</li>
  <li>El flujo adecuado de trabajo siempre debe iniciar con un git pull, seguido del desarrollo, commit y finalmente un git push, evitando conflictos y pérdidas de información.
El uso de ramas permite trabajar de forma ordenada sin afectar la rama principal, facilitando la revisión y la integración de cambios mediante Pull Requests.</li>
  <li>La integración de variables sensibles mediante .env dentro del flujo de Docker proporcionó un nivel adicional de organización y seguridad. Esto evitó exponer claves privadas o configuraciones críticas en el repositorio, manteniendo buenas prácticas en la gestión de credenciales y configuraciones.</li>
  <li>El uso de Docker permitió estandarizar completamente el entorno de ejecución, garantizando que la API se comporte de la misma manera en cualquier máquina. Esto eliminó problemas recurrentes asociados a diferencias en versiones de Python, dependencias o configuraciones locales entre los integrantes del equipo.</li>
  <li>La integración del archivo .env dentro del flujo de Docker reforzó la seguridad al evitar exponer claves sensibles, además de simplificar la configuración del entorno.</li>
  <li>El archivo .env no funcionó correctamente en GCloud porque incluía variables que la plataforma tiene reservadas, como PORT. Como medida de seguridad, GCloud activa un bloqueo por timeout cuando una aplicación no arranca de manera adecuada, lo que impidió que la API se desplegara correctamente. Para solucionar esto, fue necesario eliminar esas variables del entorno y configurar únicamente los secretos válidos, permitiendo que Cloud Run arrancara la API correctamente y sin bloquearla.</li>
</ul>

<hr>

