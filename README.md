![CI](https://github.com/vicentexte/EncrypterAES/actions/workflows/pytest_encrypter.yml/badge.svg)   /  ![CI](https://github.com/vicentexte/EncrypterAES/actions/workflows/flake_test.yml/badge.svg)

# Pasos para utilizar AES encrypter
El siguiente documento explica los pasos para poder utilizar el AES encrypter, instalar las dependencias y configurar el entorno virtual del proyecto.

## Requisitos

Este proyecto depende de varias bibliotecas de Python. Puedes instalar todas las dependencias automáticamente usando el archivo `requirements.txt`.

### 1. Crear y activar un entorno virtual

Antes de instalar las dependencias, es recomendable crear un entorno virtual para aislar las bibliotecas necesarias para este proyecto.

#### En Linux/macOS:
```bash
python3 -m venv myenv
source myenv/bin/activate 
```

#### En Windows
```bash
python -m venv myenv
myenv\Scripts\activate
```
#### Para desactivar el entorno virtual
```bash
deactivate
```
### 2. Instalar dependencias
Este programa requiere de la instalación de las librerias pycryptodome y pytest para funcionar. Para instalarlas solo debes ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```

### 3. Utilizar el programa
Ya puedes utilizar el programa correctamente para encriptar, desencriptar y realizar un test. Es importante tener el entorno virtual activado para este paso.

#### Encriptar

```bash
python encrypter.py 
```

#### Desencriptar

```bash
python decrypter.py 
```

#### Realizar test

```bash
pytest test_encrypter.py
```
