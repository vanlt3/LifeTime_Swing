#!/usr/bin/env python3
"""
Master Agent Usage Example
==========================

This example demonstrates how to use the Master Agent for TP/SL and trailing stop decisions.
The Master Agent is now integrated into your trading bot and will be called automatically.

Key Features:
1. Intelligent TP/SL level calculation based on multiple factors
2. Dynamic trailing stop activation based on market conditions  
3. Risk-reward optimization
4. Performance tracking and learning
5. Integration with specialist agents
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Example usage (this is already integrated in your bot)
def example_master_agent_usage():
    """
    Example of how the Master Agent works in your trading system
    """
    
    # The Master Agent is automatically initialized in EnhancedTradingBot
    # and used in the trading cycle
    
    print("🎯 Master Agent for TP/SL Decisions")
    print("=" * 50)
    
    # Example market data structure
    example_market_data = {
        'price_data': pd.DataFrame({
            'open': np.random.uniform(1.1000, 1.1100, 100),
            'high': np.random.uniform(1.1050, 1.1150, 100),
            'low': np.random.uniform(1.0950, 1.1050, 100),
            'close': np.random.uniform(1.1000, 1.1100, 100),
            'volume': np.random.randint(1000, 10000, 100)
        })
    }
    
    print("\n1. TP/SL Decision Process:")
    print("   📊 Gather market intelligence from specialist agents")
    print("   🔍 Calculate ATR-based levels")
    print("   📈 Analyze volatility-adjusted levels")  
    print("   📉 Consider trend-based adjustments")
    print("   🎯 Apply support/resistance constraints")
    print("   ⚖️ Optimize risk-reward ratio")
    print("   💾 Store decision for learning")
    
    print("\n2. Trailing Stop Decision Process:")
    print("   💰 Check profit threshold (>1.5%)")
    print("   📊 Assess trend strength")
    print("   🌊 Evaluate volatility level")
    print("   🚀 Confirm momentum direction")
    print("   🎯 Check S/R proximity")
    print("   ✅ Activate if conditions met")
    
    print("\n3. Learning & Adaptation:")
    print("   📈 Track TP/SL hit rates")
    print("   📊 Monitor win rates by symbol")
    print("   🎯 Adjust decision weights based on performance")
    print("   🧠 Learn from successful/failed patterns")
    print("   ⚖️ Optimize for better risk-reward ratios")
    
    print("\n4. Integration Points in Your Bot:")
    print("   🔄 Called during position opening for TP/SL levels")
    print("   ⏰ Checked every cycle for trailing stop activation") 
    print("   📊 Performance updated when positions close")
    print("   🎯 Weights adjusted based on outcomes")
    
    print("\n✅ Master Agent is fully integrated and ready!")

def master_agent_decision_factors():
    """
    Explain the decision factors used by the Master Agent
    """
    
    print("\n🧠 Master Agent Decision Factors")
    print("=" * 40)
    
    factors = {
        "ATR-Based Levels": {
            "weight": "30%",
            "description": "Uses Average True Range for volatility-adjusted TP/SL",
            "benefits": "Adapts to market volatility automatically"
        },
        "Volatility Analysis": {
            "weight": "25%", 
            "description": "Bollinger Bands position and ATR percentage",
            "benefits": "Wider stops in volatile markets, tighter in calm markets"
        },
        "Trend Strength": {
            "weight": "20%",
            "description": "Moving average alignment and trend confidence",
            "benefits": "Larger TP in strong trends, conservative in weak trends"
        },
        "Support/Resistance": {
            "weight": "15%",
            "description": "Key levels that may act as barriers",
            "benefits": "Places TP/SL near logical market levels"
        },
        "News Sentiment": {
            "weight": "10%",
            "description": "Market sentiment from news analysis",
            "benefits": "Adjusts for fundamental market drivers"
        }
    }
    
    for factor, details in factors.items():
        print(f"\n📊 {factor}")
        print(f"   Weight: {details['weight']}")
        print(f"   Method: {details['description']}")
        print(f"   Benefit: {details['benefits']}")

def trailing_stop_activation_rules():
    """
    Explain when the Master Agent activates trailing stops
    """
    
    print("\n🎯 Trailing Stop Activation Rules")
    print("=" * 35)
    
    rules = [
        {
            "rule": "Profit Threshold",
            "requirement": "Position must be >1.5% in profit",
            "importance": "Mandatory - prevents premature trailing",
            "score": "2 points"
        },
        {
            "rule": "Trend Strength", 
            "requirement": "Strong trend continuation (>0.7 confidence)",
            "importance": "High - ensures momentum support",
            "score": "1 point"
        },
        {
            "rule": "Volatility Check",
            "requirement": "Either high volatility (>0.7) or low volatility (<0.4)",
            "importance": "Medium - different strategies for different conditions",
            "score": "0.5 points"
        },
        {
            "rule": "Momentum Confirmation",
            "requirement": "RSI confirms direction (BUY: 50-80, SELL: 20-50)",
            "importance": "High - prevents counter-momentum trailing",
            "score": "1 point"
        },
        {
            "rule": "S/R Proximity",
            "requirement": "Price not too close to major support/resistance",
            "importance": "Medium - avoids trailing near reversal points",
            "score": "0.5 points"
        }
    ]
    
    print("Minimum Score Required: 2.5/5 points")
    print("Activation Decision: score >= 2.5\n")
    
    for rule in rules:
        print(f"📋 {rule['rule']} ({rule['score']})")
        print(f"   Requirement: {rule['requirement']}")
        print(f"   Importance: {rule['importance']}\n")

if __name__ == "__main__":
    example_master_agent_usage()
    master_agent_decision_factors() 
    trailing_stop_activation_rules()
    
    print("\n" + "="*60)
    print("🚀 Master Agent is now integrated into your trading bot!")
    print("   It will automatically make intelligent TP/SL decisions")
    print("   and manage trailing stops based on market conditions.")
    print("="*60)