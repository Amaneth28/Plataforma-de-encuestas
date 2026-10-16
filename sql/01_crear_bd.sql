-- Configuración inicial de MySQL

-- 1. CREAR BASE DE DATOS

CREATE DATABASE IF NOT EXISTS plataforma_encuestas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- 2. CREAR USUARIO

CREATE USER IF NOT EXISTS 'encuestas_user'@'%'
IDENTIFIED BY 'CONTRASEÑA_A_CONFIGURAR';

-- 3. ASIGNAR PERMISOS

GRANT ALL PRIVILEGES
ON plataforma_encuestas.*
TO 'encuestas_user'@'%';

-- 4. APLICAR PERMISOS

FLUSH PRIVILEGES;