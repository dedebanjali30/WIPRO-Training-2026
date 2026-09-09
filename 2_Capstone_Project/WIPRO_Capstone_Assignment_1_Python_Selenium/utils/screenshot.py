from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

def take_screenshot(driver, name):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = "".join(c if c.isalnum() or c in "_-" else "_" for c in name)
    path = SCREENSHOT_DIR / f"{safe}_{stamp}.png"
    driver.save_screenshot(str(path))
    return str(path)
