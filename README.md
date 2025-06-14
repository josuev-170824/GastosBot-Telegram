# 🤖 Bot de Gastos para Telegram

Un bot de Telegram que te ayuda a registrar y llevar el control de tus gastos personales.

## 📋 Características

- Registro de gastos con fecha, monto y motivo
- Control de presupuesto quincenal
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
Cuándo: 13/06/2025. Cuánto: 1000 colones. En qué: Uber al gym.
```

## 📊 Funcionamiento

- El bot registra cada gasto en un archivo Excel
- Mantiene un control del presupuesto quincenal (₡20,000 por defecto)
- Muestra el monto restante después de cada registro
- Las fechas se guardan en formato DD/MM/AAAA

## 📝 Notas

- Los datos se guardan en el archivo `gastos.xlsx`
- El presupuesto se reinicia cada quincena
- Puedes modificar el monto del presupuesto en la variable `PRESUPUESTO` 