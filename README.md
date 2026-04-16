# GitHub Actions Workshop  
**CI, Docker, Docker Hub y despliegue por ambientes con Render**

Este repositorio fue creado como base práctica para aprender los fundamentos de **CI/CD** usando una aplicación sencilla en Python. El objetivo del workshop es entender cómo un cambio en código pasa por validaciones automáticas, se empaqueta como imagen Docker, se publica en un registry y finalmente se despliega en distintos ambientes.

Al finalizar el workshop, el flujo completo debe permitir:

- validar código con **lint**,
- ejecutar **tests automáticos**,
- construir una **imagen Docker**,
- publicarla en **Docker Hub**,
- desplegar automáticamente a un ambiente **dev** desde la rama `dev`,
- y desplegar automáticamente a un ambiente **prod** desde la rama `master`.

---

## Objetivo del repositorio

Este proyecto está diseñado para enseñar, de forma progresiva, cómo conectar:

- **Git y GitHub**
- **GitHub Actions**
- **Docker**
- **Docker Hub**
- **Render**
- y el concepto de **ambientes de despliegue**

La meta es entender cómo se construye un flujo de ingeniería profesional, reproducible y trazable.

---

## Tecnologías utilizadas

- **Python**
- **FastAPI**
- **Pytest**
- **Ruff**
- **Docker**
- **GitHub Actions**
- **Docker Hub**
- **Render**

---

## Estructura del proyecto

```text
github-actions-workshop/
  app/
    main.py
    calculator.py
  tests/
    test_calculator.py
  requirements.txt
  Dockerfile
  README.md
  .github/
    workflows/
      ci.yml