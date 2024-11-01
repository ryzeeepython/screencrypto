
from PIL import Image, ImageDraw, ImageFont
import os


class DrawScreen:

    def __init__(self):
        self.green_color = (40,191,132,255)
        self.red_color = (221,77,108,255)
        self.orange_color = (212,174,9,255)

    def add_comm(self, n):
        if len(str(n)) >= 4:
            if '.' in str(n): 
                n2 = str(n).split('.')
                k = n2[1]
                if len((n2)[0]) == 4: 
                    n2 = str(n2[0][0]) + ',' + str(n2[0][1:])
                elif len((n2)[0]) == 5: 
                    n2 = str(n2[0][:2]) + ',' + str(n2[0][2:])
                elif len((n2)[0]) == 6: 
                    n2 = str(n2[0][:3]) + ',' + str(n2[0][3:])
                elif len((n2)[0]) == 7: 
                    n2 = str(n2[0][0]) + ',' + str(n2[0][1:4]) + ',' + str(n2[0][4:])
                else: 
                    return n
                n2 = n2+ '.' + k

            else:
                n2 = str(n).split('.')
                if len((n2)[0]) == 4: 
                    n2 = str(n2[0][0]) + ',' + str(n2[0][1:])
                elif len((n2)[0]) == 5: 
                    n2 = str(n2[0][:2]) + ',' + str(n2[0][2:])
                elif len((n2)[0]) == 6: 
                    n2 = str(n2[0][:3]) + ',' + str(n2[0][3:])
                elif len((n2)[0]) == 7: 
                    n2 = str(n2[0][0]) + ',' + str(n2[0][1:4]) + ',' + str(n2[0][4:])
                else: 
                    return n
        else: 
            return n 
        return n2
    
    def shorten_res(self, n):
        n2 = str(n).replace('-', '')
        if '.' in n2: 
            n2 = n2.split('.')
            if len(n2[1]) >= 2 and len(n2[0]) < 5:
                n2 = round(float(str(n).replace('-', '')), 2)
            elif len(n2[1]) >= 2 and len(n2[0]) < 6:
                n2 = round(float(str(n).replace('-', '')), 1)
            else: 
                n2 = n2[0][:6]
        else: 
            if len(n2) > 6:  
                n2 = n2[:6]
        
        if str(n)[0] == '-': 
            n2 = '-' + str(n2)

        return n2

    def drawscreen_test(self):

        res = 5343.121212
        type = "short"
        entry = "123"
        take = "65122"
        coin_name = "BTCUSDTGH"
        leverage = "3"

        coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",140)
        coin_font2 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",130)
        coin_font3 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",120)
        type_font  = ImageFont.truetype("main/fonts/Klein-Bold.otf",130)
        type_font1  = ImageFont.truetype("main/fonts/Klein-Bold.otf",125)
        leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",120)
        phont_2  = ImageFont.truetype("main/fonts/Inter700.ttf",95)
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

            res = self.shorten_res(res)

          
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
                    drawer.text((200, 1230), '+', font=plus_phont_1, fill=self.green_color)
                    drawer.text((570, 1230), (str(res)), font=res_font_1, fill=self.green_color)
                    drawer.text((1070, 1290), 'USDT', font=usdt_font_1, fill=self.green_color)
                else:
                    drawer.text((200, 1230), '+', font=plus_phont_1, fill=self.green_color)
                    drawer.text((570, 1230), (str(res)), font=res_font_1, fill=self.green_color)
                    drawer.text((1140, 1290), 'USDT', font=usdt_font_1, fill=self.green_color)

            if len(str(res).replace('-', '')) == 4:
                if '.' in str(res):
                    drawer.text((200, 1230), '+', font=plus_phont_2, fill=self.green_color)
                    drawer.text((520, 1230), (str(res)), font=res_font_2, fill=self.green_color)
                    drawer.text((1130, 1290), 'USDT', font=usdt_font_2, fill=self.green_color)
                else:
                    drawer.text((140, 1230), '+', font=plus_phont_2, fill=self.green_color)
                    drawer.text((460, 1230), (str(res)), font=res_font_2, fill=self.green_color)
                    drawer.text((1160, 1290), 'USDT', font=usdt_font_2, fill=self.green_color)



            if len(str(res).replace('-', '')) == 5:
                if '.' in str(res):
                    drawer.text((140, 1230), '+', font=plus_phont_3, fill=self.green_color)
                    drawer.text((440, 1230), (str(res)), font=res_font_3, fill=self.green_color)
                    drawer.text((1200, 1280), 'USDT', font=usdt_font_3, fill=self.green_color)
                else:
                    drawer.text((110, 1200), '+', font=plus_phont_3, fill=self.green_color)
                    drawer.text((400, 1200), (str(res)), font=res_font_3, fill=self.green_color)
                    drawer.text((1220, 1250), 'USDT', font=usdt_font_3, fill=self.green_color)

            if len(str(res).replace('-', '')) == 6:

                if '.' in str(res):
                    drawer.text((120, 1230), '+', font=plus_phont_4, fill=self.green_color)
                    drawer.text((400, 1230), (str(res)), font=res_font_4, fill=self.green_color)
                    drawer.text((1270, 1280), 'USDT', font=usdt_font_4, fill=self.green_color)
                else:
                    drawer.text((110, 1230), '+', font=plus_phont_4, fill=self.green_color)
                    drawer.text((400, 1230), (str(res)), font=res_font_4, fill=self.green_color)
                    drawer.text((1380, 1280), 'USDT', font=usdt_font_4, fill=self.green_color)

            if len(str(res).replace('-', '')) == 7:
                if '.' in str(res):
                    drawer.text((160, 1230), '+', font=plus_phont_5, fill=self.green_color)
                    drawer.text((420, 1230), (str(res)), font=res_font_5, fill=self.green_color)
                    drawer.text((1320, 1270), 'USDT', font=usdt_font_5, fill=self.green_color)
                else:
                    drawer.text((160, 1230), '+', font=plus_phont_5, fill=self.green_color)
                    drawer.text((420, 1230), (str(res)), font=res_font_5, fill=self.green_color)
                    drawer.text((1380, 1270), 'USDT', font=usdt_font_5, fill=self.green_color)
            
            take = self.add_comm(take)
            entry = self.add_comm(entry)

            drawer.text((990, 1770), str(take), font=phont_2, fill="white")
            drawer.text((1200, 1955), str(entry), font=phont_2, fill="white")

        else: 
            image = Image.open("main/images/red_bg.png")
            drawer = ImageDraw.Draw(image)

            res = self.shorten_res(res)
          
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
                    drawer.text((250, 1210), (str(res)), font=res_font_1, fill=self.red_color)
                    drawer.text((1070-60, 1270), 'USDT', font=usdt_font_1, fill=self.red_color)
                else:
                    drawer.text((160, 1210), (str(res)), font=res_font_1, fill=self.red_color)
                    drawer.text((1070-60, 1270), 'USDT', font=usdt_font_1, fill=self.red_color)

            if len(str(res).replace('-', '')) == 4:
                if '.' in str(res):
                    drawer.text((200, 1220), (str(res)), font=res_font_2, fill=self.red_color)
                    drawer.text((1070-60, 1270), 'USDT', font=usdt_font_2, fill=self.red_color)
                else:
                    drawer.text((200, 1210), (str(res)), font=res_font_2, fill=self.red_color)
                    drawer.text((1160-60, 1260), 'USDT', font=usdt_font_2, fill=self.red_color)

            if len(str(res).replace('-', '')) == 5:
                if '.' in str(res):
                    drawer.text((140, 1210), (str(res)), font=res_font_3, fill=self.red_color)
                    drawer.text((1160-60, 1260), 'USDT', font=usdt_font_3, fill=self.red_color)
                else:
                    drawer.text((180, 1210), (str(res)), font=res_font_3, fill=self.red_color)
                    drawer.text((1230-60, 1260), 'USDT', font=usdt_font_3, fill=self.red_color)

            if len(str(res).replace('-', '')) == 6:

                if '.' in str(res):
                    drawer.text((140, 1210), (str(res)), font=res_font_3, fill=self.red_color)
                    drawer.text((1270-60, 1260), 'USDT', font=usdt_font_3, fill=self.red_color)
                else:
                    drawer.text((150, 1210), (str(res)), font=res_font_4, fill=self.red_color)
                    drawer.text((1330-60, 1260), 'USDT', font=usdt_font_4, fill=self.red_color)

            if len(str(res).replace('-', '')) == 7:
                if '.' in str(res):
                    drawer.text((140, 1210), (str(res)), font=res_font_4, fill=self.red_color)
                    drawer.text((1350-60, 1260), 'USDT', font=usdt_font_4, fill=self.red_color)
                else:
                    drawer.text((150, 1210), (str(res)), font=res_font_5, fill=self.red_color)
                    drawer.text((1330-60, 1245), 'USDT', font=usdt_font_5, fill=self.red_color)
            
            take = self.add_comm(take)
            entry = self.add_comm(entry)

            drawer.text((990, 1765), str(take), font=phont_2, fill="white")
            drawer.text((1200, 1950), str(entry), font=phont_2, fill="white")

        image = image.convert('RGB')

        image.show()



    
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        

DrawScreen_Bingx = DrawScreen()
DrawScreen_Bingx.drawscreen_test()