
from PIL import Image, ImageDraw, ImageFont
import os


class DrawScreen:

    def __init__(self):
        self.green_color = (40,191,132,255)
        self.red_color = (221,77,108,255)
        self.orange_color = (212,174,9,255)


    def drawscreen_test(self):

        res = 12.54
        type = "short"
        entry = "123"
        take = "58.069"
        coin_name = "BTCUSDT"
        leverage = "3"

        coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",140)
        coin_font2 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",130)
        coin_font3 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",120)
        type_font  = ImageFont.truetype("main/fonts/Klein-Bold.otf",130)
        type_font1  = ImageFont.truetype("main/fonts/Klein-Bold.otf",125)
        leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",120)
        phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",110)
        usdt_font_1 = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",360)
        plus_phont_1  = ImageFont.truetype("main/fonts/Clonoid.ttf",350)
        res_font_1  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",350)
        usdt_font_2 = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",320)
        plus_phont_2  = ImageFont.truetype("main/fonts/Clonoid.ttf",310)
        res_font_2  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",310)
        usdt_font_3 = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",300)
        plus_phont_3  = ImageFont.truetype("main/fonts/Clonoid.ttf",290)
        res_font_3  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",290)
        usdt_font_4 = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",285)
        plus_phont_4  = ImageFont.truetype("main/fonts/Clonoid.ttf",270)
        res_font_4  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",280)
        usdt_font_5 = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",265)
        plus_phont_5  = ImageFont.truetype("main/fonts/Clonoid.ttf",240)
        res_font_5  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",250)


        if res > 0: 
            image = Image.open("main/images/green_bg.png")
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
                drawer.text((350, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((270, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((230, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((185, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((140, 980), coin_name, font=coin_font2, fill='white')

            elif len(coin_name) == 9:
                drawer.text((130, 985), coin_name, font=coin_font3, fill='white')


            if type == 'short':
                drawer.text((990, 990), "Шорт", font=type_font1, fill=self.red_color)
            else: 
                drawer.text((1000, 990), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((1535, 1025), str(leverage) + 'X', font=leverage_font, fill="white")


            if len(str(res).replace('-', '')) == 3:
                if '.' in str(res):
                    drawer.text((200, 1200), '+', font=plus_phont_1, fill=self.green_color)
                    drawer.text((570, 1200), (str(res)), font=res_font_1, fill=self.green_color)
                    drawer.text((1070, 1260), 'USDT', font=usdt_font_1, fill=self.green_color)
                else:
                    drawer.text((200, 1200), '+', font=plus_phont_1, fill=self.green_color)
                    drawer.text((570, 1200), (str(res)), font=res_font_1, fill=self.green_color)
                    drawer.text((1140, 1260), 'USDT', font=usdt_font_1, fill=self.green_color)

            if len(str(res).replace('-', '')) == 4:
                if '.' in str(res):
                    drawer.text((200, 1200), '+', font=plus_phont_2, fill=self.green_color)
                    drawer.text((520, 1200), (str(res)), font=res_font_2, fill=self.green_color)
                    drawer.text((1130, 1260), 'USDT', font=usdt_font_2, fill=self.green_color)
                else:
                    drawer.text((140, 1200), '+', font=plus_phont_2, fill=self.green_color)
                    drawer.text((460, 1200), (str(res)), font=res_font_2, fill=self.green_color)
                    drawer.text((1160, 1260), 'USDT', font=usdt_font_2, fill=self.green_color)



            if len(str(res).replace('-', '')) == 5:
                if '.' in str(res):
                    drawer.text((140, 1200), '+', font=plus_phont_3, fill=self.green_color)
                    drawer.text((440, 1200), (str(res)), font=res_font_3, fill=self.green_color)
                    drawer.text((1200, 1250), 'USDT', font=usdt_font_3, fill=self.green_color)
                else:
                    drawer.text((110, 1200), '+', font=plus_phont_3, fill=self.green_color)
                    drawer.text((400, 1200), (str(res)), font=res_font_3, fill=self.green_color)
                    drawer.text((1220, 1250), 'USDT', font=usdt_font_3, fill=self.green_color)

            if len(str(res).replace('-', '')) == 6:

                if '.' in str(res):
                    drawer.text((120, 1200), '+', font=plus_phont_4, fill=self.green_color)
                    drawer.text((400, 1200), (str(res)), font=res_font_4, fill=self.green_color)
                    drawer.text((1270, 1250), 'USDT', font=usdt_font_4, fill=self.green_color)
                else:
                    drawer.text((110, 1200), '+', font=plus_phont_4, fill=self.green_color)
                    drawer.text((400, 1200), (str(res)), font=res_font_4, fill=self.green_color)
                    drawer.text((1380, 1250), 'USDT', font=usdt_font_4, fill=self.green_color)

            if len(str(res).replace('-', '')) == 7:
                if '.' in str(res):
                    drawer.text((160, 1200), '+', font=plus_phont_5, fill=self.green_color)
                    drawer.text((420, 1200), (str(res)), font=res_font_5, fill=self.green_color)
                    drawer.text((1320, 1240), 'USDT', font=usdt_font_5, fill=self.green_color)
                else:
                    drawer.text((160, 1200), '+', font=plus_phont_5, fill=self.green_color)
                    drawer.text((420, 1200), (str(res)), font=res_font_5, fill=self.green_color)
                    drawer.text((1380, 1240), 'USDT', font=usdt_font_5, fill=self.green_color)
            

            drawer.text((990, 1775), str(take), font=phont_2, fill="white")
            drawer.text((1200, 1960), str(entry), font=phont_2, fill="white")

        else: 
            image = Image.open("main/images/red_bg.png")
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
                drawer.text((350-60, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((270-60, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((230-60, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((185-60, 980), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((140-60, 980), coin_name, font=coin_font2, fill='white')

            elif len(coin_name) == 9:
                drawer.text((130-60, 985), coin_name, font=coin_font3, fill='white')


            if type == 'short':
                drawer.text((990-60, 990), "Шорт", font=type_font1, fill=self.red_color)
            else: 
                drawer.text((1000-60, 990), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((1535-60, 1025), str(leverage) + 'X', font=leverage_font, fill="white")

            if len(str(res).replace('-', '')) == 3:
                if '.' in str(res):
                    drawer.text((250, 1200), (str(res)), font=res_font_1, fill=self.red_color)
                    drawer.text((1070-60, 1260), 'USDT', font=usdt_font_1, fill=self.red_color)
                else:
                    drawer.text((160, 1200), (str(res)), font=res_font_1, fill=self.red_color)
                    drawer.text((1070-60, 1260), 'USDT', font=usdt_font_1, fill=self.red_color)

            if len(str(res).replace('-', '')) == 4:
                if '.' in str(res):
                    drawer.text((200, 1200), (str(res)), font=res_font_2, fill=self.red_color)
                    drawer.text((1070-60, 1250), 'USDT', font=usdt_font_2, fill=self.red_color)
                else:
                    drawer.text((200, 1200), (str(res)), font=res_font_2, fill=self.red_color)
                    drawer.text((1160-60, 1250), 'USDT', font=usdt_font_2, fill=self.red_color)

            if len(str(res).replace('-', '')) == 5:
                if '.' in str(res):
                    drawer.text((140, 1200), (str(res)), font=res_font_3, fill=self.red_color)
                    drawer.text((1160-60, 1250), 'USDT', font=usdt_font_3, fill=self.red_color)
                else:
                    drawer.text((180, 1200), (str(res)), font=res_font_3, fill=self.red_color)
                    drawer.text((1230-60, 1250), 'USDT', font=usdt_font_3, fill=self.red_color)

            if len(str(res).replace('-', '')) == 6:

                if '.' in str(res):
                    drawer.text((140, 1200), (str(res)), font=res_font_3, fill=self.red_color)
                    drawer.text((1270-60, 1250), 'USDT', font=usdt_font_3, fill=self.red_color)
                else:
                    drawer.text((150, 1200), (str(res)), font=res_font_4, fill=self.red_color)
                    drawer.text((1330-60, 1250), 'USDT', font=usdt_font_4, fill=self.red_color)

            if len(str(res).replace('-', '')) == 7:
                if '.' in str(res):
                    drawer.text((140, 1200), (str(res)), font=res_font_4, fill=self.red_color)
                    drawer.text((1350-60, 1250), 'USDT', font=usdt_font_4, fill=self.red_color)
                else:
                    drawer.text((150, 1200), (str(res)), font=res_font_5, fill=self.red_color)
                    drawer.text((1330-60, 1235), 'USDT', font=usdt_font_5, fill=self.red_color)
            
            
            drawer.text((990, 1775), str(take), font=phont_2, fill="white")
            drawer.text((1200, 1960), str(entry), font=phont_2, fill="white")

        image = image.convert('RGB')

        image.show()



    
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        

DrawScreen_Bingx = DrawScreen()
DrawScreen_Bingx.drawscreen_test()