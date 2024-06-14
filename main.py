from PIL import Image, ImageDraw, ImageFont
import streamlit as st
from utils import *
import numpy as np
from io import BytesIO
import time

if __name__ == '__main__':
    
    st.title('🏆Final Score Chart Generate - True Sight Style')
    
    with st.sidebar:
        
        st.header('Image Detail Settings')
        
        style = st.selectbox('Style', [
            'Ti10'
        ])
        
        score_left = st.slider('Score Left', min_value=0, max_value=2, value=1, step=1)
        score_right = st.slider('Score Right', min_value=0, max_value=2, value=1, step=1)
        
        font_style = st.selectbox('Font Style', [
            'Arial Bold', 'Calibri Bold', 'Bahnschrift',
            'GrotesqueMTStd Bold',
        ], index=3)
        
        background_image = st.selectbox('Background Image', [
            '1', '2', '3'
        ], index=0)
        
        left_team_logo = st.selectbox('Left Team Logo', [
            'Team Spirit', 'Xtreme Gaming', 'Azure Ray',
            'Team Falcons', 'BetBoom', 'G2.iG'
        ], index=0)
        
        right_team_logo = st.selectbox('Right Team Logo', [
            'Team Spirit', 'Xtreme Gaming', 'Azure Ray', 
            'Team Falcons', 'BetBoom', 'G2.iG'
        ], index=1)
        
        
        match left_team_logo:
            case 'Team Spirit':
                left_team_logo_path = './pic/team_spirit.png'
                left_team_logo_x_offset_init = -400
                left_team_logo_y_offset_init = 0
                left_team_logo_size_init = 350
            case 'Xtreme Gaming':
                left_team_logo_path = './pic/xtreme_gaming.png'
                left_team_logo_x_offset_init = -400
                left_team_logo_y_offset_init = 0
                left_team_logo_size_init = 350
            case 'Azure Ray':
                left_team_logo_path = './pic/azure_ray.png'
                left_team_logo_x_offset_init = -400
                left_team_logo_y_offset_init = 0
                left_team_logo_size_init = 300
            case 'Team Falcons':
                left_team_logo_path = './pic/team_falcons.png'
                left_team_logo_x_offset_init = -600
                left_team_logo_y_offset_init = 0
                left_team_logo_size_init = 300
            case 'BetBoom':
                left_team_logo_path = './pic/bb.png'
                left_team_logo_x_offset_init = -500
                left_team_logo_y_offset_init = 0
                left_team_logo_size_init = 200
            case 'G2.iG':
                left_team_logo_path = './pic/g2_ig.png'
                left_team_logo_x_offset_init = -400
                left_team_logo_y_offset_init = 0
                left_team_logo_size_init = 300
                
        match right_team_logo:
            case 'Team Spirit':
                right_team_logo_path = './pic/team_spirit.png'
                right_team_logo_x_offset_init = 400
                right_team_logo_y_offset_init = 0
                right_team_logo_size_init = 350
            case 'Xtreme Gaming':
                right_team_logo_path = './pic/xtreme_gaming.png'
                right_team_logo_x_offset_init = 400
                right_team_logo_y_offset_init = 0
                right_team_logo_size_init = 350
            case 'Azure Ray':
                right_team_logo_path = './pic/azure_ray.png'
                right_team_logo_x_offset_init = 400
                right_team_logo_y_offset_init = 50
                right_team_logo_size_init = 300
            case 'Team Falcons':
                right_team_logo_path = './pic/team_falcons.png'
                right_team_logo_x_offset_init = 600
                right_team_logo_y_offset_init = 0
                right_team_logo_size_init = 300
            case 'BetBoom':
                right_team_logo_path = './pic/bb.png'
                right_team_logo_x_offset_init = 500
                right_team_logo_y_offset_init = 0
                right_team_logo_size_init = 200
            case 'G2.iG':
                right_team_logo_path = './pic/g2_ig.png'
                right_team_logo_x_offset_init = 400
                right_team_logo_y_offset_init = 0
                right_team_logo_size_init = 300
                
        match background_image:
            case '1':
                background_image_path = './pic/background1.jpg'
            case '2':
                background_image_path = './pic/background2.jpg'
            case '3':
                background_image_path = './pic/background3.jpg'
                
        
        with st.expander('Advanced Options'):
            
            score_font_size = st.slider('Score Font Size', min_value=1, max_value=400, value=200, step=1)
            
            score_font_x_offset = st.slider('Score Font X Offset', min_value=-400, max_value=400, value=0, step=1)
            score_font_y_offset = st.slider('Score Font Y Offset', min_value=-400, max_value=400, value=0, step=1)

            bo5_font_size = st.slider('BO5 Font Size', min_value=1, max_value=200, value=50, step=1)
            
            bo5_font_x_offset = st.slider('BO5 Font X Offset', min_value=-400, max_value=400, value=0, step=1)
            bo5_font_y_offset = st.slider('BO5 Font Y Offset', min_value=-400, max_value=400, value=100, step=1) 
            
            left_team_logo_size = st.slider('Left Team Logo Size', min_value=1, max_value=800, value=left_team_logo_size_init, step=1)
            left_team_logo_x_offset = st.slider('Left Team Logo X Offset', min_value=-800, max_value=800, value=left_team_logo_x_offset_init, step=1)
            left_team_logo_y_offset = st.slider('Left Team Logo Y Offset', min_value=-800, max_value=800, value=left_team_logo_y_offset_init, step=1)
            
            right_team_logo_size = st.slider('Right Team Logo Size', min_value=1, max_value=800, value=right_team_logo_size_init, step=1)
            right_team_logo_x_offset = st.slider('Right Team Logo X Offset', min_value=-800, max_value=800, value=right_team_logo_x_offset_init, step=1)
            right_team_logo_y_offset = st.slider('Right Team Logo Y Offset', min_value=-800, max_value=800, value=right_team_logo_y_offset_init, step=1)
    
    match style:
        case 'Ti10':
    
            progress_text = "Job Starting..."
            progress_bar = st.progress(0, text=progress_text)
                
            width, height = 3840, 1600
            canva = Image.new('RGB', (width, height), color='white') 
            
            
            with st.expander('Image personalization'):
                uploaded_file_background = st.file_uploader('Choose a background image', type=['jpg', 'jpeg', 'png'])
                uploaded_file_left_team_logo = st.file_uploader('Choose a left team logo', type=['jpg', 'jpeg', 'png'])
                uploaded_file_right_team_logo = st.file_uploader('Choose a right team logo', type=['jpg', 'jpeg', 'png'])
            
            
            if uploaded_file_background is not None:
                
                try:
                    background_image = Image.open(uploaded_file_background).convert('RGBA')
                    background_image = background_image.resize((width, height))
                    canva.paste(background_image, (0, 0))
                except Exception as e:
                    st.error(e)
                    background_image = Image.open(background_image_path).convert('RGBA')
                    background_image = background_image.resize((width, height))
                    canva.paste(background_image, (0, 0))
                    
            else:
                background_image = Image.open(background_image_path).convert('RGBA')
                background_image = background_image.resize((width, height))
                canva.paste(background_image, (0, 0))
            
            canva_draw = ImageDraw.Draw(canva)
            progress_bar.progress(10, text='Background Image Loaded...')
            
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
            progress_bar.progress(30, text='Score Text Loaded...')
            
            text = 'BO5'
            font = ImageFont.truetype(font_style, bo5_font_size)
            
            text_ascent, text_descent = font.getmetrics()
            (text_width, text_baseline), (text_offset_x, text_offset_y) = font.font.getsize(text)
            
            position = ((width - text_width - text_offset_x) // 2,  height // 2)
            position = (position[0] + bo5_font_x_offset, position[1] + bo5_font_y_offset)
            
            canva_draw.text(position, text, font=font, fill='white')
            progress_bar.progress(50, text='BO5 Text Loaded...')
            
            if uploaded_file_left_team_logo is not None:
                    
                    try:
                        
                        left_team_logo = Image.open(uploaded_file_left_team_logo)
                        logo_height = left_team_logo_size
                        left_team_logo = logo_style_transform_white(left_team_logo, logo_height, mode=2)
                        logo_width, logo_height = left_team_logo.size
                        left_team_logo_center_x = logo_width // 2
                        left_team_logo_center_y = logo_height // 2
                        left_team_logo_x_offset = -logo_width - 50
                        left_team_logo_y_offset = 0
                    
                    except Exception as e:
                        
                        st.error(e)
                        
                        left_team_logo = Image.open(left_team_logo_path)
                        logo_height = left_team_logo_size
                        left_team_logo = logo_style_transform_white(left_team_logo, logo_height, mode=2)
                        logo_width, logo_height = left_team_logo.size
                        left_team_logo_center_x = logo_width // 2
                        left_team_logo_center_y = logo_height // 2
                        
            else:
                
                left_team_logo = Image.open(left_team_logo_path)
                logo_height = left_team_logo_size
                left_team_logo = logo_style_transform_white(left_team_logo, logo_height, mode=2)
                logo_width, logo_height = left_team_logo.size
                left_team_logo_center_x = logo_width // 2
                left_team_logo_center_y = logo_height // 2
            
            
            left_logo_position = (width // 2 - left_team_logo_center_x, height // 2 - left_team_logo_center_y)
            left_logo_position = (left_logo_position[0] + left_team_logo_x_offset, left_logo_position[1] + left_team_logo_y_offset)
            
            canva.paste(left_team_logo, left_logo_position, left_team_logo)
            progress_bar.progress(70, text='Left Team Logo Loaded...')
            
            if uploaded_file_right_team_logo is not None:
                
                try:
                    
                    right_team_logo = Image.open(uploaded_file_right_team_logo)
                    logo_height = right_team_logo_size
                    right_team_logo = logo_style_transform_white(right_team_logo, logo_height, mode=2)
                    logo_width, logo_height= right_team_logo.size
                    right_team_logo_center_x = logo_width // 2
                    right_team_logo_center_y = logo_height // 2
                    right_team_logo_x_offset = logo_width + 50
                    right_team_logo_y_offset = 0
                    
                except Exception as e:
                    
                    st.error(e)
                    
                    right_team_logo = Image.open(right_team_logo_path)
                    logo_height = right_team_logo_size
                    right_team_logo = logo_style_transform_white(right_team_logo, logo_height, mode=2)
                    logo_width, logo_height= right_team_logo.size
                    right_team_logo_center_x = logo_width // 2
                    right_team_logo_center_y = logo_height // 2
                    
            else:
                    
                    right_team_logo = Image.open(right_team_logo_path)
                    logo_height = right_team_logo_size
                    right_team_logo = logo_style_transform_white(right_team_logo, logo_height, mode=2)
                    logo_width, logo_height = right_team_logo.size
                    right_team_logo_center_x = logo_width // 2
                    right_team_logo_center_y = logo_height // 2
                    
            right_logo_position = (width // 2 - right_team_logo_center_x, height // 2 - right_team_logo_center_y)
            right_logo_position = (right_logo_position[0] + right_team_logo_x_offset, right_logo_position[1] + right_team_logo_y_offset)
            
            canva.paste(right_team_logo, right_logo_position, right_team_logo)
            progress_bar.progress(90, text='Right Team Logo Loaded...')
            
            st.image(canva)
            progress_bar.progress(100, text='Final Graph Generated, Job Completed!')
            
            buf = BytesIO()
            canva.save(buf, format='png')
            byte_im = buf.getvalue()
            
            st.download_button('Download Image', byte_im, file_name='final_graph.png', mime='image/png')
            
            progress_bar.empty()
            
    with st.container():
        footer_info = [
            "❤️ Made by ",
            link("https://pinktalk.online", "JudeW"),
            br(),
            "⭐ Star this repo on ",
            link("https://github.com/PinkR1ver/dota2_final_pic_trueSightStyle", "GitHub"),
            br(),
            link("https://www.buymeacoffee.com/pinktalk", image('https://i.imgur.com/thJhzOO.png')),
        ]
        footer(footer_info)
                