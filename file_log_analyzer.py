import re
from collections import Counter
from pathlib import Path

LOG_FILE = "application.log"

def parse_log(file_path: str):
    """Parse a log file and count occurrences of ERROR, WARNING, INFO."""
    counts = Counter()
    error_lines = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                counts["ERROR"] += 1
                error_lines.append(line.strip())
            elif "WARNING" in line:
                counts["WARNING"] += 1
            elif "INFO" in line:
                counts["INFO"] += 1

    return counts, error_lines

def save_report(counts, error_lines, output_file="log_report.txt"):
    """Save a summary report to a text file."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=== Log Report ===\n")
        for level, count in counts.items():
            f.write(f"{level}: {count}\n")
        f.write("\n--- Error Details ---\n")
        for line in error_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    log_path = Path(LOG_FILE)
    if log_path.exists():
        counts, errors = parse_log(LOG_FILE)
        save_report(counts, errors)
        print("✅ Log analysis complete. Report saved to log_report.txt")
    else:
        print(f"⚠️ Log file {LOG_FILE} not found.")