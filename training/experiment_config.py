from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

images_dir = os.getenv("IMAGE_DIR")
volumes_dir = os.getenv("VOLUME_DIR")
working_dir = os.getenv("WORKING_DIR")

class Configuration(object):
    def __init__(self) -> None:

        # Working directory
        self.WORKDIR = Path(working_dir)
        self.RESOURCES = self.WORKDIR / "models" / "resources"
        # Starting weights for the I3D model
        self.MODEL_RGB_I3D = (
            self.RESOURCES / "model_rgb.pth"
        )
        
        # Data parameters
        # Path to the nodule blocks folder provided for the LUNA25 training data. 
        self.DATADIR = Path(volumes_dir + "\luna25_nodule_blocks")
        # Path to the folder containing the CSVs for training and validation.
        self.CSV_DIR = Path(volumes_dir)
        self.CSV_DIR_TRAIN = self.CSV_DIR / "train.csv" # Path to the training CSV
        self.CSV_DIR_VALID = self.CSV_DIR / "valid.csv" # Path to the validation CSV

        # Results will be saved in the /results/ directory, inside a subfolder named according to the specified EXPERIMENT_NAME and MODE.
        self.EXPERIMENT_DIR = self.WORKDIR / "results"
        if not self.EXPERIMENT_DIR.exists():
            self.EXPERIMENT_DIR.mkdir(parents=True)
            
        self.EXPERIMENT_NAME = "baseline3D_adam10epochs"
        self.MODE = "3D" # 2D or 3D

        # Training parameters
        self.SEED = 2025
        self.NUM_WORKERS = 8
        self.SIZE_MM = 50
        self.SIZE_PX = 64
        self.BATCH_SIZE = 32
        self.ROTATION = ((-20, 20), (-20, 20), (-20, 20))
        self.TRANSLATION = True
        self.EPOCHS = 10
        self.PATIENCE = 20
        self.PATCH_SIZE = [64, 128, 128]
        self.LEARNING_RATE = 1e-4
        self.WEIGHT_DECAY = 5e-4

config = Configuration()