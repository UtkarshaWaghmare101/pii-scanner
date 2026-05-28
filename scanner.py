import os
from patterns import PII_PATTERNS

def scan_file(filepath):
    """Scan a single file and return a list of findings."""
    findings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for line_number, line in enumerate(lines, start=1):
            for pii_type, pattern in PII_PATTERNS.items():
                matches = pattern.findall(line)
                if matches:
                    findings.append({
                        "file": filepath,
                        "line": line_number,
                        "type": pii_type,
                        "content": line.strip()
                    })
    except Exception as e:
        print(f"Could not read file {filepath}: {e}")
    
    return findings


def scan_directory(directory):
    """Walk through all files in a folder and scan each one."""
    all_findings = []
    
    # File types we care about
    allowed_extensions = ['.py', '.js', '.ts', '.txt', '.env', '.json', '.yaml', '.yml', '.config']
    
    for root, dirs, files in os.walk(directory):
        # Skip hidden folders like .git
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in allowed_extensions:
                full_path = os.path.join(root, filename)
                findings = scan_file(full_path)
                all_findings.extend(findings)
    
    return all_findings