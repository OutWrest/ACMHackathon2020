from PIL import Image, ImageDraw, ImageFont
import numpy as np

def export(img: Image, ttext: str, btext=None, paper='3400x4400', simg=2000, bg=(255, 255, 255)) -> Image:
    # Assert printer resolution (11x8.5) size
    pw, pl = tuple(map(int,paper.split('x')))
    assert (8.5/11) == (pw/pl)

    # Resize image to almost 2000x2000
    ix, iy = img.size
    factor = (simg/max(img.size))
    nx, ny = int(ix*factor), int(iy*factor)
    img = img.resize((nx,ny))

    # Paste class image on blank image
    p_img = Image.new('RGB', (pw, pl), bg)
    p_img.paste(img, (int((pw/2 - nx/2)), int(pl/3.3 - ny/2)))

    # Add top text
    font = ImageFont.truetype("arial.ttf", 350)
    draw = ImageDraw.Draw(p_img)

    w, _ = draw.textsize(ttext, font=font)

    draw.text(((pw - w)/2, 0), ttext, (0, 0, 0), font=font)

    return p_img


def drawTable(dx, dy, arr:np.array, fsmol=0, bg=(255, 255, 255), color=(0, 0, 0)) -> Image:
    # Still needs some work

    t_img = Image.new('RGB', (dx, dy), bg)
    t_arr = np.array(t_img)
    h, w, _ = (t_arr.shape)

    t_table = []

    arows, acols = arr.shape
    #print(arr.shape)

    a_x = w
    a_x-= fsmol

    if fsmol:
        acols-=1
        t_table.append(0) # Error fix
    
    # Develop rows
    pr = dy//arows
    
    for i in range(arows):
        for k in range(w):
            t_arr[i*pr][k] = color

    for k in range(w):
        t_arr[-1][k] = color

    # Develop cols
    pc = a_x//acols
    
    for i in range(acols):
        for k in range(w):
            t_arr[k][(w-a_x)+(i*pc)] = color

    for k in range(w):
        t_arr[k][w-1] = color

    for k in range(w):
        t_arr[k][0] = color

    # Fill text into table

    for i in range(acols):
        t_table.append((w-a_x)+(i*pc))
    
    img = Image.fromarray(t_arr)

    t_table.append(h)
    
    font = ImageFont.truetype("arial.ttf", w//25)
    draw = ImageDraw.Draw(img)


    #print(t_table)
    for row in range(arows):
        for i in range(len(t_table)-1):
            if not arr[row][i] == None:
                t_txt = str(arr[row][i])
                tw, th = draw.textsize(t_txt, font=font)

                mw = t_table[i] + ((t_table[i+1]-t_table[i])//2)

                draw.text(((mw-(tw//2)), row*pr), t_txt, color, font=font)


    return img
    





if __name__ == "__main__":
    # 3300x2250 ()
    path = 'ColdenHall/ch3200.png'
    img = Image.open(path)

    #p_img = export(img, 'CH3200')
    #p_img.show()
    n = [['#', 'Seat', 'S-#', 'Student Name']]
    for i in range(20 ):
        n.append([i+1, None, None, None])

    a = drawTable(3000, 1500, np.array(n), fsmol=300)
    a.show()




