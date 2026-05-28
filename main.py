import argparse
import os
from scanner import scan_directory
from reporter import print_report, save_report

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description="PII Scanner — Detect personal data leaks in source code"
    )
    parser.add_argument(
        '--path',
        type=str,
        default='.',
        help='Path to the folder you want to scan (default: current folder)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Optional: save report to this file (e.g. report.txt)'
    )
    
    args = parser.parse_args()
    
    # Check the folder exists
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        return
    
    print(f"\n🔍 Scanning: {args.path}")
    print("Please wait...\n")
    
    # Run the scan
    findings = scan_directory(args.path)
    
    # Print report to terminal
    print_report(findings)
    
    # Save to file if user asked for it
    if args.output:
        save_report(findings, args.output)

if __name__ == "__main__":
    main()