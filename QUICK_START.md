# 🚀 Quick Start Guide

## ⚡ Super Simple Installation (Like Playwright MCP)

### Step 1: Install the package
```bash
pip install lunchmoney-mcp
```

### Step 2: Get your Lunch Money token
1. Go to [https://my.lunchmoney.app/developers](https://my.lunchmoney.app/developers)
2. Create a new access token
3. Copy the token

### Step 3: Configure Claude Desktop
Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "lunchmoney": {
      "command": "lunchmoney-mcp",
      "env": {
        "LUNCHMONEY_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

### Step 4: Restart Claude Desktop
🔄 Restart Claude Desktop and you're ready to go!

## 📂 Where to find claude_desktop_config.json

| OS | Path |
|---|---|
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Linux** | `~/.config/Claude/claude_desktop_config.json` |

## 🎯 Example Usage

Once configured, you can ask Claude:

### View your finances
- "Show me my Lunch Money account info"
- "What are my spending categories?"
- "Show me this month's transactions"

### Create transactions
- "Add a $50 grocery expense to my Food category"
- "Record a $1200 salary payment as income"

### Manage categories
- "Create a new category called 'Entertainment'"
- "Show me all my expense categories"

### Budget tracking
- "Show me my budget for this month"
- "What's my spending vs budget in the Food category?"

## 🔧 Alternative Installation Methods

### Option A: Auto-installer (Recommended)
```bash
python install.py
```
*This will install everything and configure Claude Desktop automatically*

### Option B: Development Installation
```bash
git clone https://github.com/yourusername/lunchmoney-mcp
cd lunchmoney-mcp
pip install -e .
```

### Option C: From Source
```bash
git clone https://github.com/yourusername/lunchmoney-mcp
cd lunchmoney-mcp
pip install -r requirements.txt
python -m lunchmoney_mcp.server
```

## 🧪 Test Your Installation

```bash
# Test the command works
lunchmoney-mcp --help

# Test with your token
LUNCHMONEY_ACCESS_TOKEN=your_token python test_server.py
```

## 🔥 Pro Tips

1. **Keep your token secure** - Never share or commit it to version control
2. **Use environment variables** - Set `LUNCHMONEY_ACCESS_TOKEN` in your shell profile
3. **Test first** - Run the test script to verify everything works
4. **Backup your config** - Save your `claude_desktop_config.json` somewhere safe

## 🆘 Troubleshooting

### "Command not found: lunchmoney-mcp"
- Make sure you installed with `pip install lunchmoney-mcp`
- Check that your Python scripts directory is in your PATH

### "LUNCHMONEY_ACCESS_TOKEN environment variable is required"
- Make sure you set the token in your Claude Desktop config
- Test with: `LUNCHMONEY_ACCESS_TOKEN=your_token lunchmoney-mcp --help`

### "HTTP 401: Unauthorized"
- Your token might be invalid or expired
- Generate a new token at https://my.lunchmoney.app/developers

### Claude Desktop doesn't see the server
- Make sure the config file is in the right location
- Restart Claude Desktop after making changes
- Check the config file syntax is valid JSON

## 🎉 You're Ready!

That's it! Your Lunch Money MCP server is now as simple to use as Playwright MCP. Just one command and one config entry, and you're managing your finances with AI! 🚀 