# Lunch Money MCP Server

A Model Context Protocol (MCP) server for the [Lunch Money API](https://lunchmoney.dev), enabling AI assistants to interact with your Lunch Money account to manage transactions, categories, budgets, and more.

## Features

This MCP server provides access to the following Lunch Money functionalities:

- **User**: Get account information
- **Categories**: Create, read, update, and delete categories
- **Transactions**: Manage transactions (create, read, update, filter)
- **Tags**: Get all tags
- **Assets**: Manage accounts/assets
- **Budgets**: Get and update budgets
- **Recurring Items**: Get recurring transactions
- **Plaid Accounts**: Manage connected Plaid accounts
- **Crypto**: Manage crypto assets

## Super Simple Installation 🚀

### Option 1: Automatic Installation (Easiest)

```bash
python install.py
```

This script will:
- ✅ Install the package automatically
- ✅ Ask for your Lunch Money token
- ✅ Configure Claude Desktop automatically
- ✅ Everything ready to use

### Option 2: Manual Installation

```bash
pip install lunchmoney-mcp
```

Then add this configuration to your `claude_desktop_config.json` file:

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

**That's it!** 🎉 As simple as Playwright MCP.

### Get your access token:
1. Go to [https://my.lunchmoney.app/developers](https://my.lunchmoney.app/developers)
2. Create a new access token
3. Use it in the configuration above

## Installation from Source Code

If you prefer to install from source code:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd lunchmoney-mcp
   ```

2. **Install:**
   ```bash
   pip install -e .
   ```

3. **Configure in Claude Desktop:**
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

### Configuration file location:

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

## Usage

Once configured, you can use Claude Desktop to interact with your Lunch Money account. Here are some examples:

### Usage Examples

1. **Get user information:**
   ```
   "Show me my Lunch Money account information"
   ```

2. **View all categories:**
   ```
   "List all my Lunch Money categories"
   ```

3. **Create a new category:**
   ```
   "Create a new category called 'Entertainment' in Lunch Money"
   ```

4. **View recent transactions:**
   ```
   "Show me transactions from the last month"
   ```

5. **Create a transaction:**
   ```
   "Add a $50 transaction for 'XYZ Supermarket' in the 'Food' category"
   ```

6. **View budget:**
   ```
   "Show me this month's budget summary"
   ```

## Available Tools

### User
- `get_user`: Get user and account information

### Categories
- `get_all_categories`: Get all categories
- `get_single_category`: Get a specific category
- `create_category`: Create a new category
- `update_category`: Update an existing category
- `delete_category`: Delete a category

### Transactions
- `get_all_transactions`: Get all transactions (with filters)
- `get_single_transaction`: Get a specific transaction
- `insert_transactions`: Insert new transactions
- `update_transaction`: Update an existing transaction

### Tags
- `get_all_tags`: Get all tags

### Assets
- `get_all_assets`: Get all assets/accounts
- `create_asset`: Create a new asset/account
- `update_asset`: Update an existing asset

### Budgets
- `get_budget_summary`: Get budget summary
- `upsert_budget`: Create or update budget data

### Recurring Items
- `get_recurring_items`: Get all recurring items

### Plaid Accounts
- `get_all_plaid_accounts`: Get all Plaid accounts
- `trigger_plaid_fetch`: Trigger Plaid synchronization

### Crypto
- `get_all_crypto`: Get all crypto assets
- `update_manual_crypto`: Update a manual crypto asset

## Development

To contribute to development:

1. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

2. **Run tests:**
   ```bash
   pytest
   ```

3. **Format code:**
   ```bash
   black lunchmoney_mcp/
   ```

## Security

- Never share your Lunch Money access token
- Store your token in the `.env` file and make sure it's in your `.gitignore`
- The MCP server runs locally and doesn't send data to external services

## Limitations

- The Lunch Money API is in public beta, so there may be changes
- Some operations may have rate limits
- Changes made through the API are irreversible

## Support

If you encounter issues:

1. Verify that your access token is valid
2. Check the [official Lunch Money documentation](https://lunchmoney.dev)
3. Review the MCP server logs for specific errors

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Related Links

- [Lunch Money](https://lunchmoney.app)
- [Lunch Money API Documentation](https://lunchmoney.dev)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/desktop) 