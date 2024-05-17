import os
import datetime
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("DATABASE"))
