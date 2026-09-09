from pathlib import Path
from datetime import datetime
from html import escape

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

class ExecutionReport:
    def __init__(self):
        self.rows = []
        self.start_time = datetime.now()

    def add(self, step, status, details=""):
        self.rows.append((step, status, details))

    def save(self):
        rows = "".join(
            "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                escape(step), escape(status), escape(details)
            )
            for step, status, details in self.rows
        )
        html = (
            "<!DOCTYPE html><html><head><meta charset='UTF-8'>"
            "<title>Selenium Execution Report</title></head>"
            "<body style='font-family:Arial;margin:40px'>"
            "<h1>Wipro Selenium Capstone - Execution Report</h1>"
            "<p>Start: " + str(self.start_time) + "</p>"
            "<p>End: " + str(datetime.now()) + "</p>"
            "<table border='1' cellpadding='8' cellspacing='0' width='100%'>"
            "<tr><th>Step</th><th>Status</th><th>Details</th></tr>"
            + rows +
            "</table></body></html>"
        )
        path = REPORT_DIR / "execution_report.html"
        path.write_text(html, encoding="utf-8")
        return str(path)
