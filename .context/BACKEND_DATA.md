# Context Engineering: Backend Data Model

Este documento define el modelo de datos relacional de PostgreSQL, que opera como la única fuente de la verdad para el sistema.

## Herencia Polimórfica

### Tabla Padre: `registros_base`
Contiene la información común de todos los registros emitidos en el sistema.
- `id` (UUID) - Primary Key
- `inspector_id` - Identificador del inspector
- `modulo` - Módulo de origen del registro
- `estado` - Estado actual del registro
- `fecha_emision` - Fecha y hora de la emisión
- `ubicacion` - Coordenadas espaciales (PostGIS)
- `auditoria_jsonb` (JSONB) - Historial inmutable de estados del registro

### Tabla Hija: `infracciones_vehiculares`
Extiende a `registros_base` con información específica de infracciones de tránsito.
- `registro_uuid` (PK/FK) - Referencia a `registros_base.id`
- `ppu` - Placa Patente Única
- `marca` - Marca del vehículo
- `tipo_vehiculo` - Tipo de vehículo
- `color` - Color del vehículo
- `tipo_infraccion_id` (Integer/FK) - Referencia al catálogo de infracciones (`catalogo_infracciones.id`)
- `observaciones` (Text) - Detalles narrativos ingresados por el inspector (Obligatorio)

## Evidencias

### Tabla: `evidencias_fotograficas`
Almacena las evidencias multimedia asociadas a un registro.
- `registro_uuid` - Referencia al registro base
- `hash_sha256` - Hash criptográfico de la imagen para integridad
- **Constraint:** UNIQUE compuesto por (`registro_uuid`, `hash_sha256`) para evitar evidencias duplicadas en la misma acta.

## Auditoría y Sincronización

### Tabla: `auditoria_eventos`
Registro inmutable de acciones en el sistema.
- Utiliza columnas `JSONB` para almacenar el payload de eventos y cambios de estado.

### Tabla: `sync_events`
Control y trazabilidad de los eventos de sincronización entre clientes móviles y el backend.

## Seguridad y Accesos

### Tabla: `usuario_mfa`
Almacena credenciales de múltiples factores.
- `usuario_id` - Referencia a `usuarios.id`
- Secretos TOTP y códigos de recuperación encriptados.

### Tabla: `dispositivos_moviles`
Controla los dispositivos autorizados.
- `usuario_id` - Referencia a `usuarios.id`
- `device_id` - Identificador único de hardware
- `estado` - Estado del dispositivo (ej: 'ACTIVO')
- `revocado` - Bandera de acceso revocado
