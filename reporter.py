from datetime import datetime

def print_report(findings):
    """Print a formatted report to the terminal."""
    
    print("\n" + "="*60)
    print("         PII SCANNER — SCAN REPORT")
    print("="*60)
    print(f"Scan Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Issues Found : {len(findings)}")
    print("="*60 + "\n")
    
    if not findings:
        print("✅ No PII detected. Your code looks clean!")
        return
    
    # Group findings by file
    files_found = {}
    for item in findings:
        if item['file'] not in files_found:
            files_found[item['file']] = []
        files_found[item['file']].append(item)
    
    for filepath, items in files_found.items():
        print(f"📄 FILE: {filepath}")
        print("-" * 50)
        for item in items:
            print(f"  Line {item['line']:>4}  |  {item['type']:<25}  |  {item['content'][:60]}")
        print()


def save_report(findings, output_path):
    """Save the report to a text file."""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("PII SCANNER — SCAN REPORT\n")
        f.write("="*60 + "\n")
        f.write(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Issues: {len(findings)}\n")
        f.write("="*60 + "\n\n")
        
        if not findings:
            f.write("No PII detected.\n")
            return
        
        for item in findings:
            f.write(f"File    : {item['file']}\n")
            f.write(f"Line    : {item['line']}\n")
            f.write(f"Type    : {item['type']}\n")
            f.write(f"Content : {item['content'][:80]}\n")
            f.write("-"*40 + "\n")
    
    print(f"\n💾 Report saved to: {output_path}")