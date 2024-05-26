
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


    def drawscreen_bingx(self, data, chat_id):

        type = data['type']
        position = int(data['position'])
        entry = (data['entry_price'])
        take = (data['current_price'])
        leverage = (data['leverage'])
        coin_name = data['pair']
        res_type = data['res_type']
        
        
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
        

        if res_type == 'В USDT(PNL)':
            res  = str(res)
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
                if len(str(res).replace('.', '')) > 7: 
                    if '.' in str(res):
                        res  = str(res)[:8]
                        print(res)
                    else: 
                        res  = str(res)[:7]
                
                if res[-1] == '.': 
                    res = res[:-1]
                else:
                    for i in range(len(res)):
                        if res[-1] == '0' and '.' in res:
                            res = res[:-1]
                    if res[-1] == '.': 
                        res = res[:-1]
                

                coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",130)
                type_font  = ImageFont.truetype("main/fonts/tghaidogroteskextrabold.otf",110)
                leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",110)
                res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",380)
                phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",100)
                usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",415)
                image = Image.open("main/images/b2.png")
                drawer = ImageDraw.Draw(image)

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
                    drawer.text((190, 1190), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((1310, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                    else: 
                        drawer.text((1265, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                elif len(str(res).replace('.', '')) - 1 == 5:
                    drawer.text((190, 1190), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((1550, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((1480, 1240), 'USDT', font=usdt_font, fill=self.red_color)

                elif len(str(res).replace('.', '')) - 1 == 6:
                    drawer.text((190, 1190), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((1720, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((1660, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                elif len(str(res).replace('.', '')) - 1 == 7:
                    drawer.text((150, 1150), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((1700, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((1620, 1190), 'USDT', font=usdt_font, fill=self.red_color)
                elif len(str(res).replace('.', '')) - 1 == 3:
                    drawer.text((190, 1190), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((1200, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((1100, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                
                elif len(str(res).replace('.', '')) - 1 == 2:
                    drawer.text((190, 1190), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((1000, 1240), 'USDT', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((900, 1240), 'USDT', font=usdt_font, fill=self.red_color)

                drawer.text((970, 1690), str(take), font=phont_2, fill="white")

                drawer.text((1100, 1865), str(entry), font=phont_2, fill="white")
        elif res_type == 'В процентах (ROI)': 
            res_text = res/(position/100)
            res = round(res_text, 2) 

            if res_text > 0: 
                coin_font_7 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",60)
                coin_font_8 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",55)
                coin_font_6 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",67)
                coin_font_9 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",52)
                coin_font_5 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",70)
                type_font  = ImageFont.truetype("main/fonts/tghaidogroteskextrabold.otf",53)
                leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",50)
                res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",175)
                phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",50)
                usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",195)
                plus_phont  = ImageFont.truetype("main/fonts/Clonoid.ttf",140)
                image = Image.open("main/images/per_bg_green.png")
                drawer = ImageDraw.Draw(image)

                if len(str(res).replace('.', '')) - 1> 6: 
                    if '.' in str(res):
                        res  = str(res)[:8]
                    else: 
                        res  = str(res)[:7]

                drawer.text((80, 525), '+', font = plus_phont, fill= self.green_color)
            

                if len(coin_name) == 5:
                    drawer.text((66, 408), coin_name, font=coin_font_5, fill='white')

                elif len(coin_name) == 6:
                    drawer.text((67, 410), coin_name, font=coin_font_6, fill='white')

                elif len(coin_name) == 7:
                    drawer.text((68, 415), coin_name, font=coin_font_7, fill='white')

                elif len(coin_name) == 8:

                    drawer.text((67, 420), coin_name, font=coin_font_8, fill='white')

                elif len(coin_name) == 9:
                    drawer.text((66, 423), coin_name, font=coin_font_9, fill='white')


                if type == 'short':
                    drawer.text((410, 406), "Шорт", font=type_font, fill=self.red_color)
                else: 
                    drawer.text((415, 406), "Лонг", font=type_font, fill=self.green_color)

                drawer.text((620, 435), (str(leverage)+'X'), font=leverage_font, fill="white")

                print(len(str(res).replace('.', ''))- 1)

                if len(str(res).replace('.', ''))- 1 == 4:    
                    drawer.text((210, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((740, 530), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((695, 531), '%', font=usdt_font, fill=self.green_color)

                elif len(str(res).replace('.', '')) - 1 == 5:
                    drawer.text((210, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((780, 530), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((740, 531), '%', font=usdt_font, fill=self.green_color)

                elif len(str(res).replace('.', '')) - 1 == 6:
                    drawer.text((210, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((895, 530), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((850, 531), '%', font=usdt_font, fill=self.green_color)

                
                elif len(str(res).replace('.', '')) - 1 == 2:
                    drawer.text((210, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((530, 529), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((485, 535), '%', font=usdt_font, fill=self.green_color)

                elif len(str(res).replace('.', '')) - 1 == 1:
                    drawer.text((230, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((500, 529), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((430, 535), '%', font=usdt_font, fill=self.green_color)

                elif len(str(res).replace('.', '')) - 1 == 3:
                    drawer.text((210, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((640, 529), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((615, 535), '%', font=usdt_font, fill=self.green_color)

                drawer.text((450, 753), str(take), font=phont_2, fill="white")
                drawer.text((495, 831), str(entry), font=phont_2, fill="white")
            else: 
                coin_font_7 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",58)
                coin_font_8 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",50)
                coin_font_6 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",67)
                coin_font_9 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",48)
                coin_font_5 = ImageFont.truetype("main/fonts/OkomitoBold.ttf",70)
                type_font  = ImageFont.truetype("main/fonts/tghaidogroteskextrabold.otf",53)
                leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",50)
                res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",175)
                phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",50)
                usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",195)
                plus_phont  = ImageFont.truetype("main/fonts/Clonoid.ttf",140)
                image = Image.open("main/images/per_bg_red.png")
                drawer = ImageDraw.Draw(image)

                if len(str(res).replace('.', '')) - 1> 6: 
                    if '.' in str(res):
                        res  = str(res)[:8]
                    else: 
                        res  = str(res)[:7]

                # drawer.text((80, 525), '+', font = plus_phont, fill= self.green_color)
            

                if len(coin_name) == 5:
                    drawer.text((66, 408), coin_name, font=coin_font_5, fill='white')

                elif len(coin_name) == 6:
                    drawer.text((67, 410), coin_name, font=coin_font_6, fill='white')

                elif len(coin_name) == 7:
                    drawer.text((68, 415), coin_name, font=coin_font_7, fill='white')

                elif len(coin_name) == 8:
                    drawer.text((65, 420), coin_name, font=coin_font_8, fill='white')

                elif len(coin_name) == 9:
                    drawer.text((60, 423), coin_name, font=coin_font_9, fill='white')


                if type == 'short':
                    drawer.text((375, 405), "Шорт", font=type_font, fill=self.red_color)
                else: 
                    drawer.text((380, 406), "Лонг", font=type_font, fill=self.green_color)

                drawer.text((590, 435), str(leverage), font=leverage_font, fill="white")

                print(len(str(res).replace('.', ''))- 1)

                if len(str(res).replace('.', ''))- 1 == 4:    
                    drawer.text((80, 510), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((550, 529), '%', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((520, 535), '%', font=usdt_font, fill=self.red_color)


                elif len(str(res).replace('.', '')) - 1 == 5:
                    drawer.text((80, 510), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((660, 529), '%', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((615, 535), '%', font=usdt_font, fill=self.red_color)


                elif len(str(res).replace('.', '')) - 1 == 6:
                    drawer.text((80, 510), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((700, 529), '%', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((650, 535), '%', font=usdt_font, fill=self.red_color)

                
                elif len(str(res).replace('.', '')) - 1 == 2:
                    drawer.text((80, 510), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((420, 529), '%', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((400, 535), '%', font=usdt_font, fill=self.red_color)

                elif len(str(res).replace('.', '')) - 1 == 1:
                    drawer.text((80, 510), (str(res)), font=res_font, fill=self.green_color)
                    if '.' in str(res):
                        drawer.text((500, 529), '%', font=usdt_font, fill=self.green_color)
                    else:
                        drawer.text((430, 535), '%', font=usdt_font, fill=self.green_color)

                elif len(str(res).replace('.', '')) - 1 == 3:
                    drawer.text((80, 510), (str(res)), font=res_font, fill=self.red_color)
                    if '.' in str(res):
                        drawer.text((500, 529), '%', font=usdt_font, fill=self.red_color)
                    else:
                        drawer.text((450, 535), '%', font=usdt_font, fill=self.red_color)

                drawer.text((450, 753), str(take), font=phont_2, fill="white")
                drawer.text((495, 831), str(entry), font=phont_2, fill="white")

            


        image = image.convert('RGB')
        image.save(f'main/images/{chat_id}_img.jpg')

    def drawscreen_test(self, res, chat_id):

        res = int(res)
        type = "long"
        entry = "123"
        take = "1234"
        coin_name = "BTCUSDT"
        leverage = "50X"

        if res > 0: 
            coin_font = ImageFont.truetype("main/fonts/OkomitoBold.ttf",50)
            type_font  = ImageFont.truetype("main/fonts/tghaidogroteskextrabold.otf",48)
            leverage_font  = ImageFont.truetype("main/fonts/BBCasualProBold.ttf",50)
            res_font  = ImageFont.truetype("main/fonts/QanelasMedium.ttf",200)
            phont_2  = ImageFont.truetype("main/fonts/NeulisAltSemiBold.ttf",50)
            usdt_font = ImageFont.truetype("main/fonts/ConfigRoundedText.ttf",210)
            plus_phont  = ImageFont.truetype("main/fonts/Clonoid.ttf",130)
            res = '+' + str(res)
            image = Image.open("main/images/per_bg_green.png")
            drawer = ImageDraw.Draw(image)

            if len(str(res).replace('.', '')) - 1> 6: 
                if '.' in str(res):
                    res  = str(res)[:8]
                else: 
                    res  = str(res)[:7]

            #drawer.text((100, 700), '+', font = plus_phont, fill= self.green_color)
          
            if len(coin_name) == 4:
                drawer.text((200, 320), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 5:
                drawer.text((160, 320), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 6:
                drawer.text((130, 320), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 7:
                drawer.text((90, 320), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 8:
                drawer.text((70, 320), coin_name, font=coin_font, fill='white')

            elif len(coin_name) == 9:
                drawer.text((50, 320), coin_name, font=coin_font, fill='white')


            if type == 'short':
                drawer.text((382, 310), "Шорт", font=type_font, fill=self.red_color)
            else: 
                drawer.text((382, 310), "Лонг", font=type_font, fill=self.green_color)

            drawer.text((580, 330), str(leverage) + 'X', font=leverage_font, fill="white")

            print(len(str(res).replace('.', ''))- 1)

            if len(str(res).replace('.', ''))- 1 == 4:    
                drawer.text((40, 420), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((600, 445), 'USDT', font=usdt_font, fill=self.green_color)
                else: 
                    drawer.text((550, 445), 'USDT', font=usdt_font, fill=self.green_color)
            elif len(str(res).replace('.', '')) - 1 == 5:
                drawer.text((40, 420), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((680, 445), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((635, 445), 'USDT', font=usdt_font, fill=self.green_color)

            elif len(str(res).replace('.', '')) - 1 == 6:
                drawer.text((40, 420), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((730, 445), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((660, 445), 'USDT', font=usdt_font, fill=self.green_color)
            elif len(str(res).replace('.', '')) - 1 == 7:
                drawer.text((40, 420), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((800, 445), 'USDT', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((790, 445), 'USDT', font=usdt_font, fill=self.green_color)
            elif len(str(res).replace('.', '')) - 1 <= 3:
                print('ok')
                drawer.text((60, 500), (str(res)), font=res_font, fill=self.green_color)
                if '.' in str(res):
                    drawer.text((500, 519), '%', font=usdt_font, fill=self.green_color)
                else:
                    drawer.text((430, 530), '%', font=usdt_font, fill=self.green_color)

            drawer.text((450, 753), str(take), font=phont_2, fill="white")
            drawer.text((470, 823), str(entry), font=phont_2, fill="white")

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

            drawer.text((1100, 2050), str(entry), font=phont_2, fill="white")

        image = image.convert('RGB')

        image.save(f'main/images/{chat_id}_img.jpg')






    
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        