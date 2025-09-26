#!/usr/bin/env python3
"""
Quick Fix Script for "Too Many Values to Unpack" Error
This script provides a safe fix for the enhanced_risk_management unpacking error
"""

def create_safe_unpacking_fix():
    """
    Creates a safe unpacking function that can handle variable return values
    """
    
    fix_code = '''
def safe_enhanced_risk_management(self, symbol, signal, current_price, confidence):
    """
    Safe wrapper for enhanced_risk_management that handles variable return values
    """
    try:
        # Call the original method
        result = self.enhanced_risk_management(symbol, signal, current_price, confidence)
        
        # Handle different return formats
        if isinstance(result, (list, tuple)):
            if len(result) >= 2:
                tp, sl = result[0], result[1]
                
                # Log if there are extra values (for debugging)
                if len(result) > 2:
                    extra_values = result[2:]
                    self.logger.info(f"📊 [Risk Management] {symbol}: Extra values returned: {extra_values}")
                
                return tp, sl
            else:
                raise ValueError(f"Expected at least 2 values, got {len(result)}")
        else:
            raise ValueError(f"Expected tuple/list, got {type(result)}")
            
    except Exception as e:
        self.logger.error(f"❌ [Risk Management] Error for {symbol}: {e}")
        
        # Fallback to basic TP/SL calculation
        return self.calculate_fallback_tp_sl(symbol, signal, current_price)

def calculate_fallback_tp_sl(self, symbol, signal, current_price):
    """
    Fallback TP/SL calculation when enhanced_risk_management fails
    """
    try:
        # Basic risk management parameters
        risk_reward_ratio = 2.0
        default_risk_pips = 50
        
        # Determine pip value based on symbol
        if 'JPY' in symbol:
            pip_value = 0.01
        else:
            pip_value = 0.0001
        
        # Calculate SL and TP distances
        sl_distance = default_risk_pips * pip_value
        tp_distance = sl_distance * risk_reward_ratio
        
        if signal == 'BUY':
            sl = round(current_price - sl_distance, 5)
            tp = round(current_price + tp_distance, 5)
        else:  # SELL
            sl = round(current_price + sl_distance, 5)
            tp = round(current_price - tp_distance, 5)
        
        self.logger.info(f"📊 [Fallback TP/SL] {symbol}: TP={tp}, SL={sl}")
        return tp, sl
        
    except Exception as e:
        self.logger.error(f"❌ [Fallback TP/SL] Error for {symbol}: {e}")
        # Ultimate fallback - return None values to prevent trading
        return None, None
'''
    
    return fix_code

def create_handle_position_logic_fix():
    """
    Creates the fix for handle_position_logic method
    """
    
    fix_code = '''
# In handle_position_logic method, replace this line:
# tp, sl = self.enhanced_risk_management(symbol, signal, current_price, confidence)

# With this safe version:
try:
    tp, sl = self.safe_enhanced_risk_management(symbol, signal, current_price, confidence)
    
    # Validate TP/SL values
    if tp is None or sl is None:
        self.logger.warning(f"⚠️ [Position Logic] Invalid TP/SL for {symbol}, skipping trade")
        return None
        
    # Log successful TP/SL calculation
    self.logger.info(f"✅ [Position Logic] {symbol}: TP={tp}, SL={sl}")
    
except Exception as e:
    self.logger.error(f"❌ [Position Logic] Critical error for {symbol}: {e}")
    return None
'''
    
    return fix_code

def print_implementation_guide():
    """
    Prints step-by-step implementation guide
    """
    print("🔧 IMPLEMENTATION GUIDE")
    print("=" * 50)
    print()
    
    print("1. 📝 Add these methods to your EnhancedTradingBot class:")
    print()
    print(create_safe_unpacking_fix())
    print()
    
    print("2. 🔄 Replace the problematic line in handle_position_logic:")
    print()
    print(create_handle_position_logic_fix())
    print()
    
    print("3. ✅ Test the fix:")
    print("   - Run the bot with AUDUSD")
    print("   - Monitor logs for successful TP/SL calculations")
    print("   - Verify no 'too many values to unpack' errors")
    print()
    
    print("4. 🔍 Monitor all symbols:")
    print("   - AUDUSD (confirmed issue)")
    print("   - EURUSD, BTCUSD, XAUUSD (likely affected)")
    print("   - All other configured symbols")
    print()
    
    print("5. 📊 Expected log messages after fix:")
    print("   ✅ '[Position Logic] SYMBOL: TP=X.XXXX, SL=X.XXXX'")
    print("   📊 '[Risk Management] SYMBOL: Extra values returned: [...]'")
    print("   📊 '[Fallback TP/SL] SYMBOL: TP=X.XXXX, SL=X.XXXX'")

def analyze_symbol_impact():
    """
    Analyzes which symbols are likely affected
    """
    print("\n🎯 SYMBOL IMPACT ANALYSIS")
    print("=" * 50)
    
    symbols_analysis = {
        "AUDUSD": {"status": "🔴 CONFIRMED", "priority": "CRITICAL"},
        "EURUSD": {"status": "🟡 LIKELY", "priority": "HIGH"},
        "BTCUSD": {"status": "🟡 LIKELY", "priority": "HIGH"},
        "XAUUSD": {"status": "🟡 LIKELY", "priority": "HIGH"},
        "SPX500": {"status": "🟡 LIKELY", "priority": "HIGH"},
        "DE40": {"status": "🟡 LIKELY", "priority": "MEDIUM"},
        "USOIL": {"status": "🟡 LIKELY", "priority": "MEDIUM"},
        "AUDNZD": {"status": "🟡 LIKELY", "priority": "MEDIUM"},
        "ETHUSD": {"status": "🟡 LIKELY", "priority": "MEDIUM"}
    }
    
    print("Symbol Impact Assessment:")
    for symbol, info in symbols_analysis.items():
        print(f"  {info['status']} {symbol:<8} - Priority: {info['priority']}")
    
    print(f"\n📊 Summary:")
    print(f"  • Confirmed affected: 1 symbol (AUDUSD)")
    print(f"  • Likely affected: {len(symbols_analysis)-1} symbols")
    print(f"  • Total risk exposure: {len(symbols_analysis)} symbols")
    
    print(f"\n🚨 Recommendation: Apply fix to ALL symbols immediately")

def main():
    """
    Main function to display the complete fix
    """
    print("🚨 CRITICAL ERROR FIX")
    print("Error: too many values to unpack (expected 2)")
    print("Location: enhanced_risk_management method")
    print("=" * 60)
    
    analyze_symbol_impact()
    print_implementation_guide()
    
    print("\n" + "=" * 60)
    print("🎯 QUICK ACTION SUMMARY:")
    print("1. Add safe_enhanced_risk_management method")
    print("2. Add calculate_fallback_tp_sl method")
    print("3. Update handle_position_logic method")
    print("4. Test with AUDUSD first")
    print("5. Monitor all symbols")
    print("=" * 60)

if __name__ == "__main__":
    main()