
from PIL import Image, ImageDraw, ImageFont
import os
import random

class DrawScreen:

    def __init__(self):
        self.green_color = (40,191,132,255)
        self.red_color = (221,77,108,255)
        self.orange_color = (212,174,9,255)


    def drawscreen_test(self):

        res = -2.99
        type = "short"
        entry = "123"
        take = "58,069"
        coin_name = "BTCUSDT"
        leverage = "3"

        coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",240)
        coin_font2 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",220)
        coin_font3 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",200)
        type_font  = ImageFont.truetype("main/fonts/Klein-Bold.otf",230)
        type_font1  = ImageFont.truetype("main/fonts/Klein-Bold.otf",210)
        leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",220)
        res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",440)
        phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",190)
        usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",460)
        plus_phont  = ImageFont.truetype("main/fonts/Clonoid.ttf",360)


        if res > 0: 
            image = Image.open("main/images/bg_green.png")
            drawer = ImageDraw.Draw(image)

            res = str(res)
            if len(str(res).replace('-','')) > 7:
                if '.' in res: 
                    split_s = res.split('.')
                    if len(split_s[0]) > 6: 
                        res = split_s[0][:6]
                    else: 
                        res = round(float(res), 6 - len(split_s[0]))
                        if res.is_integer(): 
                            res = int(res)


          
            if len(coin_name) == 4:
                drawer.text((520, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((500, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((370, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((250, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((200, 1675), coin_name, font=coin_font2, fill='white')

            elif len(coin_name) == 9:
                drawer.text((200, 1675), coin_name, font=coin_font3, fill='white')


            if type == 'short':
                drawer.text((1640, 1700), "Шорт", font=type_font1, fill=self.red_color)
            else: 
                drawer.text((1650, 1680), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((2500, 1730), str(leverage) + 'X', font=leverage_font, fill="white")



            if len(str(res).replace('-', '')) == 3:
                if '.' in str(res):
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1200, 2140), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1320, 2140), 'USDT', font=usdt_font, fill=self.green_color)

            if len(str(res).replace('-', '')) == 4:
                if '.' in str(res):
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1490, 2140), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1560, 2140), 'USDT', font=usdt_font, fill=self.green_color)



            if len(str(res).replace('-', '')) == 5:
                if '.' in str(res):
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1750, 2140), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1760, 2140), 'USDT', font=usdt_font, fill=self.green_color)

            if len(str(res).replace('-', '')) == 6:

                if '.' in str(res):
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((1950, 2140), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((2010, 2140), 'USDT', font=usdt_font, fill=self.green_color)

            if len(str(res).replace('-', '')) == 7:
                if '.' in str(res):
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((2170, 2140), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((240, 2130), '+', font=plus_phont, fill=self.green_color)
                    drawer.text((570, 2070), (str(res)), font=res_font, fill=self.green_color)
                    drawer.text((2200, 2140), 'USDT', font=usdt_font, fill=self.green_color)
            

            drawer.text((1800, 3030), str(take), font=phont_2, fill="white")
            drawer.text((2000, 3350), str(entry), font=phont_2, fill="white")

        else: 
            image = Image.open("main/images/bg_red.png")
            drawer = ImageDraw.Draw(image)

            res = str(res)
            if len(str(res).replace('-','')) > 7:
                if '.' in res: 
                    split_s = res.split('.')
                    if len(split_s[0]) > 6: 
                        res = split_s[0][:6]
                    else: 
                        res = round(float(res), 6 - len(split_s[0]))
                        if res.is_integer(): 
                            res = int(res)


          
            if len(coin_name) == 4:
                drawer.text((520, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((500, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((370, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((250, 1675), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((200, 1675), coin_name, font=coin_font2, fill='white')

            elif len(coin_name) == 9:
                drawer.text((200, 1675), coin_name, font=coin_font3, fill='white')


            if type == 'short':
                drawer.text((1640, 1700), "Шорт", font=type_font1, fill=self.red_color)
            else: 
                drawer.text((1650, 1680), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((2600, 1730), str(leverage) + 'X', font=leverage_font, fill="white")



            if len(str(res).replace('-', '')) == 3:
                if '.' in str(res):
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1100, 2140), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1260, 2140), 'USDT', font=usdt_font, fill=self.red_color)

            if len(str(res).replace('-', '')) == 4:
                if '.' in str(res):
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1350, 2140), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1500, 2140), 'USDT', font=usdt_font, fill=self.red_color)


            if len(str(res).replace('-', '')) == 5:
                if '.' in str(res):
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1650, 2140), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1570, 2140), 'USDT', font=usdt_font, fill=self.red_color)

            if len(str(res).replace('-', '')) == 6:
                if '.' in str(res):
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((1870, 2140), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((2050, 2140), 'USDT', font=usdt_font, fill=self.red_color)

            if len(str(res).replace('-', '')) == 7:
                if '.' in str(res):
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((2050, 2140), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((240, 2070), (str(res)), font=res_font, fill=self.red_color)
                    drawer.text((2060, 2140), 'USDT', font=usdt_font, fill=self.red_color)
            

            drawer.text((1800, 3030), str(take), font=phont_2, fill="white")
            drawer.text((2000, 3350), str(entry), font=phont_2, fill="white")

        image = image.convert('RGB')

        image.show()



    
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        

DrawScreen_Bingx = DrawScreen()
DrawScreen_Bingx.drawscreen_test()