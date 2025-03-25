import os
os.environ["TQDM_DISABLE"] = "1"  # just in case
from transformers import pipeline

def main():
    pipe = pipeline(
        "image-classification",
        model="dima806/facial_emotions_image_detection",
        use_fast=True,
    )
    print(pipe("image.jpg"))

if __name__ == "__main__":
    main()