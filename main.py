import os
import sys
import cv2 as cv
from src import preprocessing, filters, postprocessing, utils


def enhance_image(img_path, output_dir):
    image = cv.imread(img_path)
    preprocessed_image = preprocessing.preprocess_image(image)
    enhanced_image = filters.apply_filters(preprocessed_image)

    filename = os.path.basename(img_path)
    output_file = os.path.join(output_dir, filename)
    cv.imwrite(output_file, enhanced_image)
    print(f"Enhanced image saved: {output_file}")


def enhance_images_in_dir(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = utils.get_image_files(input_dir)

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        enhance_image(image_path, output_dir)


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("Usage: python main.py <input_path> <output_directory>")
    #     sys.exit(1)

    # input_path = sys.argv[1]
    # output_dir = sys.argv[2]

    # if os.path.isdir(input_path):
    #     enhance_images_in_dir(input_path, output_dir)
    # elif os.path.isfile(input_path):
    #     enhance_image(input_path, output_dir)
    # else:
    #     print("Input path does not exist.")
    #     sys.exit(1)
    image = cv.imread("data/originals/zion.jpg")

    preprocessed = preprocessing.preprocess_image(image)
    filtered = filters.apply_filters(preprocessed)
    postprocessed = postprocessing.apply_postprocessing(filtered)

    # cv.imshow("Original", image)
    # cv.imshow("Preprocessed", preprocessed)
    cv.imshow("Filtered", filtered)
    cv.imshow("Postprocessed", postprocessed)

    filename = os.path.basename("data/originals/zion.jpg")
    output_file = os.path.join("data/postprocessed", filename)
    cv.imwrite(output_file, postprocessed)
    # cv.imshow("Postprocessed", postprocessed)

    cv.waitKey()
    cv.destroyAllWindows()
