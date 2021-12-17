"""Constants for the Eye On Water integration."""
from datetime import timedelta

SCAN_INTERVAL = timedelta(minutes=1)
DEBOUNCE_COOLDOWN = 5*60  # Seconds

DATA_COORDINATOR = "coordinator"
DATA_SMART_METER = "smart_meter_data"

DOMAIN = "eyeonwater"

WATER_METER = "Water Meter"
WATER_LEAK_SENSOR = "Water Leak Sensor"