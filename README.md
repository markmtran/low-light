*Please note: The "Review of Current Methods" section's format messes up when exporting the notebook as a PDF, so I've included it below my write-up.*

### Write-up
As a supplement to my final project, I intended to explore low-light image enhancement techniques with the following steps:

1. Pre-processing
    - Normalize the image
    - Noise Reduction
2. Enhancement
    - Contrast Enhancement
    - Sharpening
    - Brightness Adjustment
    - Exposure Compensation
3. Post-processing
    - Color Correction

I first went through the LearnOpenCV tutorial to solidify my understanding of direct kernel applications and convolutional blurs. I then transitioned to exploring other OpenCV methods that allowed me to reduce the noise in images, enhance contrast, sharpen the images, adjust their brightness, and compensate exposure. I then also tried to perform color correction on the image, but I'm currently unsuccessful as I am losing my three channels in the previous steps. However, I am able to generate some output image that looks sort of looks like some grayscale social media filter.

![Original](https://ibb.co/L9YZQJ4)
![After Filtering](https://ibb.co/M1xz3gg)

Although you can see additional details in the valley below, the sky seems to have degraded as well, so I would like to explore why.

I also looked into the "Contrast Enhancement Using the Laplacian-of-a-Gaussian Filter" paper by Neycenssac some more and tried to replicate their work, but I'm not quite sure what I'm getting myself into. 

![LoG](https://ibb.co/PskywzW)

Here, some edges are enhanced, but much detail is lost.

### Review of Current Methods
Once you’ve selected a topic or project idea, explore the literature space. Has there been academic research on this topic? Are there tutorials online, software packages, or libraries? 

Select at least 5 resources (youtube videos, papers, tutorials, opensource software, libraries, etc) and provide a short description (2-3 sentences) below: 

* Source 1: [LearnOpenCV - Image Filtering Using Convolution in OpenCV](https://learnopencv.com/image-filtering-using-convolution-in-opencv/)
    - This tutorial is a guide on how to use use 2D-convolution kernels and the OpenCV Computer Vision library to apply different blurring and sharpening techniques to an image. It also mentions bilateral filtering, which "selectively [blurs] similar intensity pixels in a neighborhood" while preserving sharper edges, and it does this by essentially changing the shape of the kernel depending on the local image content for every pixel.
      
* Source 2: [Low-light Image Enhancement via Breaking Down the Darkness](https://link.springer.com/article/10.1007/s11263-022-01667-9)
    - This paper discusses the multi-degradation of low-light images and proceeds to offer a solution capable of enhancing them by converting the RGB colorspace into a luminance-chrominance colorspace. An interesting subproblem handled by this research is the capture of images when the camera is directly opposing a light source, making the image subject particularly dark; it also discusses other methods that perform the same task, which may also be worth looking into.
      
* Source 3: [Contrast Enhancement Using the Laplacian-of-a-Gaussian Filter](https://www.sciencedirect.com/science/article/pii/S1049965283710345)
    - This paper seeks to improve the visual quality of an image by increasing the difference in intensity between neighboring pixels. It does so by applying a "Laplacian-of-a-Gaussian" (LoG) filter, which combines Gaussian smoothing with edge detection, convolving the Gaussian filter with the Laplacian filter.
      
* Source 4: [Efficient image sharpening and denoising using adaptive guided image filtering](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-ipr.2013.0563)
    - Adaptive guided image filtering enhances edges to be as sharp as adaptive bilateral filtering, but with less computational complexity. It produces a noise-free, sharpened output without producing halo-artefacts by combining guided filter and shift-variant techniques.
      
* Source 5: [Color Image Enhancement with Saturation Adjustment Method](https://link.springer.com/article/10.1007/s11263-020-01407-x)
    - This paper discusses a multi=step framework to enhance low-light image quality: exposure adjustment, contrast enhancement, color restoration, and texture refinement. It decomposes images into two components -- illumination (for light adjustment) and reflectance (for degradation removal) -- decoupling the original space into two smaller subspaces for better regularization/learning.

Topics to explore: noise reduction filters, contrast enhancement, sharpening filters, color/saturation correction