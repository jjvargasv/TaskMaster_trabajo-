# Manual de Despliegue - TaskMaster

Este manual te guía para desplegar TaskMaster tanto en local como en un servidor remoto.

---

## 1. Requisitos previos
- Python 3.10+
- Node.js y npm
- SQL Server (local o en la nube)

---

## 2. Despliegue local

### Backend (Django)
1. Ve a la carpeta `backend`:
   ```sh
   cd backend
   ```
2. Activa el entorno virtual:
   ```sh
   .\venv\Scripts\activate
   ```
3. Instala dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Configura el archivo `.env` con los datos de tu base SQL Server.
5. Aplica migraciones:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Inicia el servidor:
   ```sh
   python manage.py runserver
   ```

### Frontend (React)
1. Ve a la carpeta `frontend`:
   ```sh
   cd ../frontend
   ```
2. Instala dependencias:
   ```sh
   npm install
   ```
3. Inicia el servidor React:
   ```sh
   npm start
   ```
4. Accede a [http://localhost:3000](http://localhost:3000)

---

## 3. Despliegue remoto (recomendaciones)

### Backend
- Puedes usar servicios como Railway, Azure App Service o un VPS.
- Asegúrate de tener configurado SQL Server accesible desde el servidor.
- Usa variables de entorno seguras para las credenciales.
- Si usas Nginx o Apache, configura el proxy para servir Django con Gunicorn.

### Frontend
- Puedes desplegar en Vercel, Netlify o Azure Static Web Apps.
- Solo sube la carpeta `build` generada por:
   ```sh
   npm run build
   ```

---

## 4. Seguridad y producción
- Cambia `DEBUG = False` en `settings.py` para producción.
- Usa un `SECRET_KEY` seguro.
- Configura correctamente `ALLOWED_HOSTS`.
- Usa HTTPS en producción.

---

## 5. Soporte
Para dudas técnicas, revisa la documentación oficial de Django, React y SQL Server, o contacta al administrador del sistema.
