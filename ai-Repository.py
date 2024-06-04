import os
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mp

# Parameters
width, height = 150, 150
background_color = (1, 1, 1)  # สีพื้นหลังเข้ม
text_color = (0, 255, 128)  # สีเขียว ChatGPT
font_size = 13
 

text = ("#AIEverEvolving\nWorld is constantly\nevolving.\nI am an AI, \nready to learn and \ngrow with every challenge")
cursor_color = (0, 255, 128)  # สีเขียว ChatGPT
cursor_width = 2

# Load a font
font_path = "Roboto-Regular.ttf"  # ตรวจสอบว่าไฟล์ฟอนต์นี้อยู่ในไดเรกทอรีเดียวกันหรือให้พาธที่ถูกต้อง
try:
    font = ImageFont.truetype(font_path, 42)
except IOError:
    font = ImageFont.load_default()
# Calculate text size and position
image = Image.new('RGB', (width, height), color=background_color)
draw = ImageDraw.Draw(image)
text_position = (8, 50) 
# Calculate text size using textbbox
bbox = draw.textbbox(text_position, text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
# Create frames
frames = []
cursor_visible = False
frame_count = 12  # จำนวนเฟรมเพื่อให้วิดีโอยาวกว่า 3 วินาที (12 เฟรมที่ 0.25 วินาทีต่อเฟรมจะเท่ากับ 3 วินาที)
for i in range(frame_count):  # จำนวนเฟรม
    frame = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(frame)
    draw.text(text_position, text, fill=text_color, font=font)
    
    if cursor_visible:
        cursor_position = (text_position[0] + text_width + 5, text_position[1] + text_height)
        draw.line([cursor_position, (cursor_position[0], cursor_position[1] - font_size)], fill=cursor_color, width=cursor_width)

    frames.append(frame)
    cursor_visible = not cursor_visible
image = Image.new('RGB', (width, height), color=background_color)
# Initialize ImageDraw
draw = ImageDraw.Draw(image)
# Add text to image
draw.text(text_position, text, fill=text_color, font=font)
# บันทึกภาพเป็นไฟล์ .png
output_path = "AI_Announcement.png"
image.save(output_path, optimize=True, quality=10)
# Save frames as a GIF with high compression
gif_path = "AI_Announcement.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=250, loop=0, optimize=True)  # 250 ms ต่อเฟรม

# Convert GIF to MP4 using moviepy
gif_clip = mp.VideoFileClip(gif_path)
mp4_path = os.path.join(os.path.expanduser("~"), "Documents", "AI_Announcement.mp4")
gif_clip.write_videofile(mp4_path, codec='libx264', fps=4)  # 4 เฟรมต่อวินาที (12 เฟรมจะยาว 3 วินาที)

mp4_path

