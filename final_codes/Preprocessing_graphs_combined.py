import os
from PIL import Image

def combine_png_images(input_folder, adasyn_output, kmeans_output, svmsmote_output, ae_mice_output, all_cih_output):
    # Get all PNG files in the input folder
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    
    if not png_files:
        print("No PNG files found in the specified folder.")
        return

    # Separate files into lists based on prefixes
    adasyn_files = [f for f in png_files if f.startswith('ADASYN')]
    kmeans_files = [f for f in png_files if f.startswith('KMeans')]
    svmsmote_files = [f for f in png_files if f.startswith('SVMSMOTE')]
    ae_mice_files = [f for f in png_files if f.startswith('AE') or f.startswith('MICE')]
    prior_files = [f for f in png_files if f.startswith('Prior')]

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

    # Combine images for each group along with prior files
    combine_images(prior_files + adasyn_files, adasyn_output)
    combine_images(prior_files + kmeans_files, kmeans_output)
    combine_images(prior_files + svmsmote_files, svmsmote_output)
    combine_images(prior_files + ae_mice_files, ae_mice_output)
    combine_images(prior_files + adasyn_files + kmeans_files + svmsmote_files, all_cih_output)

# Example usage
input_folder = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\TSNE graphs"
adasyn_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\TSNE combined graphs\\ADASYN_TSNE_combined.png"
kmeans_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\TSNE combined graphs\\KMeans_TSNE_combined.png"
svmsmote_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\TSNE combined graphs\\SVMSMOTE_TSNE_combined.png"
ae_mice_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\TSNE combined graphs\\AE_MICE_TSNE_combined.png"
all_cih_output = "C:\\Users\\dev\\Desktop\\MSC thesis\\Code\\final_codes\\TSNE combined graphs\\ALL_ClassIH_TSNE_combined.png"

if __name__ == "__main__":
    combine_png_images(input_folder, adasyn_output, kmeans_output, svmsmote_output, ae_mice_output, all_cih_output)
