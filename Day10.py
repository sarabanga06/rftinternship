# Simple Log Counter

logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Counters
error_count = 0
info_count = 0
warning_count = 0

# List to store log types
log_types = []

# Process logs
for log in logs:
    log.upper()
    
    if "ERROR" in log:
        error_count += 1
        log_types.append("ERROR")
    elif "INFO" in log:
        info_count += 1
        log_types.append("INFO")
    elif "WARNING" in log:
        warning_count += 1
        log_types.append("WARNING")
        
# Display counts
print("ERROR Count =", error_count)
print("INFO Count =", info_count)
print("WARNING Count =", warning_count)

# Find most frequent log type
max_count = max(error_count, info_count, warning_count)

if max_count == error_count:
    print("Most Frequent Log Type: ERROR")
elif max_count == info_count:
    print("Most Frequent Log Type: INFO")
else:
    print("Most Frequent Log Type: WARNING")