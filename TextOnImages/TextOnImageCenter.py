from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("R.jpg")

w, h = my_image.size

print(w,h)



title_font = ImageFont.truetype('IslandMoments-Regular.ttf', 100)

title_text = "AwiAi"

image_editable = ImageDraw.Draw(my_image)

wf, hf = image_editable.textsize(title_text, title_font)

print(w,"x",h," : ",wf,"x",hf)

fontsize=100

title_font = ImageFont.truetype('IslandMoments-Regular.ttf', 100)

image_editable.text(((w-wf)/2 , (h-hf)/2), title_text, (34, 201, 188), font=title_font)

my_image.save("result1.jpg")
