#!/usr/bin/env python3
"""Verification script to check if lunchmoney-mcp is properly set up"""

import os
import sys
import json
import subprocess
from pathlib import Path

def check_installation():
    """Check if lunchmoney-mcp is installed"""
    print("🔍 Checking installation...")
    
    try:
        result = subprocess.run(['lunchmoney-mcp', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✅ lunchmoney-mcp is installed: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ lunchmoney-mcp is not installed")
        print("   Install with: pip install lunchmoney-mcp")
        return False

def check_token():
    """Check if token is available"""
    print("🔍 Checking token...")
    
    token = os.getenv('LUNCHMONEY_ACCESS_TOKEN')
    if token:
        print(f"✅ Token found: {token[:8]}...")
        return True
    else:
        print("❌ LUNCHMONEY_ACCESS_TOKEN not found in environment")
        return False

def get_claude_config_path():
    """Get the Claude Desktop config path for the current OS"""
    if os.name == 'nt':  # Windows
        return Path(os.environ.get('APPDATA', '')) / 'Claude' / 'claude_desktop_config.json'
    elif sys.platform == 'darwin':  # macOS
        return Path.home() / 'Library' / 'Application Support' / 'Claude' / 'claude_desktop_config.json'
    else:  # Linux
        return Path.home() / '.config' / 'Claude' / 'claude_desktop_config.json'

def check_claude_config():
    """Check Claude Desktop configuration"""
    print("🔍 Checking Claude Desktop configuration...")
    
    config_path = get_claude_config_path()
    
    if not config_path.exists():
        print(f"❌ Claude Desktop config not found at: {config_path}")
        print("   Create the config file manually or run: python install.py")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        if 'mcpServers' not in config:
            print("❌ No mcpServers section in Claude Desktop config")
            return False
        
        if 'lunchmoney' not in config['mcpServers']:
            print("❌ lunchmoney server not configured in Claude Desktop")
            return False
        
        lm_config = config['mcpServers']['lunchmoney']
        
        # Check command
        if lm_config.get('command') != 'lunchmoney-mcp':
            print("❌ Wrong command in Claude Desktop config")
            print(f"   Expected: 'lunchmoney-mcp', Got: '{lm_config.get('command')}'")
            return False
        
        # Check token
        if 'env' not in lm_config or 'LUNCHMONEY_ACCESS_TOKEN' not in lm_config['env']:
            print("❌ LUNCHMONEY_ACCESS_TOKEN not set in Claude Desktop config")
            return False
        
        token = lm_config['env']['LUNCHMONEY_ACCESS_TOKEN']
        if not token or token == 'your_token_here' or token == 'replace_with_your_token':
            print("❌ Token not properly set in Claude Desktop config")
            print("   Update the token in your config file")
            return False
        
        print(f"✅ Claude Desktop config is correct: {config_path}")
        print(f"   Token: {token[:8]}...")
        return True
        
    except json.JSONDecodeError:
        print("❌ Claude Desktop config file is not valid JSON")
        return False
    except Exception as e:
        print(f"❌ Error reading Claude Desktop config: {e}")
        return False

def main():
    """Main verification process"""
    print("🔧 Lunch Money MCP Setup Verification")
    print("=" * 50)
    
    all_good = True
    
    # Check installation
    if not check_installation():
        all_good = False
    
    print()
    
    # Check token in environment (optional)
    check_token()
    
    print()
    
    # Check Claude Desktop config
    if not check_claude_config():
        all_good = False
    
    print()
    print("=" * 50)
    
    if all_good:
        print("🎉 Everything looks good!")
        print("✅ lunchmoney-mcp is properly installed and configured")
        print("🔄 Restart Claude Desktop if you haven't already")
        print("💬 You can now ask Claude about your Lunch Money data!")
    else:
        print("❌ Some issues found")
        print("📖 Check the errors above and fix them")
        print("🆘 Need help? Check QUICK_START.md or README.md")

if __name__ == "__main__":
    main() 