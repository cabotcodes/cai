mkdir -p ~/.streamlit/
echo "[theme]
primaryColor = ‘#8BB1C5’
backgroundColor = ‘#FFFFFF’
secondaryBackgroundColor = ‘#F0F2F6’
textColor= ‘#31333F’
font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml