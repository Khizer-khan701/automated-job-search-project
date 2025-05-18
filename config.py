import os
import sys
from dotenv import load_dotenv
from exception import CustomException
from logger import logging
load_dotenv()

try:
    # APi KEYS
    logging.info("Getting the APIs")
    OPEN_API_KEY=os.getenv("OPEN_API_KEY")
    SERP_API_KEY=os.getenv("SERP_API_KEY")

    # Model Setting
    LLM_MODEL="gpt-3.5-turbo"

    # job Search Setting
    DEFAULT_JOBCOUNT=5
    JOB_PLATFORMS=["LinkedIn","Indeed","Glassdoor","ZipRecruiter","Monster"]

    COLORS={
        # Primary palette
        "primary": "#1C4E80",    # Dark Blue For main elements and headers
        "secondary": "#0091d5",  # Medium Blue for secondary
        "tertiary":  "#6BB4C0",  # Teal blue for tertiary elements 

        # Accent colors
        "accent": "#F17300",     #Orane for highlighting
        "accent1": "#3E7CB1",    #Steel blue for subtler accent
        "accent2": "#44BBA4",    #Seaform for highlighting
        "accent3": "#F17300",    #Orange for call-to-action buttons

        # Functional colors
        "success": "#26A69A",    #Teal Green for success message
        "warning": "#F9A825",    #Golden yellow for warnings
        "error":   "#E53935",    #Bright Red for error
        "info":    "#0277BD",    #Information Blue

        # Background and text - Basic professional style
        "background": "#F5F7FA", # light blue-gray for backgrounds
        "card_bg":    "#FFFFFF", #white for card background
        "text":       "#FFFFFF", # Text for text on dark background
        "text_dark":  "#000000", # Black for text on light backgrounds
        "text_red":   "#FF5252", #Red color for high contrast text
        "panel_bg":   "#F0F5FF", #Light blue background for panels

    }
    logging.info("Configuration is done")
except Exception as e:
    raise CustomException(e,sys)