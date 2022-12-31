from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()

print(os.getenv('BD_PASSWORD'))
