def validate_pdf(file_path):
    import os
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    if not file_path.lower().endswith('.pdf'):
        raise ValueError(f"The file {file_path} is not a valid PDF file.")
    
    return True

def check_pdf_size(file_path, max_size_mb=10):
    import os
    
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
    if file_size > max_size_mb:
        raise ValueError(f"The file {file_path} exceeds the maximum size of {max_size_mb} MB.")
    
    return True