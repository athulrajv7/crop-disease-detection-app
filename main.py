import os
import cv2

IMAGE_DIR = "data/sample_leaf_images"

def list_images(folder_path):
    print("\n🔍 Looking for images in:", folder_path)
    files = os.listdir(folder_path)
    images = [f for f in files if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    return images

def load_and_show_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"⚠️ Failed to load {image_path}")
        return
    print(f"✅ Loaded {image_path} - shape: {img.shape}")
    # Uncomment below to actually view the image
    # cv2.imshow("Leaf Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    print("🌿 Crop Disease Detection - Starter App")

    image_files = list_images(IMAGE_DIR)

    if not image_files:
        print("🚫 No images found. Add some to the folder first.")
    else:
        for filename in image_files:
            full_path = os.path.join(IMAGE_DIR, filename)
            load_and_show_image(full_path)
