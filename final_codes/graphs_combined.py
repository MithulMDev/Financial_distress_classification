import os
from PIL import Image

def combine_png_images(input_folder, adasyn_ae_output, adasyn_mice_output, kmsmote_ae_output, kmsmote_mice_output, svmsmote_ae_output, svmsmote_mice_output):
    # Get all PNG files in the input folder
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    
    if not png_files:
        print("No PNG files found in the specified folder.")
        return

    # Separate files into lists
    adasyn_ae_files = [f for f in png_files if f.startswith('ADASYN_AE_3_PCA')]
    adasyn_mice_files = [f for f in png_files if f.startswith('ADASYN_MICE_3_PCA')]
    kmsmote_ae_files = [f for f in png_files if f.startswith('KMSMOTE_AE_3_PCA')]
    kmsmote_mice_files = [f for f in png_files if f.startswith('KMSMOTE_MICE_3_PCA')]
    svmsmote_ae_files = [f for f in png_files if f.startswith('SVMSMOTE_AE_3_PCA')]
    svmsmote_mice_files = [f for f in png_files if f.startswith('SVMSMOTE_MICE_3_PCA')]

    # Function to combine images for a given list of files
    def combine_images(file_list, output_file):
        if not file_list:
            print(f"No images to combine for {output_file}")
            return

        # Open all images
        images = [Image.open(os.path.join(input_folder, f)) for f in file_list]

        # Calculate the size of the output image
        max_width = max(img.width for img in images)
        total_height = sum(img.height for img in images)

        # Create a new image with the calculated dimensions
        combined_image = Image.new('RGB', (max_width, total_height), color='white')

        # Paste all images into the new image
        y_offset = 0
        for img in images:
            combined_image.paste(img, (0, y_offset))
            y_offset += img.height

        # Save the combined image
        combined_image.save(output_file)
        print(f"Combined image saved as {output_file}")

    # Combine images for each group
    combine_images(adasyn_ae_files, adasyn_ae_output)
    combine_images(adasyn_mice_files, adasyn_mice_output)
    combine_images(kmsmote_ae_files, kmsmote_ae_output)
    combine_images(kmsmote_mice_files, kmsmote_mice_output)
    combine_images(svmsmote_ae_files, svmsmote_ae_output)
    combine_images(svmsmote_mice_files, svmsmote_mice_output)

# Example usage
input_folder = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Lime and shap graphs"
adasyn_ae_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Final graphs\\combined_adasyn_ae_images.png"
adasyn_mice_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Final graphs\\combined_adasyn_mice_images.png"
kmsmote_ae_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Final graphs\\combined_kmsmote_ae_images.png"
kmsmote_mice_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Final graphs\\combined_kmsmote_mice_images.png"
svmsmote_ae_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Final graphs\\combined_svmsmote_ae_images.png"
svmsmote_mice_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\Final graphs\\combined_svmsmote_mice_images.png"



if __name__ == "__main__":
    
    combine_png_images(input_folder, adasyn_ae_output, adasyn_mice_output, kmsmote_ae_output, kmsmote_mice_output, svmsmote_ae_output, svmsmote_mice_output)