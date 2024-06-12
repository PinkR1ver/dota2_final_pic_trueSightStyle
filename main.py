from PIL import Image, ImageDraw, ImageFont
import streamlit as st
from utils import *
import numpy as np
from io import BytesIO

if __name__ == '__main__':
    
    st.title('Final Graph Generate - True Sight Style')
    
    with st.sidebar:
        
        score_left = st.slider('Score Left', min_value=0, max_value=2, value=1, step=1)
        score_right = st.slider('Score Right', min_value=0, max_value=2, value=1, step=1)
        score_font_size = st.slider('Score Font Size', min_value=50, max_value=400, value=200, step=1)
        
        font_style = st.selectbox('Font Style', [
            'Arial Bold', 'Calibri Bold', 'Bahnschrift',
            'GrotesqueMTStd Bold',
        ])
        
        score_font_x_offset = st.slider('Score Font X Offset', min_value=-400, max_value=400, value=0, step=1)
        score_font_y_offset = st.slider('Score Font Y Offset', min_value=-400, max_value=400, value=0, step=1)

        bo5_font_size = st.slider('BO5 Font Size', min_value=5, max_value=200, value=50, step=1)
        
        bo5_font_x_offset = st.slider('BO5 Font X Offset', min_value=-400, max_value=400, value=0, step=1)
        bo5_font_y_offset = st.slider('BO5 Font Y Offset', min_value=-400, max_value=400, value=100, step=1) 
        
        left_team_logo_width = st.slider('Left Team Logo Width', min_value=50, max_value=500, value=300, step=1)
        left_team_logo_x_offset = st.slider('Left Team Logo X Offset', min_value=-800, max_value=800, value=-400, step=1)
        left_team_logo_y_offset = st.slider('Left Team Logo Y Offset', min_value=-800, max_value=800, value=-50, step=1)
        
        right_team_logo_width = st.slider('Right Team Logo Width', min_value=50, max_value=500, value=300, step=1)
        right_team_logo_x_offset = st.slider('Right Team Logo X Offset', min_value=-800, max_value=800, value=400, step=1)
        right_team_logo_y_offset = st.slider('Right Team Logo Y Offset', min_value=-800, max_value=800, value=0, step=1)

            
        
    width, height = 3840, 1600
    canva = Image.new('RGB', (width, height), color='white') 
    
    uploaded_file = st.file_uploader('Choose a background image', type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        
        try:
            background_image = Image.open(uploaded_file).convert('RGBA')
            background_image = background_image.resize((width, height))
            canva.paste(background_image, (0, 0))
        except Exception as e:
            st.error(e)
            background_image = Image.open('./pic/background.jpg').convert('RGBA')
            canva.paste(background_image, (0, 0))
            
    else:
        background_image = Image.open('./pic/background.jpg').convert('RGBA')
        canva.paste(background_image, (0, 0))
    
    canva_draw = ImageDraw.Draw(canva)
    
    match font_style:
        case 'Arial Bold':
            font_style = './font/ARIALBD.TTF'
        case 'Calibri Bold':
            font_style = './font/CALIBRIB.TTF'
        case 'Bahnschrift':
            font_style = './font/BAHNSCHRIFT.TTF'
        case 'GrotesqueMTStd Bold':
            font_style = './font/GrotesqueMTStd-Bold.OTF'
            
    font = ImageFont.truetype(font_style, score_font_size)
    score_text = f'{score_left}   {score_right}'
    
    text_ascent, text_descent = font.getmetrics()
    (text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(score_text)
    
    position = ((width - text_width) // 2, (height - text_ascent - text_descent) // 2)
    position = (position[0] + score_font_x_offset, position[1] + score_font_y_offset)
    
    canva_draw.text(position, score_text, font=font, fill='white')
    
    text = '-'
    text_ascent, text_descent = font.getmetrics()
    (text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(text)
    
    position = ((width - text_width) // 2, (height - text_ascent - text_descent) // 2)
    position = (position[0] + score_font_x_offset, position[1] + score_font_y_offset)
    
    canva_draw.text(position, text, font=font, fill='white')
    
    text = 'BO5'
    font = ImageFont.truetype(font_style, bo5_font_size)
    
    text_ascent, text_descent = font.getmetrics()
    (text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(text)
    
    position = ((width - text_width - text_offset_x) // 2,  height // 2)
    position = (position[0] + bo5_font_x_offset, position[1] + bo5_font_y_offset)
    
    canva_draw.text(position, text, font=font, fill='white')
    
    uploaded_file = st.file_uploader('Choose a left team logo', type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
            
            try:
                
                left_team_logo = Image.open(uploaded_file)
                logo_width = left_team_logo_width
                left_team_logo = logo_style_transform_white(left_team_logo, logo_width)
                logo_height, logo_width = left_team_logo.size
                left_team_logo_center_x = logo_width // 2
                left_team_logo_center_y = logo_height // 2
            
            except Exception as e:
                
                st.error(e)
                
                left_team_logo = Image.open('./pic/left_team_logo.png')
                logo_width = left_team_logo_width
                left_team_logo = logo_style_transform_white(left_team_logo, logo_width)
                logo_height, logo_width = left_team_logo.size
                left_team_logo_center_x = logo_width // 2
                left_team_logo_center_y = logo_height // 2
                
    else:
        
        left_team_logo = Image.open('./pic/left_team_logo.png')
        logo_width = left_team_logo_width
        left_team_logo = logo_style_transform_white(left_team_logo, logo_width)
        logo_height, logo_width = left_team_logo.size
        left_team_logo_center_x = logo_width // 2
        left_team_logo_center_y = logo_height // 2
        
    left_logo_position = (width // 2 - left_team_logo_center_x, height // 2 - left_team_logo_center_y)
    left_logo_position = (left_logo_position[0] + left_team_logo_x_offset, left_logo_position[1] + left_team_logo_y_offset)
    
    canva.paste(left_team_logo, left_logo_position, left_team_logo)
    
    uploaded_file = st.file_uploader('Choose a right team logo', type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        
        try:
            
            right_team_logo = Image.open(uploaded_file)
            logo_width = right_team_logo_width
            right_team_logo = logo_style_transform_white(right_team_logo, logo_width)
            logo_height, logo_width = right_team_logo.size
            right_team_logo_center_x = logo_width // 2
            right_team_logo_center_y = logo_height // 2
            
        except Exception as e:
            
            st.error(e)
            
            right_team_logo = Image.open('./pic/right_team_logo.png')
            logo_width = right_team_logo_width
            right_team_logo = logo_style_transform_white(right_team_logo, logo_width)
            logo_height, logo_width = right_team_logo.size
            right_team_logo_center_x = logo_width // 2
            right_team_logo_center_y = logo_height // 2
            
    else:
            
            right_team_logo = Image.open('./pic/right_team_logo.png')
            logo_width = right_team_logo_width
            right_team_logo = logo_style_transform_white(right_team_logo, logo_width)
            logo_height, logo_width = right_team_logo.size
            right_team_logo_center_x = logo_width // 2
            right_team_logo_center_y = logo_height // 2
            
    right_logo_position = (width // 2 - right_team_logo_center_x, height // 2 - right_team_logo_center_y)
    right_logo_position = (right_logo_position[0] + right_team_logo_x_offset, right_logo_position[1] + right_team_logo_y_offset)
    
    canva.paste(right_team_logo, right_logo_position, right_team_logo)
    
    st.image(canva)
    
    buf = BytesIO()
    canva.save(buf, format='png')
    byte_im = buf.getvalue()
    
    st.download_button('Download Image', byte_im, file_name='final_graph.png', mime='image/png')
        