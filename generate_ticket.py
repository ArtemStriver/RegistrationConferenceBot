#!/usr/bin/env python3
"""
Метод для генерации билета на конференцию с именем пользователя, его email и персональным автаром.
"""

from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont


TEMPLATE_PATH = 'files/ticket_template.png'
FONT_PATH = "files/Roboto-Regular.ttf"
FONT_SIZE = 28

BLACK = (0, 0, 0, 255)
NAME_OFFSET = (270, 190)
EMAIL_OFFSET = (270, 245)

AVATAR_SIZE = 50
AVATAR_OFFSET = (75, 170)


def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK)

    response = requests.get(url=f'https://api.dicebear.com/6.x/identicon/png?seed={name}')
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)

    base.paste(avatar.resize((avatar.width // 2, avatar.height // 2)), AVATAR_OFFSET)

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file
