# Extracted from https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

