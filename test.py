
import os
ROOT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)

print(os.path.abspath(os.path.join(ROOT_PATH, "results")))