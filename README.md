# 🤖 Bot de Gastos para Telegram

Un bot de Telegram que te ayuda a registrar y llevar el control de tus gastos personales.

## 📋 Características

- Registro de gastos con fecha, monto y motivo
- Control del total de gastos acumulados
- Almacenamiento de datos en Excel
- Interfaz simple y fácil de usar

## 🚀 Requisitos

- Python 3.x
- Bibliotecas requeridas:
  - python-telegram-bot
  - pandas
  - openpyxl
  - python-dotenv

## ⚙️ Instalación

1. Clona este repositorio
2. Instala las dependencias:
```bash
pip install python-telegram-bot pandas openpyxl python-dotenv
```

## 🔧 Configuración

1. Obtén un token de BotFather en Telegram
2. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```
TELEGRAM_TOKEN=tu_token_aquí
```

> ⚠️ **Nota**: El archivo `.env` está incluido en `.gitignore` por seguridad. Asegúrate de crear tu propio archivo `.env` con tu token.

## 💰 Uso

1. Inicia el bot:
```bash
python bot_gastos.py
```

2. En Telegram, envía un mensaje al bot con el siguiente formato:
```
Cuándo: DD/MM/AAAA. Cuánto: MONTO colones. En qué: MOTIVO.
```

Ejemplo:
```
Cuándo: 01/01/2025. Cuánto: 1000 colones. En qué: Uber Universidad.
```

3. Comandos disponibles:
- `/start` - Muestra el mensaje de bienvenida y el formato a usar
- `/total` - Muestra el total de gastos acumulados

## 📊 Funcionamiento

- El bot registra cada gasto en un archivo Excel
- Muestra el total acumulado después de cada registro
- Las fechas se guardan en formato DD/MM/AAAA
- Puedes consultar el total de gastos en cualquier momento con el comando `/total`

## 📝 Notas

- Los datos se guardan en el archivo `gastos.xlsx`
- El archivo Excel se crea automáticamente al registrar el primer gasto