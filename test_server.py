#!/usr/bin/env python3
"""Simple test script to verify the Lunch Money MCP server functionality"""

import os
import asyncio
import json
from lunchmoney_mcp.server import get_http_client
from dotenv import load_dotenv

load_dotenv()

async def test_connection():
    """Test basic connectivity to Lunch Money API"""
    try:
        async with get_http_client() as client:
            response = await client.get("/v1/me")
            response.raise_for_status()
            
            user_data = response.json()
            print("✅ Conexión exitosa a Lunch Money API")
            print(f"Usuario: {user_data.get('user_name', 'N/A')}")
            print(f"Email: {user_data.get('user_email', 'N/A')}")
            print(f"Cuenta: {user_data.get('budget_name', 'N/A')}")
            
    except Exception as e:
        print(f"❌ Error conectando a Lunch Money API: {e}")
        print("Verifica que LUNCHMONEY_ACCESS_TOKEN esté configurado correctamente")

async def test_categories():
    """Test getting categories"""
    try:
        async with get_http_client() as client:
            response = await client.get("/v1/categories")
            response.raise_for_status()
            
            categories = response.json()
            print(f"✅ Obtenidas {len(categories.get('categories', []))} categorías")
            
            # Show first few categories
            for i, cat in enumerate(categories.get('categories', [])[:3]):
                print(f"  - {cat.get('name', 'N/A')}")
                
    except Exception as e:
        print(f"❌ Error obteniendo categorías: {e}")

async def test_transactions():
    """Test getting transactions"""
    try:
        async with get_http_client() as client:
            response = await client.get("/v1/transactions", params={"limit": 5})
            response.raise_for_status()
            
            transactions = response.json()
            print(f"✅ Obtenidas {len(transactions.get('transactions', []))} transacciones")
            
            # Show first few transactions
            for i, trans in enumerate(transactions.get('transactions', [])[:3]):
                print(f"  - {trans.get('payee', 'N/A')}: {trans.get('amount', 'N/A')} {trans.get('currency', 'N/A')}")
                
    except Exception as e:
        print(f"❌ Error obteniendo transacciones: {e}")

async def main():
    """Run all tests"""
    if not os.getenv("LUNCHMONEY_ACCESS_TOKEN"):
        print("❌ LUNCHMONEY_ACCESS_TOKEN no está configurado")
        print("Crea un archivo .env con tu token de acceso")
        return
    
    print("🧪 Probando conectividad del servidor MCP de Lunch Money...\n")
    
    await test_connection()
    print()
    await test_categories()
    print()
    await test_transactions()
    print("\n✅ Pruebas completadas!")

if __name__ == "__main__":
    asyncio.run(main()) 