#!/usr/bin/env python3
"""Script to build and publish the lunchmoney-mcp package"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def main():
    """Main publication process"""
    print("📦 Publishing lunchmoney-mcp to PyPI")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ pyproject.toml not found. Make sure you're in the project root directory.")
        sys.exit(1)
    
    # Clean previous builds
    if Path("dist").exists():
        run_command("rm -rf dist/", "Cleaning previous builds")
    
    if Path("build").exists():
        run_command("rm -rf build/", "Cleaning build directory")
    
    # Build the package
    run_command("python -m build", "Building package")
    
    # Check if dist directory was created
    if not Path("dist").exists():
        print("❌ Build failed - no dist directory created")
        sys.exit(1)
    
    # List built files
    print("\n📄 Built files:")
    for file in Path("dist").glob("*"):
        print(f"  - {file.name}")
    
    # Ask for confirmation before uploading
    print("\n🚀 Ready to upload to PyPI")
    print("Make sure you have:")
    print("  - PyPI account credentials")
    print("  - Updated version number in pyproject.toml")
    print("  - All changes committed to git")
    
    response = input("\nProceed with upload? (y/N): ")
    if response.lower() != 'y':
        print("❌ Upload cancelled")
        sys.exit(0)
    
    # Upload to PyPI
    # First try TestPyPI
    print("\n🧪 Uploading to TestPyPI first...")
    try:
        run_command("python -m twine upload --repository testpypi dist/*", "Uploading to TestPyPI")
        print("✅ Successfully uploaded to TestPyPI")
        
        response = input("\nUpload to production PyPI? (y/N): ")
        if response.lower() == 'y':
            run_command("python -m twine upload dist/*", "Uploading to PyPI")
            print("✅ Successfully uploaded to PyPI")
            print("\n🎉 Package published successfully!")
            print("Install with: pip install lunchmoney-mcp")
        else:
            print("❌ Production upload cancelled")
            print("Test installation with: pip install -i https://test.pypi.org/simple/ lunchmoney-mcp")
            
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        print("Make sure you have configured your PyPI credentials")
        print("Run: python -m twine configure")

if __name__ == "__main__":
    main() 