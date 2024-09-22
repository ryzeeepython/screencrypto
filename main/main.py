
from PIL import Image, ImageDraw, ImageFont
import os
import asyncio
import config

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


    def is_int(self,str):
        try:
            int(str)
            return True
        except ValueError:
            return False
        
    def is_number(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False



    def drawscreen(self,data, chat_id):
        image = Image.open("main/images/image.png")
        drawer = ImageDraw.Draw(image)
        coin_name = data['pair']
        type = data['type']
        leverage = (data['leverage'])
        str_leverage = (data['leverage']) + 'x'
        entry = (data['entry_price'])
        take = (data['current_price'])
        
        if type == 'long': 
            res = (float(take) - float(entry)) / (float(entry) / 100) * int(leverage)

        else:
            res = (float(entry) - float(take)) / (float(entry) / 100) * int(leverage)


        if len(str(res)) > 5:
            new_res = ''
            list = []
            for i in range(5):
                list.append(str(res)[i])
            
            if list[-1] == '.':
                list.pop(-1)
                   
            for i in list:
                new_res += i 
            res = new_res

        #draw type
        if type == 'short':
            drawer.text((145, 185), "Продать", font=self.sell_buy_font, fill= self.red_color)
        elif type == 'long':
            drawer.text((145, 185), "Купить", font=self.sell_buy_font, fill= self.green_color)

        #draw leverage
        if len(str(str_leverage)) == 2:
            drawer.text((338, 182), str_leverage, font=self.leverage_font, fill='white')

        if len(str(str_leverage)) == 3:
            drawer.text((338, 182), str_leverage, font=self.leverage_font, fill='white')

        
        elif len(str(str_leverage)) == 4:
            drawer.text((334, 182), str_leverage, font=self.leverage_font, fill='white')

                
        elif len(str(str_leverage)) == 5:
            drawer.text((328, 182), str_leverage, font=self.leverage_font, fill='white')



        #draw coin_name 
        if len(str(coin_name)) == 6:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((570, 190), "Бессрочный", font=self.srok_font, fill='white')

        if len(str(coin_name)) == 7:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((590, 190), "Бессрочный", font=self.srok_font, fill='white')

        elif len(str(coin_name)) == 8:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((600, 190), "Бессрочный", font=self.srok_font, fill='white')

        elif len(str(coin_name)) == 9:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((610, 190), "Бессрочный", font=self.srok_font, fill='white')

        elif len(str(coin_name)) == 10:
            drawer.text((450, 185), coin_name, font=self.coin_font, fill='white')
            drawer.text((620, 190), "Бессрочный", font=self.srok_font, fill='white')

        #draw persent
        if len(str(res)) == 2:
            drawer.text((150, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((325, 215), "%", font=self.percent, fill=self.green_color) 

        elif len(str(res)) == 3:
            drawer.text((150, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((370, 215), "%", font=self.percent, fill=self.green_color) 

        elif len(str(res)) == 4:
            drawer.text((120, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((390, 215), "%", font=self.percent, fill=self.green_color) 

        elif len (str(res)) == 5:
            drawer.text((120, 220), f"+{res}", font=self.res_font, fill=self.green_color) 
            drawer.text((420, 215), "%", font=self.percent, fill=self.green_color) 

        #draw entry and take price
        drawer.text((410, 330), entry, font=self.prices, fill=self.orange_color) 
        drawer.text((410, 370), take, font=self.prices, fill=self.orange_color) 

        image = image.convert('RGB')
        image.save(f'main/images/{chat_id}_img.jpg')

    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        


class DrawScreen_Bingx:

    def __init__(self):
        self.red_color = (249,5,104)
        self.green_color = (0,253,154)

    def is_int(self,str):
        try:
            int(str)
            return True
        except ValueError:
            return False
        
    def is_number(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def drawscreen_test(self, data, chat_id):

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

        type = data['type']
        entry = (data['entry_price'])
        take = (data['current_price'])
        leverage = (data['leverage'])
        coin_name = data['pair']
        position = int(data['position'])

        if type == 'long': 
            b = float(entry)
            a = float(take) 

            percent = ((a/b-1) * int(leverage)) 
            res = int(position) * percent

        else:
            b = float(take)
            a = float(entry)
            percent = (((b/a-1) * 100) * int(leverage) /100) 
            res = int(position) * percent * -1

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
        image.save(f'main/images/{chat_id}_img.jpg')


    
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        