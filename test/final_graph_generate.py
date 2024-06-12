from PIL import Image, ImageDraw, ImageFont
from logo_style_transform_white import *

width, height = 3840, 1600

canvas = Image.new('RGB', (width, height), color='white')  # 背景颜色设置为白色

background_image_path = './background.jpg'
background_image = Image.open(background_image_path).convert('RGBA')

background_image_resized = background_image.resize((width, height))

canvas.paste(background_image_resized, (0, 0))


font_size = 200  # 字体大小
font = ImageFont.truetype('./GrotesqueMTStd-Bold.OTF', font_size)

text_1 = '2   2'

text_ascent, text_descent = font.getmetrics()
(text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(text_1)
position_1 = ((width - text_width) // 2, (height - text_ascent - text_descent) // 2)

text_2 = '-'
text_ascent, text_descent = font.getmetrics()
(text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(text_2)
position_2 = ((width - text_width) // 2, (height - text_baseline - text_ascent) // 2)

canvas_draw = ImageDraw.Draw(canvas)
canvas_draw.text(position_1, text_1, font=font, fill='white')
canvas_draw.text(position_2, text_2, font=font, fill='white')

font_size = 50
font = ImageFont.truetype('./GrotesqueMTStd-Bold.OTF', font_size)

text_3 = 'BO5'
text_ascent, text_descent = font.getmetrics()
(text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(text_3)
position_3 = ((width - text_width - text_offset_x) // 2,  height // 2 + 50)

canvas_draw.text(position_3, text_3, font=font, fill='white')

left_team_logo_path = './team_turtle.png'
logo_width = 300

left_team_logo = logo_style_transform_white(left_team_logo_path, logo_width)
logo_height, logo_width = left_team_logo.size
left_team_logo_center_x = logo_width // 2
left_team_logo_center_y = logo_height // 2

logo_position = (width // 2 - left_team_logo_center_x, height // 2 - left_team_logo_center_y)
# logo_position = (logo_position[0] - 300, logo_position[1] - 100)

canvas.paste(left_team_logo, logo_position, left_team_logo)

right_team_logo_path = './azure_ray.png'
# logo_width = 300

right_team_logo = logo_style_transform_white(right_team_logo_path, logo_width)
logo_height, logo_width = right_team_logo.size
left_team_logo_center_x = logo_width // 2
left_team_logo_center_y = logo_height // 2

logo_position = (width // 2 - left_team_logo_center_x, height // 2 - left_team_logo_center_y)
# logo_position = (logo_position[0] + 300, logo_position[1] - 100)

canvas.paste(right_team_logo, logo_position, right_team_logo)

canvas.save('canvas.png')