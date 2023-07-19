import os


RM_API_BASE_URL = os.getenv("RM_API_BASE_URL")
RM_API_CHARACTERS_URL = f"{RM_API_BASE_URL}/character"
RM_API_LOCATION_URL = f"{RM_API_BASE_URL}/location"
RM_API_EPISODE_URL = f"{RM_API_BASE_URL}/episode"

OUTPUT_DIR = os.path.join(os.getcwd(), "output")
