
from PIL import Image, ImageDraw, ImageFont
import os

class DrawScreen2:
    def __init__(self):
        self.num_font  = ImageFont.truetype("main/fonts/ConfigRoundedMedium.ttf",192)
        self.text_font = ImageFont.truetype("main/fonts/URWGeometricRegular.otf",176)
        self.grey_color = (87, 87, 87)
        self.green_color = (90,197,157,255)
        self.red_color = (245,76,85,255)
    
    def put_commas(self, s): 
        s = str(s).split('.')
        s1 = s[0][::-1]
        s3 = ''
        while len(s1) > 0: 
            s3 = s1[:3][::-1] + ',' + s3 
            s1 = s1[3:]
        if s3.endswith(','): 
            s3 = s3[:-1]
        if len(s) > 1:
            return str(s3+'.'+ s[1])
        else: 
            return str(s3)
        
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
        
    def drawscreen(self, data, chat_id):
        type = data['type']
        marge = (data['marge'])
        entry = (data['entry_price'])
        take = (data['current_price'])
        leverage = (data['leverage'])
        coin_name = data['coin_name']
        risk = data['risk']
        

        #подсчет позиции
        position = float(marge) * float(leverage)


        #подсчет pnl
        if type == 'long': 
            b = float(entry)
            a = float(take) 

            percent = ((a/b-1) * int(leverage))  
            pnl = float(marge) * percent

        else:
            b = float(take)
            a = float(entry)
            percent = (((b/a-1) * 100) * int(leverage) /100) 
            pnl = float(marge) * percent * -1

        #подсчет pnl в процентах
        pnl_percent = pnl/(float(marge)/100)
        pnl_percent = round(pnl_percent, 2) 



        #подсчет ликвидации 
        if type == 'long':
            liquidation = (float(entry)*int(leverage)) / (int(leverage) + 1 - (int(leverage) / 100))
        else: 
            liquidation = (float(entry)*int(leverage)) / (int(leverage) - 1 + (int(leverage) / 100))
        
    
        if '.' in str(pnl):
            if len(str(pnl).split('.')[1]) > 5: 
                pnl = round(float(pnl), 4)

        if '.' in str(position):
            if len(str(position).split('.')[1]) > 2: 
                position = round(float(position), 2)
        

        if '.' in str(liquidation):
            if len(str(liquidation).split('.')[1]) > 6: 
                liquidation = round(float(liquidation), 6)


        if type == 'long': 
            image = Image.open("main/images/2vbg_green1.png")
        else:
            image = Image.open("main/images/2vbg_red1.png")
        drawer = ImageDraw.Draw(image)


        #рисуем название монеты 

        font = ImageFont.truetype("main/fonts/FontsFree-Net-TTInterfaces-Medium.ttf",200)
        drawer.text((4 * 55, 4 * 60), coin_name, font=font, fill="black")




        #рисуем плечо
        font = ImageFont.truetype("main/fonts/URWGeometric-Medium.ttf",160)
        if len(leverage) >= 2:
            drawer.text((4 * 456, 4 * 154), leverage + 'X', font=font, fill=self.grey_color)
        else:
            drawer.text(( 4 * 467, 4 * 154), leverage + 'X', font=font, fill=self.grey_color)

        #рисуем п/у
        if float(pnl) < 0: 
            drawer.text((4 * 65, 4 * 335), '-' + self.put_commas(str(pnl)[1:]), font=self.num_font, fill=self.red_color)
        else: 
            drawer.text((4 * 65,4 *  335), '+' + self.put_commas(pnl), font=self.num_font, fill=self.green_color)

        #рисуем доход

        if float(pnl_percent) < 0: 
           x_coor = 1125 - 25*(len(str(pnl_percent)) - 5)
           pnl_percent = str(pnl_percent)
           color = self.red_color
           drawer.text((4 * x_coor, 4 * 335), '-' + self.put_commas(str(pnl_percent)[1:]) + '%', font=self.num_font, fill=color)
        else: 
            x_coor = 1125 - 25*(len(str(pnl_percent)) - 4)
            pnl_percent = str(pnl_percent) 
            color = self.green_color
            drawer.text((4 * x_coor, 4 * 335), '+' + self.put_commas(str(pnl_percent)) + '%', font=self.num_font, fill=color)
        
        #рисуем позицию 
        drawer.text((4 * 70, 4 * 470), str(position), font=self.num_font, fill='black')


        #рисуем цену открытия
        drawer.text((4 * 70,4 *  620), self.put_commas(str(entry)), font=self.num_font, fill='black')
        
        #рисуем маркировку
        drawer.text((4 * 530,4 *  620), self.put_commas(str(take)), font=self.num_font, fill='black')
        
             
        #рисуем ликвидацию
        x_coor = 1250 - 25*(len(str(liquidation)) - 1)
        drawer.text((4 * x_coor,4 *  620), self.put_commas(str(liquidation)), font=self.num_font, fill='black')

        #рисуем маржу  
        drawer.text((4 * 530, 4 * 470), marge, font=self.num_font, fill='black')
        im2 = Image.open("main/images/test2.png")
        x_coor = 2240 + (100*(len(marge)-1))
        image.paste(im2, (x_coor, 1870))

        #рисуем риск
        x_coor = 1225 - 25*(len(risk) - 1)
        drawer.text((4 * x_coor,4 * 470), risk + '%', font=self.num_font, fill=self.green_color)
        
        image = image.convert('RGB')

        image.save(f'main/images/{chat_id}_img.jpg')

            
    def delete_screen(self, chat_id):
        path = f'main/images/{chat_id}_img.jpg' 
        os.remove(path)        