# 🚗 Sistema de Gestión Automotora

Este proyecto es una aplicación web desarrollada con **Django** diseñada para administrar de forma integral una concesionaria de vehículos. Permite la gestión de sedes, vendedores y stock de autos a través de una interfaz moderna y amigable.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** [Python](https://www.python.org/) & [Django Framework](https://www.djangoproject.com/)
* **Frontend:** [Bootstrap 5](https://getbootstrap.com/) (CSS/JS) & [Bootstrap Icons](https://icons.getbootstrap.com/)
* **Base de Datos:** [SQLite](https://www.sqlite.org/) (Local)

---

## 🚀 Funcionalidades

- **Panel de Control:** Inicio con acceso rápido a todas las áreas.
- **Altas Personalizadas:** Formularios modernos para Automotoras, Vendedores y Autos con mensajes de éxito sin redirección.
- **Buscador de Sedes:** Motor de búsqueda por nombre con visualización en tablas profesionales.
- **Vista de Detalle:** Página específica para consultar la información completa de cada automotora.
- **Diseño Responsive:** Adaptado para su uso en computadoras y dispositivos móviles.

---

## 📂 Estructura del Proyecto

- `concesionaria/models.py`: Definición de las entidades (Auto, Vendedor, Automotora).
- `concesionaria/views.py`: Lógica de negocio y procesamiento de formularios.
- `concesionaria/urls.py`: Configuración de rutas y parámetros dinámicos.
- `templates/`: Plantillas HTML con herencia de base y componentes Bootstrap.

---

## ⚙️ Guía de Instalación (Paso a Paso)

Sigue estas instrucciones para replicar el entorno de desarrollo en tu computadora local:

### 1. Clonar el repositorio
Descarga el código fuente en tu máquina local:
git clone https://github.com/mauroatp/TuPrimeraPagina-deSoza.git

### 2. Configuración del Entorno Virtual

Crea el entorno para aislar las librerías:
python -m venv env

### 3. Activación del Entorno

env\Scripts\activate
Sabrás que está activo porque aparecerá (env) al principio de la línea en tu terminal.

### 4. Instalación de Django

pip install django

### 5. Preparación de la Base de Datos

Genera los archivos necesarios para guardar la información localmente:
python manage.py makemigrations
python manage.py migrate

### 6. Creación de la cuenta de Administrador

Crea un usuario para acceder al panel /admin:
python manage.py createsuperuser
Escribe el nombre de usuario, correo y contraseña (los caracteres no se verán mientras escribes por seguridad).

### 7. Ejecución del Sistema

Inicia el servidor local:
python manage.py runserver
Accede mediante tu navegador a: http://127.0.0.1:8000/
