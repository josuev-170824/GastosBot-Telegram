from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import pandas as pd
from datetime import datetime
import re
from dotenv import load_dotenv
import os

# CONFIG
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
PRESUPUESTO = 20000  # Monto quincenal
ARCHIVO = 'gastos.xlsx'  # Archivo Excel para datos

# CARGAR DATOS
def cargar_datos():
    try:
        df = pd.read_excel(ARCHIVO)
        df["Fecha"] = pd.to_datetime(df["Fecha"]).dt.date
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Fecha", "Monto", "Motivo"])
    except Exception as e:
        return pd.DataFrame(columns=["Fecha", "Monto", "Motivo"])

# GUARDAR DATOS
def guardar_datos(df):
    df = df.sort_values(by="Fecha", ascending=True)
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    with pd.ExcelWriter(ARCHIVO, engine='openpyxl', datetime_format='dd/mm/yyyy') as writer:
        df.to_excel(writer, index=False)

# COMANDO /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hola, soy tu bot de gastos. Envíame un mensaje así:\n\nCuándo: 13/06/2025. Cuánto: 1000 colones. En qué: Uber al gym.")

# MENSAJE DE GASTO
async def registrar_gasto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text.strip()

    match = re.search(r"Cuándo:\s*(\d{2}/\d{2}/\d{4}).*?Cuánto:\s*(\d+).*?En qué:\s*(.+)", mensaje, re.IGNORECASE)
    
    if match:
        fecha_str = match.group(1)
        monto = int(match.group(2))
        motivo = match.group(3).strip()

        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            await update.message.reply_text("❌ La fecha no es válida. Use formato: 13/06/2025.")
            return

        df = cargar_datos()
        
        nuevo_gasto = pd.DataFrame([{"Fecha": fecha, "Monto": monto, "Motivo": motivo}])
        df = pd.concat([df, nuevo_gasto], ignore_index=True)
        
        guardar_datos(df)

        total_gastos = df["Monto"].sum()
        restante = PRESUPUESTO - total_gastos

        respuesta = (
            f"✅ Va a registrar:\n"
            f"📅 Fecha: {fecha.strftime('%d/%m/%Y')}\n"
            f"💵 Monto: ₡{monto:,}\n"
            f"📝 Motivo: {motivo}\n\n"
            f"✔️ Ya fue registrado. Quedan ₡{restante:,} del presupuesto."
        )
        await update.message.reply_text(respuesta)

    else:
        await update.message.reply_text(
            "❌ Prompt no tiene el formato correcto.\n"
            "Por favor usá este formato:\n\n"
            "Cuándo: 13/06/2025. Cuánto: 1200 colones. En qué: Uber al gym."
        )

# INICIAR EL BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, registrar_gasto))

app.run_polling()
