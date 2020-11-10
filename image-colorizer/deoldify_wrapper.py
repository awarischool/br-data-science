import os
from os import path
import warnings
try:
    print("  Importing Libraries")
    from deoldify import device
    from deoldify.device_id import DeviceId
    device.set(device=DeviceId.GPU0)
    import torch
    if not torch.cuda.is_available():
        warnings.warn('WARNING: GPU not available. Activate it on Colab at Edit > Notebook Settings')

    print("  Installing Colab requirements...")
    os.system("pip install -r colab_requirements.txt")

    print("  Importing DeOldify Visualize module and FastAI")
    import fastai
    from deoldify.visualize import *
    torch.backends.cudnn.benchmark = True

except Exception as e:
    print(e)
    print("DeOldify not found, installing..")
    if not path.exists('DeOldify'):
        print("  Cloning DeOldify Repository...")
        os.system("git clone https://github.com/jantic/DeOldify.git DeOldify")
        print("  Opening DeOldify Folder")
        os.chdir("DeOldify")

    print("  Importing Libraries")
    from deoldify import device
    from deoldify.device_id import DeviceId
    device.set(device=DeviceId.GPU0)
    import torch
    if not torch.cuda.is_available():
        warnings.warn('WARNING: GPU not available. Activate it on Colab at Edit > Notebook Settings')

    print("  Installing Colab requirements...")
    os.system("pip install -r colab_requirements.txt")

    print("  Importing DeOldify Visualize module and FastAI")
    import fastai
    from deoldify.visualize import *
    torch.backends.cudnn.benchmark = True

    print("  Downloading Colorizer Model")
    os.system("mkdir 'models'")
    os.system("wget https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth?dl=0 -O ./models/ColorizeStable_gen.pth")

class DeOldify:
    def __init__(self):
        print("  Initializing Colorizer")
        self.colorizer = get_image_colorizer(artistic=False)
        self.show_image_in_notebook = show_image_in_notebook

        print("Done!")
    def sys(self, cmd):
        os.system(cmd)

    def colorize(self, filepath_or_url=None, render_factor = 35, compare=True):
        source_url = filepath_or_url

        if source_url is not None and source_url !='':
            image_path = self.colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=compare)
            self.show_image_in_notebook(image_path)
        else:
            print('Provide an image url and try again.')
    def range_render_factor(self):
        for i in range(10,40,2):
            self.colorizer.plot_transformed_image('test_images/image.png', render_factor=i, display_render_factor=True, figsize=(8,8))
