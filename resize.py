from PIL import Image

def resize_image(input_path, output_path, size=(1080, 1080)):
    img = Image.open(input_path)
    img = img.resize(size, Image.ANTIALIAS)
    img.save(output_path)
    print(f"Image saved at {output_path}")

resize_image("input.jpg", "output.jpg")
