<!-- 
=======================================================================================================================
Decisiones permanentes del proyecto:

1. StoreTic es un sistema híbrido (Desktop + Web)
2. El Desktop es el panel de administración principal
3. La API es el punto único de acceso a datos
4. PostgreSQL es la base de datos central
5. CustomTkinter es obligatorio para Desktop
6. El proyecto prioriza entornos con recursos limitados
=======================================================================================================================
 -->


Decisiones estructurales permanentes del proyecto StoreTic (14-01-2026):

1. StoreTic es un sistema híbrido:
   - Desktop (administración)
   - Backend API (núcleo)
   - Web (fase futura)

2. La aplicación Desktop:
   - Es el panel de administración principal
   - Nunca accede directamente a la base de datos

3. El backend:
   - Es el único punto de acceso a los datos
   - Centraliza toda la lógica de negocio

4. La base de datos:
   - Es única y compartida
   - SQLite solo para desarrollo
   - PostgreSQL para producción

5. Prioridades del proyecto:
   - Simplicidad
   - Estabilidad
   - Mantenibilidad
   - Adecuado para entornos con recursos limitados

Estas decisiones no deben romperse en futuras implementaciones.