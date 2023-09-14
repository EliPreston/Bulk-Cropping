from PIL import Image
import os


def crop(width, height, xStart, yStart):

    area = (xStart, yStart, xStart+width, yStart+height)
    count = 0

    for filename in filenames:
        img = Image.open("input/"+filename)

        croppped_img = img.crop(area)
        cropped_label = "Page " + str(count) + ".png"
        croppped_img.save(f"output/{cropped_label}") 
        
        print(f"Image {count} finished processing....")
        count += 1
        

    print("All images cropped")





if __name__ == "__main__":
    folder = "input"
    filenames = [filename for filename in os.listdir(folder)]
    filenames.sort()

    width, height = 990, 1447
    xStart, yStart = 1020, 245

    crop(width, height, xStart, yStart)



