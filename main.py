import os
from dotenv import load_dotenv

from DataManager import DataManager

load_dotenv()

print(os.getenv("DATABASE"))
dm = DataManager(os.getenv("DATABASE"))
print(dm.validate())
