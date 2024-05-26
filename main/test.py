
from PIL import Image, ImageDraw, ImageFont
import os


class DrawScreen:

    def __init__(self):
        self.leverage_font  = ImageFont.truetype("main/fonts/FontspringDEMOneuevektorabook.ttf",30)
        self.coin_font = ImageFont.truetype("main/fonts/DMCAPS.TTF",30)
        self.res_font = ImageFont.truetype("main/fonts/DMCAPS.TTF",95)
        self.prices = ImageFont.truetype("main/fonts/DMCAPS.TTF",35)
        self.percent = ImageFont.truetype("main/fonts/GolosTextRegular.ttf",95)
        self.srok_font = ImageFont.truetype("main/fonts/GenerischSansSemiBold.ttf",30)
        self.green_color = (40,191,132,255)
        self.red_color = (221,77,108,255)
        self.orange_color = (212,174,9,255)
        self.sell_buy_font = ImageFont.truetype("main/fonts/FFNortRegular.ttf",25)

    def drawscreen_test(self, res, chat_id):

        res = str(res)
        type = "long"
        entry = "123"
        take = "1234"
        coin_name = "BTCUSDT"
        leverage = "2"

        if res[0] != '-': 
            if len(str(res).replace('.', '')) > 5: 
                if '.' in str(res):
                    res  = str(res)[:6]
                else: 
                    res  = str(res)[:5]
            
            if res[-1] == '.': 
                res = res[:-1]
            else:
                for i in range(len(res)):
                    if res[-1] == '0' and '.' in res:
                        res = res[:-1]
                if res[-1] == '.': 
                    res = res[:-1]

            coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",60)
            type_font  = ImageFont.truetype("main/fonts/tghaidogroteskextrabold.otf",52)
            leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",50)
            res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",180)
            phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",50)
            usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",190)
            plus_phont  = ImageFont.truetype("main/fonts/Clonoid.ttf",145)
            image = Image.open("main/images/bg4_2.png")
            drawer = ImageDraw.Draw(image)


            drawer.text((80, 550), '+', font = plus_phont, fill= self.green_color)

            if len(coin_name) == 4:
                drawer.text((200, 415), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((165, 415), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((120, 415), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((85, 415), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((55, 415), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 9:
                drawer.text((30, 415), coin_name, font=coin_font, fill='white')


            if type == 'short':
                drawer.text((415, 403), "Шорт", font=type_font, fill=self.red_color)
            else: 
                drawer.text((423, 403), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((640, 432), str(leverage) + 'X', font=leverage_font, fill="white")

            if len(str(res).replace('.', '')) - 1 == 4:   
                print('4') 
                drawer.text((205, 520), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((750, 545), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((700, 545), 'USDT', font=usdt_font, fill=self.green_color)

            elif len(str(res).replace('.', '')) - 1 == 5:
                print('5')
                drawer.text((205, 520), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((820, 545), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((765, 545), 'USDT', font=usdt_font, fill=self.green_color)

            elif len(str(res).replace('.', '')) - 1 == 2:
                print('2')
                drawer.text((205, 520), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((565, 545), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((520, 545), 'USDT', font=usdt_font, fill=self.green_color)

            elif len(str(res).replace('.', '')) - 1 == 1:
                print('1')
                drawer.text((205, 520), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((485, 545), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((455, 545), 'USDT', font=usdt_font, fill=self.green_color)

            elif len(str(res).replace('.', '')) - 1 < 1:
                print('<1')
                drawer.text((205, 520), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((420, 545), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((370, 545), 'USDT', font=usdt_font, fill=self.green_color)

            elif len(str(res).replace('.', '')) - 1 == 3:
                print('3')
                drawer.text((205, 520), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((650, 545), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((600, 545), 'USDT', font=usdt_font, fill=self.green_color)

            drawer.text((445, 753), str(take), font=phont_2, fill="white")
            drawer.text((500, 833), str(entry), font=phont_2, fill="white")

        else: 
            coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",130)
            type_font  = ImageFont.truetype("main/fonts/tghaidogroteskextrabold.otf",110)
            leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",110)
            res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",325)
            phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",100)
            usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",360)
            image = Image.open("main/images/b2.png")
            drawer = ImageDraw.Draw(image)
            if len(str(res)) > 6: 
                res  = str(res)[:7]

            if len(coin_name) == 4:
                drawer.text((450, 925), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((350, 925), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((280, 925), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((190, 925), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((120, 925), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 9:
                drawer.text((60, 925), coin_name, font=coin_font, fill='white')



            if type == 'short':
                drawer.text((930, 905), "Шорт", font=type_font, fill=self.red_color)
            else: 
                drawer.text((930, 905), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((1450, 965), str(leverage) + 'X', font=leverage_font, fill="white")
            
            if len(str(res).replace('.', ''))- 1 == 4:      
                drawer.text((150, 1150), (str(res)), font=res_font, fill=self.red_color)
                if '.' in str(res):
                    drawer.text((1200, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                else: 
                    drawer.text((1100, 1190), 'USDT', font=usdt_font, fill=self.red_color)
            elif len(str(res).replace('.', '')) - 1 == 5:
                drawer.text((150, 1150), (str(res)), font=res_font, fill=self.red_color)
                if '.' in str(res):
                    drawer.text((1370, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((1280, 1190), 'USDT', font=usdt_font, fill=self.red_color)

            elif len(str(res).replace('.', '')) - 1 == 6:
                drawer.text((150, 1150), (str(res)), font=res_font, fill=self.red_color)
                if '.' in str(res):
                    drawer.text((1550, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((1450, 1190), 'USDT', font=usdt_font, fill=self.red_color)
            elif len(str(res).replace('.', '')) - 1 == 7:
                drawer.text((150, 1150), (str(res)), font=res_font, fill=self.red_color)
                if '.' in str(res):
                    drawer.text((1700, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((1620, 1190), 'USDT', font=usdt_font, fill=self.red_color)
            elif len(str(res).replace('.', '')) - 1 <= 3:
                drawer.text((150, 1150), (str(res)), font=res_font, fill=self.red_color)
                if '.' in str(res):
                    drawer.text((1000, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                else:
                    drawer.text((900, 1190), 'USDT', font=usdt_font, fill=self.red_color)

            drawer.text((970, 1690), str(take), font=phont_2, fill="white")

            drawer.text((1100, 1865), str(entry), font=phont_2, fill="white")

        image = image.convert('RGB')

        image.show(f'main/images/{chat_id}_img.jpg')




    
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        

DrawScreen_Bingx = DrawScreen()
DrawScreen_Bingx.drawscreen_test('123221232.24', '4245367')