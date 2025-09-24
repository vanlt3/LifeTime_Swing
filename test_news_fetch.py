#!/usr/bin/env python3
"""
Test script for comprehensive news fetching for all symbols
This script demonstrates the enhanced news fetching capabilities.
"""

import sys
import os
import asyncio
from datetime import datetime

# Add the current directory to the path so we can import the bot
sys.path.append('/workspace')

# Import necessary components from the main bot file
from Bot_Trading_Swing import (
    NewsEconomicManager, 
    DailyNewsScheduler, 
    SYMBOLS,
    API_KEYS
)

async def test_news_fetching():
    """Test the news fetching functionality for all symbols"""
    
    print("🚀 Testing Enhanced News Fetching System")
    print("=" * 60)
    
    # Check if API keys are available
    print("\n🔑 API Keys Status:")
    for api_name, key in API_KEYS.items():
        if key and key != "DEMO_KEY" and len(key) > 10:
            print(f"   ✅ {api_name}: Configured")
        else:
            print(f"   ❌ {api_name}: Not configured or demo key")
    
    print(f"\n📋 Symbols to fetch news for ({len(SYMBOLS)}):")
    for i, symbol in enumerate(SYMBOLS, 1):
        print(f"   {i:2d}. {symbol}")
    
    try:
        # Initialize the news manager
        print("\n📰 Initializing News Manager...")
        news_manager = NewsEconomicManager()
        
        # Initialize the daily news scheduler with all symbols
        print("📅 Initializing Daily News Scheduler...")
        scheduler = DailyNewsScheduler(
            news_manager=news_manager,
            symbols_to_track=SYMBOLS
        )
        
        # Test manual news fetching
        print("\n🎯 Starting manual news fetch for all symbols...")
        start_time = datetime.now()
        
        scheduler.fetch_news_now()
        
        end_time = datetime.now()
        total_duration = (end_time - start_time).total_seconds()
        
        print(f"\n✅ News fetching test completed in {total_duration:.1f} seconds")
        
        # Check if news data directory was created
        news_dir = "/workspace/news_data"
        if os.path.exists(news_dir):
            print(f"📁 News data directory created: {news_dir}")
            
            # List contents
            for root, dirs, files in os.walk(news_dir):
                level = root.replace(news_dir, '').count(os.sep)
                indent = ' ' * 2 * level
                print(f"{indent}📂 {os.path.basename(root)}/")
                subindent = ' ' * 2 * (level + 1)
                for file in files[:5]:  # Show first 5 files
                    print(f"{subindent}📄 {file}")
                if len(files) > 5:
                    print(f"{subindent}... and {len(files) - 5} more files")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

def test_scheduler_configuration():
    """Test the scheduler configuration"""
    
    print("\n🔧 Testing Scheduler Configuration")
    print("-" * 40)
    
    try:
        # Create a mock news manager for testing
        class MockNewsManager:
            async def get_aggregated_news(self, symbol):
                # Simulate news fetching
                await asyncio.sleep(0.1)  # Simulate API call
                return [{"title": f"Test news for {symbol}", "summary": "Test summary"}]
        
        mock_manager = MockNewsManager()
        scheduler = DailyNewsScheduler(mock_manager, SYMBOLS)
        
        print(f"✅ Scheduler initialized with {len(scheduler.symbols_to_track)} symbols")
        print(f"📅 Fetch times (UTC): {scheduler.fetch_times}")
        print(f"📋 Symbols tracked: {', '.join(scheduler.symbols_to_track)}")
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")

if __name__ == "__main__":
    print("🔬 News Fetching System Test Suite")
    print("=" * 60)
    
    # Test scheduler configuration first
    test_scheduler_configuration()
    
    # Test actual news fetching
    asyncio.run(test_news_fetching())
    
    print("\n" + "=" * 60)
    print("🏁 Test suite completed!")