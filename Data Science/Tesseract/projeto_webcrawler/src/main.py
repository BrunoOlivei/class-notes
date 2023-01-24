import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas

URL = "https://www.nike.com.br/snkrs/calendario"
page = requests.get(URL, headers={"User-Agent": "Requests"})

soup = BeautifulSoup(page.content, 'html.parser')

job_elements = soup.find_all('h2', class_="Typographystyled__StyledHeading-sc-1h4c8w0-1 gnpgNR GridProductCardstyled__ProductNickname-sc-1br37gm-7 hOzsLy")

tenis_disponiveis = [element.text for element in job_elements]

c = canvas.Canvas("tenis_disponiveis.pdf")
c.setFont("Helvetica", 12)
c.drawString(100, 750, "TÊNIS DISPONÍVEIS")

horizontal = 100
vertical = 700

for item in tenis_disponiveis:
    c.drawString(horizontal, vertical, item)
    vertical -= 20

c.showPage()
c.save()
