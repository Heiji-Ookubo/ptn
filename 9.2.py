from PIL import Image, ImageFilter
list_of_img = ["img_ppc/1.jpg", "img_ppc/2.jpg", "img_ppc/3.jpg", "img_ppc/4.jpg", "img_ppc/5.jpg",]
logo = Image.open("img_ppc/logo.jpg")
logo = logo.reduce(4)
for i in range(5):
    with Image.open(list_of_img[i]) as img:
        img.filter(ImageFilter.SHARPEN)
        img.show()
        img.paste(logo)
        img.show()