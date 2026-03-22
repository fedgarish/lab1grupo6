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
  <li>OJEDA ALIN</li>
  <li>SUNTAXI DIEGO</li>
</ul>
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
<p align="center">
  <img src="Evidencias/parte3.png" width="500">
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
<p align="center">
  <img src="Evidencias/parte4.png" width="500">
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
<p align="center">
  <img src="Evidencias/parte5.png" width="500">
</p>

<h3>Comentario</h3>
<p>
  El despliegue en la nube permitió acceder al API de forma remota, garantizando disponibilidad y escalabilidad.
</p>

<hr>

