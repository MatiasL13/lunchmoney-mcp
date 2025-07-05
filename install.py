#!/usr/bin/env python3
"""Quick installation script for lunchmoney-mcp"""

import os
import sys
import subprocess
import json
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
        return None

def get_claude_config_path():
    """Get the Claude Desktop config path for the current OS"""
    if os.name == 'nt':  # Windows
        return Path(os.environ.get('APPDATA', '')) / 'Claude' / 'claude_desktop_config.json'
    elif sys.platform == 'darwin':  # macOS
        return Path.home() / 'Library' / 'Application Support' / 'Claude' / 'claude_desktop_config.json'
    else:  # Linux
        return Path.home() / '.config' / 'Claude' / 'claude_desktop_config.json'

def update_claude_config(token):
    """Update Claude Desktop configuration"""
    config_path = get_claude_config_path()
    
    # Create directory if it doesn't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Read existing config or create new one
    config = {}
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
        except:
            config = {}
    
    # Add lunchmoney-mcp server
    if 'mcpServers' not in config:
        config['mcpServers'] = {}
    
    config['mcpServers']['lunchmoney'] = {
        "command": "lunchmoney-mcp",
        "env": {
            "LUNCHMONEY_ACCESS_TOKEN": token
        }
    }
    
    # Write updated config
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✅ Updated Claude Desktop config: {config_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to update Claude Desktop config: {e}")
        return False

def main():
    """Main installation process"""
    print("🚀 Installing lunchmoney-mcp")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    # Try to install from PyPI first
    print("📦 Attempting to install from PyPI...")
    result = run_command("pip install lunchmoney-mcp", "Installing from PyPI")
    
    if result is None:
        # Fallback to local installation
        print("🔄 PyPI installation failed, trying local installation...")
        if not Path("pyproject.toml").exists():
            print("❌ pyproject.toml not found. Make sure you're in the project root directory.")
            sys.exit(1)
        
        result = run_command("pip install -e .", "Installing locally")
        if result is None:
            print("❌ Installation failed")
            sys.exit(1)
    
    # Test installation
    test_result = run_command("lunchmoney-mcp --help", "Testing installation")
    if test_result is None:
        print("❌ Installation test failed")
        sys.exit(1)
    
    print("\n🔑 Setting up Lunch Money token...")
    print("Get your token from: https://my.lunchmoney.app/developers")
    
    token = input("Enter your Lunch Money access token: ").strip()
    if not token:
        print("❌ No token provided. You'll need to configure it manually.")
        print("Add this to your Claude Desktop config:")
        print('"LUNCHMONEY_ACCESS_TOKEN": "your_token_here"')
        sys.exit(1)
    
    # Update Claude Desktop config
    if update_claude_config(token):
        print("\n🎉 Installation completed successfully!")
        print("✅ lunchmoney-mcp is installed and configured")
        print("✅ Claude Desktop config updated")
        print("\n🔄 Please restart Claude Desktop to use the new MCP server")
    else:
        print("\n⚠️  Installation completed but Claude Desktop config update failed")
        print("Please manually add this to your Claude Desktop config:")
        print(f'"LUNCHMONEY_ACCESS_TOKEN": "{token}"')

if __name__ == "__main__":
    main() 