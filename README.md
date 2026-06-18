# 🌎 Conversor de Fuso Horário

Um aplicativo web interativo para converter horários entre diferentes locais do Brasil e do mundo, perfeito para agendar reuniões com clientes em diferentes zonas de tempo.

## 📋 Características

✅ Converte horários entre todos os estados brasileiros  
✅ Suporte para principais países do mundo  
✅ Exibe horário atual em Brasília  
✅ Interface intuitiva e responsiva  
✅ Datas em formato brasileiro (dd/mm/yyyy)  
✅ Cálculo automático de diferença entre fusos horários

## 🚀 Como Usar

### Instalação

1. Clone ou baixe o projeto:

```bash
git clone <seu-repositorio>
cd Fuso
```

2. Crie um ambiente virtual (opcional mas recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando o Aplicativo

```bash
streamlit run fuso.py
```

O aplicativo abrirá em `http://localhost:8501/`

## 📦 Dependências

- **streamlit** - Framework para criar a interface web
- **pytz** - Biblioteca para manipulação de fusos horários
- **babel** - Formatação de datas em português

Veja `requirements.txt` para a lista completa.

## 📍 Locais Suportados

### Estados Brasileiros

- Acre (AC)
- Amazonas (AM)
- Roraima (RR)
- Rondônia (RO)
- Mato Grosso (MT)
- Mato Grosso do Sul (MS)
- Pará (PA)
- Amapá (AP)
- Brasília - DF
- São Paulo (SP)
- Minas Gerais (MG)
- Rio de Janeiro (RJ)
- Bahia (BA)
- Pernambuco (PE)
- Ceará (CE)
- Fernando de Noronha

### Países

- 🇵🇹 Portugal
- 🇬🇧 Inglaterra
- 🇫🇷 França
- 🇺🇸 Nova York
- 🇺🇸 Los Angeles
- 🇨🇦 Canadá
- 🇯🇵 Japão
- 🇨🇳 China
- 🇦🇺 Austrália
- 🇦🇷 Argentina
- 🇨🇱 Chile
- 🇲🇽 México

## 📖 Como Funciona

1. **Brasília - Agora**: Exibe o horário atual em Brasília
2. **Consultar Data e Horário**: Escolha uma data e hora específica
3. **Conversor**: Selecione a origem e o destino para converter o horário
4. **Resultado**: Veja a conversão com a diferença de fusos horários

## 🎨 Interface

A aplicação oferece:

- Métrica em tempo real do horário de Brasília
- Seletor de data com formato brasileiro
- Seletor de horário
- Conversor interativo entre locais
- Exibição clara da diferença entre fusos

## 🔧 Personalização

Você pode adicionar novos estados ou países editando o dicionário `locais` no arquivo `fuso.py`:

```python
locais = {
    "Nome do Local": "Timezone_IANA",
    # ...
}
```

Consulte [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) para encontrar o timezone correto.

## 📝 Licença

Este projeto é de código aberto e pode ser usado livremente.

## 👨‍💻 Autor

Desenvolvido como ferramenta para agendamento internacional.

---

**Dúvidas?** Abra uma issue ou entre em contato! 🚀
