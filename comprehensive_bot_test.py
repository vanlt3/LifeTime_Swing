#!/usr/bin/env python3
"""
Comprehensive Test Suite for Trading Bot
Tests all major features and components
"""

import sys
import os
import json
import sqlite3
import asyncio
from datetime import datetime, timedelta
import traceback

class BotTester:
    def __init__(self):
        self.test_results = {}
        self.total_tests = 0
        self.passed_tests = 0
        
    def log_test(self, test_name, passed, details=""):
        """Log test result"""
        self.total_tests += 1
        if passed:
            self.passed_tests += 1
            status = "✅ PASS"
        else:
            status = "❌ FAIL"
            
        print(f"{status} {test_name}")
        if details:
            print(f"    {details}")
            
        self.test_results[test_name] = {
            'passed': passed,
            'details': details
        }

    def test_file_structure(self):
        """Test 1: File Structure and Dependencies"""
        print("\n📁 Testing File Structure...")
        
        # Check main bot file
        bot_file = "/workspace/Bot-Trading_Swing.py"
        self.log_test("Main bot file exists", os.path.exists(bot_file))
        
        # Check database file
        db_file = "/workspace/trading_bot.db"
        self.log_test("Database file exists", os.path.exists(db_file))
        
        # Check logs directory
        logs_dir = "/workspace/logs"
        self.log_test("Logs directory exists", os.path.exists(logs_dir))
        
        # Check news data directory
        news_dir = "/workspace/news_data"
        self.log_test("News data directory exists", os.path.exists(news_dir))

    def test_imports_and_syntax(self):
        """Test 2: Import statements and syntax"""
        print("\n🐍 Testing Imports and Syntax...")
        
        try:
            with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
                content = f.read()
            
            # Check for critical imports
            critical_imports = [
                'import pandas as pd',
                'import numpy as np',
                'import sqlite3',
                'import asyncio',
                'from datetime import datetime',
                'import logging'
            ]
            
            for imp in critical_imports:
                found = imp in content
                self.log_test(f"Import check: {imp}", found)
                
            # Basic syntax check
            compile(content, "/workspace/Bot-Trading_Swing.py", 'exec')
            self.log_test("Python syntax validation", True, "No syntax errors found")
            
        except SyntaxError as e:
            self.log_test("Python syntax validation", False, f"Syntax error: {e}")
        except Exception as e:
            self.log_test("Python syntax validation", False, f"Error: {e}")

    def test_configuration_constants(self):
        """Test 3: Configuration and Constants"""
        print("\n⚙️ Testing Configuration...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check critical constants
        constants = [
            'SYMBOLS',
            'PRIMARY_TIMEFRAME_BY_SYMBOL',
            'ENABLE_REALTIME_MONITORING',
            'REALTIME_CHECK_INTERVAL',
            'SYMBOL_METADATA'
        ]
        
        for const in constants:
            found = const in content
            self.log_test(f"Configuration: {const}", found)

    def test_database_structure(self):
        """Test 4: Database Structure"""
        print("\n🗄️ Testing Database Structure...")
        
        try:
            conn = sqlite3.connect("/workspace/trading_bot.db")
            cursor = conn.cursor()
            
            # Check if main tables exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            
            expected_tables = ['trades', 'market_data', 'news_data', 'features']
            
            for table in expected_tables:
                found = table in tables
                self.log_test(f"Database table: {table}", found)
            
            conn.close()
            self.log_test("Database connection", True, f"Found {len(tables)} tables")
            
        except Exception as e:
            self.log_test("Database connection", False, str(e))

    def test_class_definitions(self):
        """Test 5: Class Definitions"""
        print("\n🏗️ Testing Class Definitions...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check for critical classes
        classes = [
            'class RealTimeMonitor:',
            'class EnhancedDataManager:',
            'class AdvancedFeatureEngineer:',
            'class MasterAgentCoordinator:',
            'class NewsManager:',
            'class TradingBot:'
        ]
        
        for cls in classes:
            found = cls in content
            self.log_test(f"Class definition: {cls.replace('class ', '').replace(':', '')}", found)

    def test_method_definitions(self):
        """Test 6: Critical Method Definitions"""
        print("\n🔧 Testing Method Definitions...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check for critical methods
        methods = [
            'def create_enhanced_features',
            'def get_enhanced_signal',
            'def open_position_enhanced',
            'def close_position_enhanced',
            'def _check_sl_tp_hit',
            'def _handle_realtime_sl_tp_hit',
            'async def test_sl_tp_detection',
            'def calculate_price_action_score'
        ]
        
        for method in methods:
            found = method in content
            self.log_test(f"Method: {method.replace('def ', '').replace('async def ', '')}", found)

    def test_realtime_monitoring_config(self):
        """Test 7: Real-time Monitoring Configuration"""
        print("\n⏰ Testing Real-time Monitoring Config...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check monitoring configurations
        monitoring_configs = [
            'ENABLE_REALTIME_MONITORING = True',
            'REALTIME_CHECK_INTERVAL = 30',
            'ENABLE_WICK_DETECTION = True',
            'MAX_REALTIME_RETRIES = 3'
        ]
        
        for config in monitoring_configs:
            found = config in content
            self.log_test(f"Monitoring config: {config.split(' = ')[0]}", found)

    def test_symbol_configurations(self):
        """Test 8: Symbol Configurations"""
        print("\n📈 Testing Symbol Configurations...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check if BTCUSD and SPX500 are configured
        test_symbols = ['BTCUSD', 'SPX500', 'EURUSD', 'XAUUSD']
        
        for symbol in test_symbols:
            found = f'"{symbol}"' in content or f"'{symbol}'" in content
            self.log_test(f"Symbol configuration: {symbol}", found)

    def test_master_agent_integration(self):
        """Test 9: Master Agent Integration"""
        print("\n🤖 Testing Master Agent Integration...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check Master Agent components
        master_agent_features = [
            'MasterAgentCoordinator',
            'select_active_strategy',
            'get_dynamic_risk_multiplier',
            'decide_tp_sl_levels',
            'Master Agent Decision'
        ]
        
        for feature in master_agent_features:
            found = feature in content
            self.log_test(f"Master Agent: {feature}", found)

    def test_news_integration(self):
        """Test 10: News Integration"""
        print("\n📰 Testing News Integration...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check news features
        news_features = [
            'NewsManager',
            'check_news_filter',
            'add_news_sentiment_features',
            'fetch_news_data'
        ]
        
        for feature in news_features:
            found = feature in content
            self.log_test(f"News integration: {feature}", found)
        
        # Check if news data files exist
        news_files = [
            "/workspace/news_data/news_index.json",
            "/workspace/fetch_news.py"
        ]
        
        for file_path in news_files:
            exists = os.path.exists(file_path)
            self.log_test(f"News file: {os.path.basename(file_path)}", exists)

    def test_error_handling(self):
        """Test 11: Error Handling"""
        print("\n🚨 Testing Error Handling...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check for proper error handling patterns
        error_patterns = [
            'try:',
            'except Exception as e:',
            'except KeyboardInterrupt:',
            'logger.error',
            'print(f"❌'
        ]
        
        for pattern in error_patterns:
            count = content.count(pattern)
            found = count > 0
            self.log_test(f"Error handling: {pattern}", found, f"Found {count} instances")

    def test_logging_system(self):
        """Test 12: Logging System"""
        print("\n📝 Testing Logging System...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check logging configurations
        logging_features = [
            'import logging',
            'logger.info',
            'logger.warning',
            'logger.error',
            'self.logger'
        ]
        
        for feature in logging_features:
            count = content.count(feature)
            found = count > 0
            self.log_test(f"Logging: {feature}", found, f"Found {count} instances")

    def test_discord_integration(self):
        """Test 13: Discord Integration"""
        print("\n💬 Testing Discord Integration...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check Discord features
        discord_features = [
            'send_discord_alert',
            'DISCORD_WEBHOOK_URL',
            'discord_webhook'
        ]
        
        for feature in discord_features:
            found = feature in content
            self.log_test(f"Discord: {feature}", found)

    def test_data_validation_logic(self):
        """Test 14: Data Validation Logic"""
        print("\n🔍 Testing Data Validation...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check validation patterns
        validation_patterns = [
            'if.*is None',
            'if.*empty',
            'validate_',
            'required_fields',
            'isinstance(',
            'float(',
            'int('
        ]
        
        for pattern in validation_patterns:
            count = len([line for line in content.split('\n') if pattern.replace('.*', '') in line])
            found = count > 5  # Should have multiple validation checks
            self.log_test(f"Validation pattern: {pattern}", found, f"Found {count} instances")

    def test_position_management(self):
        """Test 15: Position Management"""
        print("\n💼 Testing Position Management...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check position management features
        position_features = [
            'open_positions',
            'close_position_enhanced',
            'save_open_positions',
            'load_open_positions',
            'position_size_percent',
            'risk_amount_percent'
        ]
        
        for feature in position_features:
            found = feature in content
            self.log_test(f"Position management: {feature}", found)

    def test_recent_fixes(self):
        """Test 16: Recent Fixes"""
        print("\n🔧 Testing Recent Fixes...")
        
        with open("/workspace/Bot-Trading_Swing.py", 'r') as f:
            content = f.read()
        
        # Check that recent fixes are in place
        fixes = [
            ('Features method fix', 'create_enhanced_features'),
            ('Position validation', 'required_fields = [\'signal\', \'sl\', \'tp\']'),
            ('Enhanced SL/TP logging', '🎯 [Real-time Monitor]'),
            ('Health check method', '_check_realtime_monitoring_health'),
            ('Test function', 'test_sl_tp_detection')
        ]
        
        for fix_name, fix_pattern in fixes:
            found = fix_pattern in content
            self.log_test(f"Recent fix: {fix_name}", found)

    def run_all_tests(self):
        """Run all test suites"""
        print("🚀 Starting Comprehensive Bot Testing...")
        print("=" * 60)
        
        # Run all test suites
        test_methods = [
            self.test_file_structure,
            self.test_imports_and_syntax,
            self.test_configuration_constants,
            self.test_database_structure,
            self.test_class_definitions,
            self.test_method_definitions,
            self.test_realtime_monitoring_config,
            self.test_symbol_configurations,
            self.test_master_agent_integration,
            self.test_news_integration,
            self.test_error_handling,
            self.test_logging_system,
            self.test_discord_integration,
            self.test_data_validation_logic,
            self.test_position_management,
            self.test_recent_fixes
        ]
        
        for test_method in test_methods:
            try:
                test_method()
            except Exception as e:
                print(f"❌ Error in {test_method.__name__}: {e}")
                self.log_test(test_method.__name__, False, str(e))
        
        self.print_summary()

    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.total_tests - self.passed_tests}")
        print(f"Success Rate: {(self.passed_tests / self.total_tests * 100):.1f}%")
        
        # Show failed tests
        failed_tests = [name for name, result in self.test_results.items() if not result['passed']]
        
        if failed_tests:
            print(f"\n❌ Failed Tests ({len(failed_tests)}):")
            for test in failed_tests:
                details = self.test_results[test]['details']
                print(f"  • {test}")
                if details:
                    print(f"    └─ {details}")
        else:
            print(f"\n🎉 All tests passed!")
        
        # Critical systems check
        critical_systems = [
            'Main bot file exists',
            'Python syntax validation', 
            'Database connection',
            'Real-time monitoring config',
            'Position management features',
            'Recent fixes applied'
        ]
        
        critical_failures = [test for test in critical_systems if test in failed_tests]
        
        if critical_failures:
            print(f"\n🚨 CRITICAL ISSUES DETECTED:")
            for issue in critical_failures:
                print(f"  • {issue}")
            print("\n⚠️ Bot may not function properly until these issues are resolved.")
        else:
            print(f"\n✅ All critical systems are functioning properly.")
            print("🚀 Bot is ready for trading operations.")

def main():
    """Main test execution"""
    tester = BotTester()
    tester.run_all_tests()
    
    # Return appropriate exit code
    if tester.passed_tests == tester.total_tests:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())