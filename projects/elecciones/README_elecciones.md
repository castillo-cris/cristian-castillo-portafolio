# 🗳️ Proyecto de Análisis Electoral en Colombia  
**General Electoral Analysis Project in Colombia**

## 📌 Descripción / Description
Este espacio reúne múltiples proyectos de análisis electoral en Colombia, con el objetivo de **explorar, documentar y visualizar dinámicas democráticas** usando datos públicos y oficiales.  
This repository gathers multiple electoral analysis projects in Colombia to **explore, document, and visualize** democratic dynamics using public and official data.

Incluye:
- Bases de datos históricas (censo, participación, financiación, observación política).  
- Procesos de limpieza y normalización de datos.  
- Visualizaciones comparativas y mapas interactivos.  
- Documentación bilingüe para audiencias locales e internacionales.  

---

## 📂 Estructura del proyecto / Project structure

projects/elecciones/
├── data/ 
│ ├── raw/ # Datos originales (CSV, GeoJSON, etc.) - gestionados con Git LFS 
│ ├── processed/ # Datos limpios y normalizados 
│ 
├── notebooks/ # Jupyter Notebooks con análisis temáticos 
├── mapas/ # Mapas interactivos en HTML ├── docs/ # Documentación y reportes └── README.md # Este archivo


---

## ⚙️ Requisitos / Requirements
- Python 3.9+
- Librerías principales:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`
  - `geopandas`, `folium`
  - `unicodedata`

Instalación rápida:
```bash
pip install -r requirements.txt

git lfs install
git clone https://github.com/castillo-cris/cristian-castillo-portafolio.git
