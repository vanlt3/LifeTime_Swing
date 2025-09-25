#!/usr/bin/env python3
"""
MasterAgent Fix - Temporary solution for the missing select_active_strategy method
This provides a minimal implementation to fix the AttributeError
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, Optional

class MasterAgent:
    """
    Master Agent for strategy selection and TP/SL decisions
    This is a minimal implementation to fix the missing select_active_strategy method
    """
    
    def __init__(self):
        """Initialize the Master Agent"""
        self.strategies = ['trending', 'ranging', 'breakout', 'reversal']
        self.performance_history = {}
        self.active_strategies = {}
        
    def select_active_strategy(self, symbol: str, features_df: pd.DataFrame) -> str:
        """
        Select the most appropriate strategy for the given symbol and market conditions
        
        Args:
            symbol: Trading symbol (e.g., 'EURUSD')
            features_df: DataFrame containing market features and indicators
            
        Returns:
            str: Selected strategy name ('trending', 'ranging', 'breakout', 'reversal')
        """
        try:
            if features_df is None or features_df.empty:
                return 'trending'  # Default fallback
                
            # Get the latest market conditions
            latest_row = features_df.iloc[-1] if len(features_df) > 0 else None
            
            if latest_row is None:
                return 'trending'  # Default fallback
            
            # Strategy selection logic based on market conditions
            strategy_scores = {
                'trending': 0,
                'ranging': 0, 
                'breakout': 0,
                'reversal': 0
            }
            
            # Check for trending conditions
            if 'trend_strength' in latest_row:
                trend_strength = latest_row.get('trend_strength', 0)
                if trend_strength > 0.6:
                    strategy_scores['trending'] += 2
                elif trend_strength < 0.3:
                    strategy_scores['ranging'] += 2
                    
            # Check for volatility (breakout indicator)
            if 'volatility' in latest_row:
                volatility = latest_row.get('volatility', 0)
                if volatility > 0.7:
                    strategy_scores['breakout'] += 2
                elif volatility < 0.3:
                    strategy_scores['ranging'] += 1
                    
            # Check for mean reversion signals
            if 'rsi' in latest_row:
                rsi = latest_row.get('rsi', 50)
                if rsi > 80 or rsi < 20:
                    strategy_scores['reversal'] += 2
                elif 30 < rsi < 70:
                    strategy_scores['trending'] += 1
                    
            # Check for range-bound conditions
            if 'bb_position' in latest_row:
                bb_position = latest_row.get('bb_position', 0.5)
                if 0.2 < bb_position < 0.8:
                    strategy_scores['ranging'] += 1
                    
            # Select the strategy with the highest score
            selected_strategy = max(strategy_scores.items(), key=lambda x: x[1])[0]
            
            # Store the selection for tracking
            self.active_strategies[symbol] = selected_strategy
            
            return selected_strategy
            
        except Exception as e:
            print(f"⚠️ [MasterAgent] Error in select_active_strategy: {e}")
            return 'trending'  # Safe fallback
    
    def calculate_tp_sl_levels(self, symbol: str, signal: str, entry_price: float, 
                              features_df: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate TP and SL levels based on market conditions
        
        Args:
            symbol: Trading symbol
            signal: 'BUY' or 'SELL'
            entry_price: Entry price for the position
            features_df: Market features DataFrame
            
        Returns:
            Dict with 'tp' and 'sl' levels
        """
        try:
            # Default risk-reward ratio
            risk_reward_ratio = 2.0
            default_risk_pips = 50
            
            # Get ATR if available for dynamic levels
            atr = 50  # Default ATR in pips
            if features_df is not None and not features_df.empty:
                latest_row = features_df.iloc[-1]
                if 'atr' in latest_row:
                    atr = latest_row.get('atr', 50)
                elif 'atr_pips' in latest_row:
                    atr = latest_row.get('atr_pips', 50)
            
            # Calculate SL and TP based on ATR
            sl_distance = max(atr * 1.5, default_risk_pips)  # 1.5x ATR or minimum 50 pips
            tp_distance = sl_distance * risk_reward_ratio
            
            # Convert pips to price levels
            pip_value = 0.0001 if 'JPY' not in symbol else 0.01
            
            if signal == 'BUY':
                sl_level = entry_price - (sl_distance * pip_value)
                tp_level = entry_price + (tp_distance * pip_value)
            else:  # SELL
                sl_level = entry_price + (sl_distance * pip_value)
                tp_level = entry_price - (tp_distance * pip_value)
            
            return {
                'tp': round(tp_level, 5),
                'sl': round(sl_level, 5)
            }
            
        except Exception as e:
            print(f"⚠️ [MasterAgent] Error calculating TP/SL: {e}")
            # Return safe default levels
            pip_value = 0.0001 if 'JPY' not in symbol else 0.01
            if signal == 'BUY':
                return {
                    'tp': round(entry_price + (100 * pip_value), 5),
                    'sl': round(entry_price - (50 * pip_value), 5)
                }
            else:
                return {
                    'tp': round(entry_price - (100 * pip_value), 5),
                    'sl': round(entry_price + (50 * pip_value), 5)
                }
    
    def should_activate_trailing_stop(self, symbol: str, position: Dict[str, Any], 
                                    current_price: float, features_df: pd.DataFrame) -> bool:
        """
        Determine if trailing stop should be activated for a position
        
        Args:
            symbol: Trading symbol
            position: Position details
            current_price: Current market price
            features_df: Market features DataFrame
            
        Returns:
            bool: True if trailing stop should be activated
        """
        try:
            signal = position.get('signal', 'BUY')
            entry_price = position.get('entry_price', current_price)
            
            # Calculate current profit percentage
            if signal == 'BUY':
                profit_pct = (current_price - entry_price) / entry_price * 100
            else:
                profit_pct = (entry_price - current_price) / entry_price * 100
            
            # Minimum profit threshold for trailing stop activation
            min_profit_threshold = 1.5  # 1.5%
            
            if profit_pct < min_profit_threshold:
                return False
            
            # Additional conditions for trailing stop activation
            activation_score = 0
            
            # Check trend strength
            if features_df is not None and not features_df.empty:
                latest_row = features_df.iloc[-1]
                
                trend_strength = latest_row.get('trend_strength', 0.5)
                if trend_strength > 0.7:
                    activation_score += 1
                
                # Check volatility
                volatility = latest_row.get('volatility', 0.5)
                if volatility > 0.7 or volatility < 0.4:
                    activation_score += 0.5
                
                # Check momentum
                rsi = latest_row.get('rsi', 50)
                if signal == 'BUY' and 50 < rsi < 80:
                    activation_score += 1
                elif signal == 'SELL' and 20 < rsi < 50:
                    activation_score += 1
            
            # Activate if score is sufficient
            return activation_score >= 1.5
            
        except Exception as e:
            print(f"⚠️ [MasterAgent] Error in trailing stop decision: {e}")
            return False

# Example of how to integrate this into the bot
def integrate_master_agent_fix():
    """
    Instructions for integrating the MasterAgent fix into the main bot file
    """
    print("🔧 MasterAgent Integration Fix")
    print("=" * 40)
    print()
    print("To fix the 'select_active_strategy' AttributeError:")
    print()
    print("1. Add the MasterAgent class to your Bot-Trading_Swing.py file")
    print("2. Initialize it in the EnhancedTradingBot.__init__ method:")
    print("   self.master_agent_coordinator = MasterAgent()")
    print()
    print("3. The select_active_strategy method will now be available")
    print("4. Additional methods are provided for TP/SL and trailing stops")
    print()
    print("This fix provides:")
    print("✅ select_active_strategy method")
    print("✅ calculate_tp_sl_levels method")  
    print("✅ should_activate_trailing_stop method")
    print("✅ Error handling and safe fallbacks")

if __name__ == "__main__":
    integrate_master_agent_fix()