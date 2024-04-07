# DevSecOps

Este repositorio contiene un pipeline para un proyecto desarrollado con Streamlit, que incluye análisis de seguridad de dependencias y análisis de código estático con SonarCloud. Este proyecto se ha realizado para el curso DevSecOps de Iebschool.

## Herramientas Utilizadas

### Pip-audit

[Pip-audit](https://pypi.org/project/pip-audit/) es una herramienta de análisis de seguridad de dependencias para Python. Escanea las dependencias de tu proyecto en busca de vulnerabilidades conocidas y te proporciona información sobre cómo resolverlas.

### SonarCloud

[SonarCloud](https://sonarcloud.io/) es una plataforma en la nube para análisis de código estático. Identifica problemas de calidad del código, vulnerabilidades de seguridad y ofrece sugerencias de mejora para tu código Python.

![./Img/SonarCloud.png]

## Ejecución del Proyecto Streamlit

Para ejecutar el proyecto Streamlit:

1. **Instalación de Dependencias**: Crea un entorno virtual y instala las dependencias necesarias ejecutando el siguiente comando:

   ```
   python -m venv .venv
   .venv/Scripts/activate
   pip install -r requirements.txt
   ```

2. **Iniciar aplicación**

    `streamlit run src/app.py`