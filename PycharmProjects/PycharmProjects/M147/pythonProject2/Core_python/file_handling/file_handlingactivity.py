def count_log(filename):
    critical_count = 0
    info_count = 0
    error_count = 0

    try:
        with open(r'logfile.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("CRITICAL"):
                    critical_count += 1
                elif line.startswith("INFO"):
                    info_count += 1
                elif line.startswith("ERROR"):
                    error_count += 1
        return critical_count, info_count, error_count

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None


log_filename = 'logfile.txt'
critical, info, error = count_log(log_filename)
if critical is not None:
    print(f"CRITICAL count: {critical}")
    print(f"INFO count: {info}")
    print(f"ERROR count: {error}")
#Output-
# CRITICAL count: 7
# INFO count: 5
# ERROR count: 5