import pandas as pd
import re

def write_to_excel(structured_info, excel_output_path):
    # Extract lines that look like table rows
    lines = [line.strip() for line in structured_info.splitlines() if "|" in line]
    # Remove separator line (the one with ---)
    lines = [line for line in lines if not re.match(r"^\s*\|?\s*-+\s*\|", line)]
    # Split each line into columns
    rows = [ [cell.strip() for cell in line.strip("|").split("|")] for line in lines ]
    # First row is header
    header, *data = rows
    # Create DataFrame and write to Excel
    df = pd.DataFrame(data, columns=header)
    df.to_excel(excel_output_path, index=False)