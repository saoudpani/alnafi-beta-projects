#!/usr/bin/env python3

#roll a dice
import dice_ascii, random, os
def pil_dice(img_number):
    #from PIL import Image, ImageDraw, ImageEnhance
    #from IPython.display import display

    im = Image.open('dices.png')
    enhancer = ImageEnhance.Sharpness(im)
    im = enhancer.enhance(3)

    # Here the image "im" is cropped and assigned to new variable im_crop
    im_list = []
    left, right = 0, 135
    for d in range(1,7):
        #img_file = 'dice'+str(d)+'.png'
        single_dice = im.crop((4+left, 4, right*d, 140))
        im_list.append(single_dice)

    #     #save images one by one
    #     if not os.path.exists('imgs'):
    #         os.mkdir('imgs')
    #     single_dice.save('imgs/'+img_file)
        left+=133
    try:
        return display(im_list[img_number-1])
    except:
        print('six dices only')
def show_dice_image(image):
    try:
        pil_dice(image)
    except:
        if image == 1: print(dice_ascii.d1)
        elif image == 2: print(dice_ascii.d2)
        elif image == 3: print(dice_ascii.d3)
        elif image == 4: print(dice_ascii.d4)
        elif image == 5: print(dice_ascii.d5)
        elif image == 6: print(dice_ascii.d6)
        else: print('six dice images only')
            
#calculate probability of sum of two fair dices rolled
def probability_two_dices(total):
    if any(x == total for x in (12,2)): return (1/36)*100
    elif any(x == total for x in (11,3)): return (2/36)*100
    elif any(x == total for x in (10,4)): return (3/36)*100
    elif any(x == total for x in (9,5)): return (4/36)*100
    elif any(x == total for x in (8,6)): return (5/36)*100
    elif total == 7: return (6/36)*100 
  

#main game working code block
def probability_of_two_dices(total):
    if total == 12 or 1:
        return (1/36)*100

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    rand1, rand2 = random.randint(1, 6), random.randint(1, 6)
    total = rand1+rand2
    prob = probability_two_dices(total)
    show_dice_image(rand1)
    show_dice_image(rand2)
    print('Sum of two dices {} + {} = {}\nProbability of the sum of two dices is {:.2f}%'.format(rand1,rand2,total,prob))
    roll_again = input("Enter 'y' or 'yes' To Roll The dices Again?")
    try:
        clear_output(wait=True)
    except:
        # for windows 
        if os.name == 'nt': _ = os.system('cls') 
        # for mac and linux
        else: _ = os.system('clear')