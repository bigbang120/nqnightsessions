# enq-night-sessions config setup

# Environment Variables
SYMBOL = "NQ"              # Full E-mini Nasdaq futures contract (or broker specific ticker)
LOT_SIZE = 2.0             # Let's launch with 1 full contract to test the logic safely
MAGIC_NUMBER = 882026      # Unique bot identifier for MT5 tracking

# Session Timing (EST / Asian Session Window)
START_TIME = "19:00"       # Start monitoring breakouts
END_TIME = "23:00"         # Hard close session cut-off

# Risk Thresholds (Tailored for NQ $20/point scaling)
TARGET_PROFIT_POINTS = 40  # $800 target profit per trade
STOP_LOSS_POINTS = 20      # $400 maximum risk window per trade
