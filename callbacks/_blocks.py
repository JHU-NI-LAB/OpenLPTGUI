import enum

class Blocks(enum.Enum):
    __order__ = 'importImage setAreaColor histogramEqualization brightnessAndContrast averageBlur gaussianBlur medianBlur grayscale globalThresholding adaptativeMeanThresholding adaptativeGaussianThresholding otsuBinarization findContour'
    importImage = 0
    setAreaColor = importImage + 1
    histogramEqualization = setAreaColor + 1
    brightnessAndContrast = histogramEqualization + 1
    averageBlur = brightnessAndContrast + 1
    gaussianBlur = averageBlur + 1
    medianBlur = gaussianBlur + 1
    grayscale = medianBlur + 1
    globalThresholding = grayscale + 1
    adaptativeMeanThresholding = globalThresholding + 1
    adaptativeGaussianThresholding = adaptativeMeanThresholding + 1
    otsuBinarization = adaptativeGaussianThresholding + 1
    findContour = otsuBinarization + 1