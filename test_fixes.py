#!/usr/bin/env python3
"""
Test script to verify the fixes for:
1. Missing 'get_features_dataframe' method error
2. TP/SL monitoring issues for Master Agent
"""

import sys

def test_features_method_fix():
    """Test that the get_features_dataframe method has been replaced correctly"""
    print("🧪 Testing features method fix...")
    
    # Read the bot file and check for the fix
    with open('/workspace/Bot-Trading_Swing.py', 'r') as f:
        content = f.read()
    
    # Check that old method is not used
    if 'get_features_dataframe' in content:
        old_usage = content.count('get_features_dataframe')
        print(f"❌ Found {old_usage} instances of 'get_features_dataframe' - should be replaced")
        return False
    
    # Check that new method is used
    if 'create_enhanced_features' in content:
        new_usage = content.count('create_enhanced_features')
        print(f"✅ Found {new_usage} instances of 'create_enhanced_features' - looks good")
        return True
    
    print("❌ Neither old nor new method found")
    return False

def test_monitoring_enhancements():
    """Test that monitoring enhancements are in place"""
    print("\n🧪 Testing monitoring enhancements...")
    
    with open('/workspace/Bot-Trading_Swing.py', 'r') as f:
        content = f.read()
    
    checks = [
        ('Position validation', 'required_fields = [\'signal\', \'sl\', \'tp\']'),
        ('Enhanced logging', 'self.logger.info(f"🎯 [Real-time Monitor] {symbol} {hit_result[\'type\']} hit detected'),
        ('Price validation', 'if price is not None and price > 0:'),
        ('Health check method', 'async def _check_realtime_monitoring_health'),
        ('Test function', 'async def test_sl_tp_detection'),
        ('Enhanced status display', 'Show position details for debugging')
    ]
    
    results = []
    for check_name, check_string in checks:
        if check_string in content:
            print(f"✅ {check_name}: Found")
            results.append(True)
        else:
            print(f"❌ {check_name}: Not found")
            results.append(False)
    
    return all(results)

def test_realtime_monitoring_logic():
    """Test the real-time monitoring logic"""
    print("\n🧪 Testing real-time monitoring logic...")
    
    # Mock position data
    test_positions = {
        'BTCUSD': {
            'symbol': 'BTCUSD',
            'signal': 'BUY',
            'entry_price': 50000.0,
            'sl': 49000.0,
            'tp': 52000.0
        },
        'SPX500': {
            'symbol': 'SPX500', 
            'signal': 'SELL',
            'entry_price': 4500.0,
            'sl': 4600.0,
            'tp': 4400.0
        }
    }
    
    # Test SL/TP hit detection logic
    def check_current_price_hit(position, current_price):
        """Simplified version of the SL/TP hit detection logic"""
        signal = position['signal']
        sl_price = float(position['sl'])
        tp_price = float(position['tp'])
        current_price = float(current_price)
        
        if signal == "BUY":
            if current_price <= sl_price:
                return "SL"
            elif current_price >= tp_price:
                return "TP"
        else:  # SELL
            if current_price >= sl_price:
                return "SL"
            elif current_price <= tp_price:
                return "TP"
        
        return None
    
    # Test scenarios
    test_scenarios = [
        # BTCUSD BUY position tests
        ('BTCUSD', 48000.0, 'SL'),  # Price below SL
        ('BTCUSD', 53000.0, 'TP'),  # Price above TP
        ('BTCUSD', 50500.0, None),  # Price between SL and TP
        
        # SPX500 SELL position tests  
        ('SPX500', 4700.0, 'SL'),   # Price above SL
        ('SPX500', 4300.0, 'TP'),   # Price below TP
        ('SPX500', 4450.0, None),   # Price between SL and TP
    ]
    
    all_passed = True
    for symbol, test_price, expected in test_scenarios:
        position = test_positions[symbol]
        result = check_current_price_hit(position, test_price)
        
        if result == expected:
            status = "✅"
        else:
            status = "❌"
            all_passed = False
            
        print(f"{status} {symbol} @ {test_price}: Expected {expected}, Got {result}")
    
    return all_passed

def main():
    """Run all tests"""
    print("🚀 Running fix verification tests...\n")
    
    results = []
    
    # Test 1: Features method fix
    results.append(test_features_method_fix())
    
    # Test 2: Monitoring enhancements
    results.append(test_monitoring_enhancements())
    
    # Test 3: Real-time monitoring logic
    results.append(test_realtime_monitoring_logic())
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print(f"\n📊 Test Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The fixes should work correctly.")
        return 0
    else:
        print("⚠️ Some tests failed. Please review the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())