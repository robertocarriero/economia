# Información Económica Financiera de Argentina

![bcra](https://github.com/user-attachments/assets/088e58e7-7dc7-4e4c-a5dd-448c976865d6)
![bcra1](https://github.com/user-attachments/assets/704d3a8d-ac99-4ad1-a240-1325a79f0ed5)

**Información Económica Financiera de Argentina** es una aplicación web que proporciona datos actualizados sobre indicadores económicos clave del país. La plataforma ofrece herramientas interactivas y visualizaciones que facilitan la comprensión de la situación económica actual.

## Características

- **Simulador de Plazo Fijo**: Permite a los usuarios calcular los intereses generados por una inversión a plazo fijo, ingresando el capital, la Tasa Nominal Anual (TNA) y el período de inversión.
- **Datos del Banco Central de la República Argentina (BCRA)**:
  - **Inflación Mensual**: Información sobre la variación mensual del índice de precios al consumidor.
  - **TNA**: Tasa Nominal Anual vigente.
  - **Depósitos en Entidades Financieras**: Datos sobre los depósitos en el sistema financiero.
- **Cotizaciones del Dólar**:
  - **Dólar Blue**: Cotización del dólar en el mercado paralelo.
  - **Dólar Oficial**: Cotización oficial del dólar.
- **Enlaces de Interés**: Acceso a recursos y sitios web relacionados con la economía y finanzas de Argentina.

## Tecnologías Utilizadas

- **Django**: Framework principal para el desarrollo del backend.
- **Python**: Lenguaje de programación utilizado.
- **JavaScript**: Para funcionalidades interactivas en el frontend.
- **CSS & Bootstrap 4**: Estilizado y diseño responsivo de la aplicación.

- ##  Estructura del Proyecto

economiaproject/
 ├── economia/                
 │   ├── settings.py          
 │   ├── urls.py              
 │   ├── wsgi.py              
 │   ├── asgi.py              
 │   └── __init__.py
 │
 ├── app_economia/            
 │   ├── migrations/          
 │   ├── static/              
 │   │   ├── css/             
 │   │   ├── js/              
 │   │   └── images/         
 │   ├── templates/          
 │   ├── views.py            
 │   ├── models.py            
 │   ├── urls.py             
 │   ├── forms.py            
 │   ├── admin.py            
 │   ├── tests.py             
 │   └── __init__.py         
 │
 ├── db.sqlite3               
 ├── manage.py                
 ├── requirements.txt        
 ├── README.md               
 ├── .gitignore               
 └── .env                     
```

### ** Explicación**
- 📂 `economia/` → Carpeta principal del proyecto Django.
- 📂 `app_economia/` → Aplicación específica dentro del proyecto.
- 📂 `static/` → Contiene archivos estáticos (CSS, JS, imágenes).
- 📂 `templates/` → Contiene las plantillas HTML utiliza






