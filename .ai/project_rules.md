<!-- 
=======================================================================================================================
Proyecto: StoreTic

StoreTic es un sistema híbrido:
- Aplicación de Escritorio (CustomTkinter) para administración
- Backend central (API)
- Aplicación Web (fase futura)
- Base de datos compartida PostgreSQL

Principios del proyecto:
1. Simplicidad antes que complejidad
2. Código legible antes que elegante
3. Arquitectura clara antes que velocidad de desarrollo
4. Pensado para entornos con conectividad limitada
5. Usuarios finales con bajo nivel técnico

Restricciones:
- No usar frameworks pesados innecesarios
- No acoplar Desktop directamente a la base de datos
- Toda comunicación debe pasar por la API
- No introducir lógica de negocio en la interfaz 
=======================================================================================================================
-->

Reglas del proyecto StoreTic:

Arquitectura:
- Desktop → API → Base de datos
- No lógica de negocio en la interfaz
- No acceso directo a la BD desde el Desktop

Código:
- Python claro y explícito
- Funciones cortas y legibles
- Evitar abstracciones innecesarias
- Evitar sobre-ingeniería

Desarrollo:
- Cada cambio debe respetar el estado actual del proyecto
- No asumir funcionalidades no implementadas
- Toda nueva funcionalidad debe ser incremental

Alcance:
- Primero cerrar ciclos completos (producto → venta → reporte)
- Luego añadir seguridad, optimización y nuevas capas

