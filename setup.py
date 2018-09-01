from setuptools import setup, find_packages


setup(
    name="explainability",
    version="0.1",
    packages=find_packages(),

    install_requires=[
    	"scikit-learn",
    	"scikit-image",
    	"opencv-python",
    	"keras",
    	"torch",
        "torchvision",
        "tqdm",
        "matplotlib",
        "pandas",
        "ray",
        "shapely",
        "numpy",
    ],

    # Excluding LIME
    dependency_links=[
    	"git+https://github.com/michaeltu1/Mask_RCNN.git",
		"git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI",
		"git+https://github.com/keras-team/keras-contrib.git"
    ]
)
