#!/usr/bin/env python3
"""
Manual News Fetching Utility
============================

This utility allows you to manually fetch news for all trading symbols.
It provides the same output format as shown in the user's requirements.

Usage:
    python fetch_news.py                    # Fetch news for all symbols
    python fetch_news.py --symbols EURUSD   # Fetch news for specific symbol(s)
    python fetch_news.py --test             # Test mode (mock data)
"""

import sys
import os
import argparse
import asyncio
from datetime import datetime

# Add the current directory to the path
sys.path.append('/workspace')

try:
    # Try different import methods
    try:
        from Bot_Trading_Swing import (
            NewsEconomicManager, 
            DailyNewsScheduler, 
            SYMBOLS,
            API_KEYS
        )
    except ImportError:
        # Try with underscore replacement
        import importlib.util
        spec = importlib.util.spec_from_file_location("bot_module", "/workspace/Bot-Trading_Swing.py")
        bot_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bot_module)
        
        NewsEconomicManager = bot_module.NewsEconomicManager
        DailyNewsScheduler = bot_module.DailyNewsScheduler
        SYMBOLS = bot_module.SYMBOLS
        API_KEYS = bot_module.API_KEYS
        
except Exception as e:
    print(f"❌ Error importing required modules: {e}")
    print("This script requires the main trading bot file to be present.")
    
    # Fallback: use default symbols for demonstration
    print("🔄 Using fallback configuration for demonstration...")
    SYMBOLS = ["BTCUSD", "ETHUSD", "XAUUSD", "USOIL", "SPX500", "DE40", "EURUSD", "AUDUSD", "AUDNZD"]
    API_KEYS = {}
    NewsEconomicManager = None
    DailyNewsScheduler = None

class NewsUtility:
    """Utility class for manual news fetching"""
    
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.news_manager = None
        self.scheduler = None
    
    async def initialize(self):
        """Initialize the news components"""
        try:
            if self.test_mode:
                print("🧪 Running in test mode with mock data")
                return True
            
            print("🔄 Initializing news components...")
            self.news_manager = NewsEconomicManager()
            print("✅ News manager initialized")
            return True
            
        except Exception as e:
            print(f"❌ Failed to initialize: {e}")
            return False
    
    async def fetch_news_for_symbols(self, symbols=None):
        """Fetch news for specified symbols or all symbols"""
        
        if symbols is None:
            symbols = SYMBOLS
        elif isinstance(symbols, str):
            symbols = [symbols]
        
        print(f"\n📰 Fetching news for {len(symbols)} symbols...")
        start_time = datetime.now()
        
        total_news = 0
        successful_symbols = 0
        failed_symbols = []
        
        for i, symbol in enumerate(symbols, 1):
            try:
                print(f"🔍 [{i}/{len(symbols)}] Fetching news for {symbol}...")
                
                if self.test_mode:
                    # Mock data for testing
                    await asyncio.sleep(0.2)  # Simulate API call
                    news_items = [
                        {"title": f"Test news 1 for {symbol}", "summary": "Mock summary 1"},
                        {"title": f"Test news 2 for {symbol}", "summary": "Mock summary 2"}
                    ]
                else:
                    # Real news fetching
                    news_items = await self.news_manager.get_aggregated_news(symbol)
                
                if news_items:
                    total_news += len(news_items)
                    successful_symbols += 1
                    print(f"✅ {symbol}: {len(news_items)} news items")
                else:
                    print(f"⚠️ {symbol}: No news found")
                
                # Small delay to avoid rate limiting
                if not self.test_mode:
                    await asyncio.sleep(1)
                
            except Exception as e:
                print(f"❌ {symbol}: Error - {str(e)}")
                failed_symbols.append(symbol)
        
        # Calculate duration and display summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        self.display_summary(successful_symbols, len(symbols), total_news, duration, failed_symbols)
    
    def display_summary(self, successful, total, news_count, duration, failed_symbols):
        """Display the news fetch summary in the required format"""
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
        
        print("\n" + "="*50)
        print("📰 Daily News Update")
        print(f"News fetch completed at {current_time}")
        print("📊 Summary")
        print(f"Symbols: {successful}/{total}")
        print(f"News Items: {news_count}")
        print(f"Duration: {duration:.1f}s")
        print("Trading Bot - Daily News Scheduler")
        
        if failed_symbols:
            print(f"⚠️ Failed symbols: {', '.join(failed_symbols)}")
        
        print("="*50)

async def main():
    """Main function"""
    
    parser = argparse.ArgumentParser(description='Manual News Fetching Utility')
    parser.add_argument('--symbols', nargs='+', help='Specific symbols to fetch news for')
    parser.add_argument('--test', action='store_true', help='Run in test mode with mock data')
    parser.add_argument('--list-symbols', action='store_true', help='List all available symbols')
    
    args = parser.parse_args()
    
    if args.list_symbols:
        print("📋 Available symbols:")
        for i, symbol in enumerate(SYMBOLS, 1):
            print(f"   {i:2d}. {symbol}")
        return
    
    # Initialize the utility
    utility = NewsUtility(test_mode=args.test)
    
    if not await utility.initialize():
        print("❌ Failed to initialize news utility")
        return
    
    # Check API keys if not in test mode
    if not args.test:
        print("\n🔑 API Configuration:")
        configured_apis = 0
        for api_name, key in API_KEYS.items():
            if key and key != "DEMO_KEY" and len(key) > 10:
                print(f"   ✅ {api_name}")
                configured_apis += 1
            else:
                print(f"   ❌ {api_name}")
        
        if configured_apis == 0:
            print("\n⚠️ No API keys configured. Consider running with --test flag.")
            return
    
    # Fetch news
    symbols_to_fetch = args.symbols if args.symbols else None
    await utility.fetch_news_for_symbols(symbols_to_fetch)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ News fetching interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()