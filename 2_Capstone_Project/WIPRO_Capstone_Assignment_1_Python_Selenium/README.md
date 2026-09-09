# Wipro Capstone Assignment 1
## Automate a Web Application Using Selenium WebDriver with Python

**This project uses Python + Selenium only. PyTest is NOT used.**

### Automated Flow
1. Launch Chrome
2. Open Automation Exercise
3. Login
4. Search product
5. Open product details
6. Set quantity
7. Add to cart
8. Open cart
9. Verify product and quantity
10. Capture screenshots
11. Generate HTML execution report

### Install
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### Credentials
Create `test_data/credentials.json`:
```json
{
  "email": "your_registered_email@example.com",
  "password": "your_password"
}
```
Do NOT upload this file to GitHub.

### Run
```powershell
python tests/ecommerce_test.py
```

No PyTest is required.

### Output
Screenshots: `screenshots/`
Execution report: `reports/execution_report.html`

Selenium 4 uses Selenium Manager, so a separate chromedriver or webdriver-manager package is normally not required.
