# Diccionario de Datos - Sistema de Fiscalización Municipal (SGF)

Este documento contiene el diccionario de datos de la base de datos PostgreSQL (`sgf_core`) utilizada por el backend del sistema para el MVP y la arquitectura Offline-First.

---

## 1. Módulo de Seguridad y Accesos

### Tabla: `roles`
Almacena los niveles de acceso al sistema.
* **`id`** (Integer) - *Primary Key*. Identificador único del rol.
* **`nombre`** (String) - Nombre del rol (ej: Administrador, Inspector). *Único*.

### Tabla: `usuarios`
Almacena las credenciales de los inspectores y administradores.
* **`id`** (UUID) - *Primary Key*. Identificador único del usuario.
* **`username`** (String) - Nombre de usuario para iniciar sesión. *Único*.
* **`hashed_password`** (String) - Contraseña encriptada mediante Bcrypt.
* **`activo`** (Boolean) - Indica si el usuario puede acceder al sistema.
* **`rol_id`** (Integer) - *Foreign Key*. Referencia a `roles.id`.

### Tabla: `sesiones_moviles`
Registro de tokens y sesiones para auditoría de conexiones (Módulo futuro / Opcional en el MVP Stateless).
* **`id`** (UUID) - *Primary Key*.
* **`usuario_id`** (UUID) - *Foreign Key*. Referencia a `usuarios.id`.
* **`dispositivo_id`** (String) - Identificador único del celular.
* **`token_hash`** (String) - Hash SHA-256 del token emitido.
* **`creada_at`** (DateTime) - Fecha de inicio de sesión.
* **`expira_at`** (DateTime) - Fecha límite de vigencia del token.
* **`revocada`** (Boolean) - Si es `true`, invalida prematuramente la sesión.

---

## 2. Módulo de Registros (Herencia Polimórfica)

### Tabla: `registros_base`
Tabla maestra que contiene los datos comunes a cualquier tipo de registro, acta o citación en el sistema.
* **`id`** (UUID) - *Primary Key*. Identificador universal generado desde el dispositivo móvil offline.
* **`inspector_id`** (UUID) - *Foreign Key*. Referencia al inspector (`usuarios.id`) que emitió el registro.
* **`modulo`** (String) - Discriminador polimórfico (ej: 'infraccion_vehicular').
* **`estado`** (String) - Estado de la sincronización (ej: 'sincronizado', 'guardadoLocal').
* **`fecha_emision`** (DateTime) - Fecha y hora exacta en la que se generó en la calle.
* **`ubicacion`** (Geometry POINT) - Coordenadas geográficas espaciales usando SRID 4326 (PostGIS).

### Tabla: `infracciones_vehiculares`
Extiende a `registros_base` con los campos específicos para multas y citaciones de tránsito.
* **`registro_uuid`** (UUID) - *Primary Key* y *Foreign Key*. Referencia a `registros_base.id`.
* **`ppu`** (String) - Placa Patente Única del vehículo involucrado.
* **`rut_infractor`** (String) - RUT del conductor (Opcional).
* **`nombre_completo`** (String) - Nombre del conductor (Opcional).
* **`marca`** (String) - Marca del vehículo.
* **`tipo_vehiculo`** (String) - Tipo de vehículo (Auto, Moto, Camioneta, etc.).
* **`color`** (String) - Color del vehículo.
* **`tipo_infraccion_id`** (String) - Código del tipo de infracción (1 = Advertencia, 2 = Citación JPL).
* **`observaciones`** (Text) - Detalles adicionales ingresados por el inspector (Opcional).

### Tabla: `evidencias_fotograficas`
Guarda el registro inmutable de las fotografías tomadas en terreno para validación criptográfica.
* **`id`** (UUID) - *Primary Key*. Identificador único de la evidencia.
* **`registro_uuid`** (UUID) - *Foreign Key*. Vinculada al acta correspondiente en `registros_base.id`.
* **`hash_sha256`** (String) - Cadena de hash inmutable de la foto tomada localmente, garantiza que la imagen no fue adulterada.

---

## 3. Módulo de Auditoría y Telemetría

### Tabla: `auditoria_eventos`
Registro detallado de cambios de estado y acciones del usuario en el sistema.
* **`id`** (UUID) - *Primary Key*.
* **`entidad_id`** (String) - UUID o identificador de la entidad afectada.
* **`entidad_tipo`** (String) - Tipo de entidad (ej: 'InfraccionVehicular').
* **`accion`** (String) - Acción realizada (ej: 'CREACION_POR_SYNC').
* **`usuario_id`** (UUID) - *Foreign Key*. Usuario responsable de la acción.
* **`payload`** (JSONB) - Respaldo en formato JSON del cuerpo de datos recibido.
* **`fecha`** (DateTime) - Fecha y hora del evento en el servidor.

### Tabla: `sync_events`
Telemetría técnica sobre los procesos de sincronización masivos de la arquitectura Offline-First.
* **`id`** (UUID) - *Primary Key*.
* **`dispositivo_id`** (String) - ID o modelo del equipo que realiza el sync.
* **`inspector_id`** (UUID) - *Foreign Key*. Referencia a `usuarios.id`.
* **`fecha_sync`** (DateTime) - Marca de tiempo de la sincronización.
* **`estado`** (String) - Resultado (ej: 'EXITOSO', 'ERROR').
* **`detalles`** (JSONB) - Metadata adicional u observaciones técnicas del ciclo de sync.

---

## 4. Tablas Catálogo / Diccionarios

### Tabla: `catalogo_infracciones`
Diccionario paramétrico del tipo de resoluciones permitidas.
* **`id`** (Integer) - *Primary Key*. Código paramétrico.
* **`nombre`** (String) - Nombre de la resolución (ej: 'Advertencia Empadronada', 'Citación JPL').
* *(Puede contener campos descriptivos o montos de penalización asociados según ordenanza municipal)*.

### Tabla: `spatial_ref_sys`
*Nota: Esta tabla es exclusiva de la extensión **PostGIS**. Es un catálogo del estándar OGC con más de 8500 sistemas de proyección cartográfica. No almacena datos de la aplicación, sino diccionarios de coordenadas.*
