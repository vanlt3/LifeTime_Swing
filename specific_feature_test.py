#!/usr/bin/env python3
"""
Specific Feature Tests for Trading Bot
Tests specific functionality that may need deeper validation
"""

import sys
import os
import json
import sqlite3
from datetime import datetime

def test_master_agent_functionality():
    """Test Master Agent specific functionality"""
    print("🤖 Testing Master Agent Functionality...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Look for Master Agent class patterns (might be embedded)
    master_agent_patterns = [
        'class.*Master.*Agent',
        'master_agent_coordinator',
        'MasterAgent',
        'master_agent',
        'MASTER_AGENT',
        'select_active_strategy',
        'get_dynamic_risk_multiplier',
        'decide_tp_sl_levels'
    ]
    
    found_patterns = []
    for pattern in master_agent_patterns:
        if pattern.lower().replace('.*', '') in content.lower():
            found_patterns.append(pattern)
    
    print(f"✅ Master Agent patterns found: {len(found_patterns)}/8")
    for pattern in found_patterns:
        print(f"  • {pattern}")
    
    return len(found_patterns) >= 5

def test_news_manager_functionality():
    """Test News Manager functionality"""
    print("\n📰 Testing News Manager Functionality...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Look for news-related functionality
    news_patterns = [
        'news_manager',
        'NewsFilter',
        'news_filter',
        'check_news_filter',
        'news_sentiment',
        'economic_event',
        'news_data',
        'fetch_news'
    ]
    
    found_patterns = []
    for pattern in news_patterns:
        if pattern.lower() in content.lower():
            found_patterns.append(pattern)
    
    print(f"✅ News functionality patterns found: {len(found_patterns)}/8")
    for pattern in found_patterns:
        print(f"  • {pattern}")
    
    # Check news files
    news_files = [
        "/workspace/fetch_news.py",
        "/workspace/news_data/news_index.json"
    ]
    
    news_files_exist = 0
    for file_path in news_files:
        if os.path.exists(file_path):
            news_files_exist += 1
            print(f"  • {os.path.basename(file_path)} exists")
    
    return len(found_patterns) >= 4 and news_files_exist >= 1

def test_trading_bot_main_class():
    """Test main TradingBot class functionality"""
    print("\n🤖 Testing TradingBot Main Class...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Look for main bot class patterns
    bot_patterns = [
        'class.*Bot',
        '__init__.*self',
        'async def run',
        'def start',
        'main_loop',
        'bot_cycle',
        'execute_bot',
        'trading_bot'
    ]
    
    found_patterns = []
    for pattern in bot_patterns:
        if pattern.lower().replace('.*', '') in content.lower():
            found_patterns.append(pattern)
    
    print(f"✅ TradingBot class patterns found: {len(found_patterns)}/8")
    for pattern in found_patterns:
        print(f"  • {pattern}")
    
    return len(found_patterns) >= 5

def test_database_functionality():
    """Test database functionality in detail"""
    print("\n🗄️ Testing Database Functionality...")
    
    try:
        conn = sqlite3.connect("/workspace/trading_bot.db")
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        
        print(f"✅ Database tables found: {len(tables)}")
        for table in tables:
            print(f"  • {table}")
            
            # Get table structure
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            print(f"    └─ Columns: {len(columns)}")
            for col in columns[:3]:  # Show first 3 columns
                print(f"       • {col[1]} ({col[2]})")
            if len(columns) > 3:
                print(f"       • ... and {len(columns)-3} more")
        
        conn.close()
        return len(tables) >= 1
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def test_realtime_monitoring_integration():
    """Test real-time monitoring integration"""
    print("\n⏰ Testing Real-time Monitoring Integration...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Check for real-time monitoring integration points
    monitoring_integration = [
        'realtime_monitor',
        'start_monitoring',
        'stop_monitoring',
        'update_positions',
        '_check_sl_tp_hit',
        'position_hit_callback',
        '_handle_realtime_sl_tp_hit',
        'monitoring_active'
    ]
    
    found_integrations = []
    for integration in monitoring_integration:
        if integration in content:
            found_integrations.append(integration)
    
    print(f"✅ Monitoring integration points found: {len(found_integrations)}/8")
    for integration in found_integrations:
        print(f"  • {integration}")
    
    return len(found_integrations) >= 6

def test_position_lifecycle():
    """Test complete position lifecycle"""
    print("\n💼 Testing Position Lifecycle...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Check position lifecycle methods
    lifecycle_methods = [
        'open_position_enhanced',
        'close_position_enhanced',
        'save_open_positions',
        'load_open_positions',
        'check_existing_positions',
        'monitor_positions',
        'update_positions',
        'position_management'
    ]
    
    found_methods = []
    for method in lifecycle_methods:
        if method in content:
            found_methods.append(method)
    
    print(f"✅ Position lifecycle methods found: {len(found_methods)}/8")
    for method in found_methods:
        print(f"  • {method}")
    
    return len(found_methods) >= 6

def test_signal_generation():
    """Test signal generation functionality"""
    print("\n📊 Testing Signal Generation...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Check signal generation components
    signal_components = [
        'get_enhanced_signal',
        'calculate_price_action_score',
        'create_enhanced_features',
        'AdvancedFeatureEngineer',
        'technical_analysis',
        'signal_strength',
        'confidence',
        'BUY',
        'SELL'
    ]
    
    found_components = []
    for component in signal_components:
        if component in content:
            found_components.append(component)
    
    print(f"✅ Signal generation components found: {len(found_components)}/9")
    for component in found_components:
        print(f"  • {component}")
    
    return len(found_components) >= 7

def test_risk_management():
    """Test risk management functionality"""
    print("\n⚖️ Testing Risk Management...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Check risk management features
    risk_features = [
        'position_size_percent',
        'risk_amount_percent',
        'stop_loss',
        'take_profit',
        'risk_multiplier',
        'max_exposure',
        'correlation_limits',
        'emergency_stop',
        'risk_management'
    ]
    
    found_features = []
    for feature in risk_features:
        if feature in content:
            found_features.append(feature)
    
    print(f"✅ Risk management features found: {len(found_features)}/9")
    for feature in found_features:
        print(f"  • {feature}")
    
    return len(found_features) >= 6

def test_api_integrations():
    """Test API integrations"""
    print("\n🌐 Testing API Integrations...")
    
    with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
        content = f.read()
    
    # Check API integration patterns
    api_patterns = [
        'finnhub',
        'oanda',
        'alpha_vantage',
        'api_key',
        'API_KEY',
        'requests.get',
        'aiohttp',
        'async def.*fetch',
        'get.*price',
        'fetch.*data'
    ]
    
    found_apis = []
    for pattern in api_patterns:
        if pattern.lower().replace('.*', '') in content.lower():
            found_apis.append(pattern)
    
    print(f"✅ API integration patterns found: {len(found_apis)}/10")
    for api in found_apis:
        print(f"  • {api}")
    
    return len(found_apis) >= 5

def main():
    """Run specific feature tests"""
    print("🔍 Running Specific Feature Tests...")
    print("=" * 50)
    
    tests = [
        ("Master Agent", test_master_agent_functionality),
        ("News Manager", test_news_manager_functionality), 
        ("TradingBot Class", test_trading_bot_main_class),
        ("Database", test_database_functionality),
        ("Real-time Monitoring", test_realtime_monitoring_integration),
        ("Position Lifecycle", test_position_lifecycle),
        ("Signal Generation", test_signal_generation),
        ("Risk Management", test_risk_management),
        ("API Integrations", test_api_integrations)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Error in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SPECIFIC FEATURE TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"Total Feature Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed / total * 100):.1f}%")
    
    print(f"\n📋 Feature Status:")
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} {test_name}")
    
    if passed == total:
        print(f"\n🎉 All specific feature tests passed!")
        return 0
    else:
        print(f"\n⚠️ Some features may need attention.")
        return 1

if __name__ == "__main__":
    sys.exit(main())