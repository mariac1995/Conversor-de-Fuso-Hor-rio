import streamlit as st
from datetime import datetime, date, time
import pytz


# CONFIGURAÇÃO
st.set_page_config(
    page_title="Conversor de Fuso Horário",
    page_icon="🌎"
)


st.title("🌎 Conversor de Fuso Horário")
st.write("Agende clientes em diferentes locais convertendo horários automaticamente.")


# -----------------------------
# LOCAIS
# -----------------------------

locais = {

    # Estados
    "Acre (AC)": "America/Rio_Branco",
    "Amazonas (AM)": "America/Manaus",
    "Roraima (RR)": "America/Boa_Vista",
    "Rondônia (RO)": "America/Porto_Velho",

    "Mato Grosso (MT)": "America/Cuiaba",
    "Mato Grosso do Sul (MS)": "America/Campo_Grande",

    "Pará (PA)": "America/Belem",
    "Amapá (AP)": "America/Belem",

    "Brasília - DF": "America/Sao_Paulo",

    "São Paulo (SP)": "America/Sao_Paulo",
    "Minas Gerais (MG)": "America/Sao_Paulo",
    "Rio de Janeiro (RJ)": "America/Sao_Paulo",

    "Bahia (BA)": "America/Bahia",

    "Pernambuco (PE)": "America/Recife",
    "Ceará (CE)": "America/Fortaleza",

    "Fernando de Noronha": "America/Noronha",


    # Países
    "Portugal 🇵🇹": "Europe/Lisbon",
    "Inglaterra 🇬🇧": "Europe/London",
    "França 🇫🇷": "Europe/Paris",

    "Nova York 🇺🇸": "America/New_York",
    "Los Angeles 🇺🇸": "America/Los_Angeles",

    "Canadá 🇨🇦": "America/Toronto",

    "Japão 🇯🇵": "Asia/Tokyo",
    "China 🇨🇳": "Asia/Shanghai",

    "Austrália 🇦🇺": "Australia/Sydney",

    "Argentina 🇦🇷": "America/Argentina/Buenos_Aires",

    "Chile 🇨🇱": "America/Santiago",

    "México 🇲🇽": "America/Mexico_City"
}



# -----------------------------
# DATA E HORA
# -----------------------------


st.divider()

st.subheader("📅 Informações do agendamento")


data_escolhida = st.date_input(
    "Escolha a data:",
    value=date.today(),
    format="DD/MM/YYYY"
)


hora_escolhida = st.time_input(
    "Escolha o horário:",
    value=time(15,0)
)



# -----------------------------
# ORIGEM E DESTINO
# -----------------------------


st.divider()

st.subheader("🔄 Conversão")


origem = st.selectbox(
    "Horário informado pelo cliente:",
    locais.keys()
)


destino = st.selectbox(
    "Converter para:",
    locais.keys(),
    index=list(locais.keys()).index("Brasília - DF")
)



# -----------------------------
# CONVERSÃO
# -----------------------------


fuso_origem = pytz.timezone(
    locais[origem]
)


fuso_destino = pytz.timezone(
    locais[destino]
)



data_hora = datetime.combine(
    data_escolhida,
    hora_escolhida
)



# coloca o fuso da origem
horario_origem = fuso_origem.localize(
    data_hora
)



# converte
horario_destino = horario_origem.astimezone(
    fuso_destino
)



# -----------------------------
# RESULTADO
# -----------------------------


st.divider()

st.success(
    f"""
📍 Origem:
{origem}

📅 Data:
{horario_origem.strftime('%d/%m/%Y')}

🕒 Horário informado:
{horario_origem.strftime('%H:%M')}


➡️ Convertido para:

📍 {destino}

📅 Data:
{horario_destino.strftime('%d/%m/%Y')}

🕒 Horário:
{horario_destino.strftime('%H:%M')}
"""
)



# diferença

diferenca = (
    horario_destino.utcoffset()
    -
    horario_origem.utcoffset()
).total_seconds() / 3600



st.info(
    f"Diferença de horário: {diferenca:+.0f} horas"
)