create table clientes (
  cliente_id INTEGER UNSIGNED PRIMARY KEY,
  nombre VARCHAR(60) NOT NULL,
  telefono INTEGER UNIQUE NOT NULL,
  email VARCHAR(30) UNIQUE NOT NULL,
  ciudad VARCHAR(20) NOT NULL,
  pais VARCHAR(20) NOT NULL,
  password VARCHAR(40) NOT NULL
);

create table creditos(
  id_credito INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  id_cliente INTEGER UNSIGNED NOT NULL,
  estado ENUM('pendiente','aprobado','denegado') DEFAULT "pendiente" NOT NULL,
  fecha_solicitud TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  activo BOOLEAN NOT NULL,
  monto INTEGER UNSIGNED NOT NULL,
  interes DECIMAL(3,1) NOT NULL,
  concepto_cliente ENUM('aceptado','rechazado','pendiente') DEFAULT "pendiente" NOT NULL
);

create table pagos (
  id_pago INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  id_credito INTEGER UNSIGNED NOT NULL,
  fecha_pago TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  monto INTEGER UNSIGNED NOT NULL,
  estado ENUM('hecho','pendiente') NOT NULL
);

create table empresas (
  id_empresa INTEGER UNSIGNED PRIMARY KEY,
  id_cliente INTEGER UNSIGNED NOT NULL,
  nombre VARCHAR(40) NOT NULL,
  direccion VARCHAR(30) NOT NULL,
  telefono INTEGER NOT NULL NULL,
  ciudad VARCHAR(20) NOT NULL,
  pais VARCHAR(20) NOT NULL
);

create table cookies (
  id_cookie INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  id_cliente INTEGER UNSIGNED NOT NULL,
  password VARCHAR(60) NOT NULL,
  cookie VARCHAR(40)
);
