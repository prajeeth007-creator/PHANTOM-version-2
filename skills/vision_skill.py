import cv2

def analyze_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return "I cannot see the image."

    height, width, channels = img.shape

    return f"I see an image with resolution {width}x{height}."