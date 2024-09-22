# Image Processing Techniques

This repository contains various image processing techniques implemented using Python, including histogram equalization, logarithmic transformations, and image specification methods.

## Files Included

- `image_specification.py`: Applies image specification techniques using two images.
- `image_transformation.py`: Demonstrates various image transformations.
- `image_transformation_with_variants.py`: Includes multiple transformation options (linear, logarithmic, exponential).
- `image_histogram.py`: Analyzes and displays histograms of images.

## Features:

- `Histogram Equalization`: Enhance the contrast of images by redistributing pixel intensity values.
- `Logarithmic Transformations`: Apply logarithmic scaling to adjust the brightness and contrast of images.
- `Image Specification`: Utilize a reference image to specify the histogram of another image for better visual results.
- `Histogram Analysis`: Generate and visualize histograms to understand the distribution of pixel intensities in images.

## Getting Started

1. Clone the repository:
    ```sh
    git clone git@github.com:MateusjsSilva/image-processing-techniques.git
    cd image-processing-techniques\src\
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Run the Scripts

1. **Execute the desired script using Python**:
    ```sh
    python <script-name>.py
    ```

## Contribution

Feel free to open issues or submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.