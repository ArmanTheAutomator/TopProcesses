# Top Processes by CPU or Memory

import psutil  # allows for retrieving process & system utilization info
import os  # allows for running OS commands, including terminating processes


def get_top_processes(resource, number):
    """
    This function gets the top N processes based on CPU or memory usage.

    param resource: string, either "cpu" or "memory" to specify resource.
    param number: Integer, the number of top processes to retrieve.

    :return:
    A list of tuples, where each tuple contains:
        - Process object from psutil
        - Resource usage percentage (CPU) or usage in MB (memory)
    """
    processes = []
    for process in psutil.process_iter():
        try:
            if resource == "cpu":
                cpu_usage = process.cpu_percent()
            elif resource == "memory":
                memory_usage = process.memory_info().rss / (1024 * 1024)  # memory usage in MB
            else:
                raise ValueError("Invalid resource specified")
            processes.append((process, cpu_usage if resource == "cpu" else memory_usage))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass  # Ignore processes that cannot be accessed

    processes.sort(key=lambda p: p[1], reverse=True)  # Sort by usage in descending order
    return processes[:number]  # Return the top N processes


def display_top_processes(processes, resource):
    """
    This function displays information about the top processes.

    param processes: List of tuples as returned by get_top_processes function.
    param resource: String, either "cpu" or "memory" to specify the resource.
    """
    print(f"Top 5 processes by {resource.upper()} usage: ")
    for i, (process, usage) in enumerate(processes, start=1):
        print(
            f"{i}. {process.name()} - {usage:.1f}% CPU" if resource == "cpu"
            else f"{i}. {process.name()} - {usage:.1f} MB Memory"
        )


def terminate_process(process):
    """
    This function terminates a process using its PID and os.kill.

    param process: psutil.process pbject representing the process to terminate.
    """
    try:
        process_name = process.name()  # Try to get name, but handle potential exception.
    except psutil.NoSuchProcess:
        process_name = f"(PID: {process.pid})"  # Usage PID as fallback

    try:
        os.kill(process.pid, 15)  # SIGTERM signal for termination request
        print(f"Process {process_name} terminated successfully.")
    except (PermissionError, ProcessLookupError):
        print(f"Error terminating process {process_name}.")


def run_process_manager():
    # Get User input for resource type (CPU or Memory)
    resource = input("Enter 'cpu' to monitor CPU usage or 'memory' to monitor memory usage: ").lower()
    if resource not in ("cpu", "memory"):
        print("Invalid resource specified. Please enter 'cpu' or 'memory'.")
        return

    # Get top 5 processes
    top_processes = get_top_processes(resource, 5)

    # Display top processes
    display_top_processes(top_processes, resource)

    # Get user choice for termination
    choice = input("Enter the number (1-5) of the process to terminate, or '0' to quit: ")
    if not choice.isdigit() or int(choice) < 0 or int(choice) > 5:
        print("Invalid choice. Please enter a number between 1 and 5, or 0 to quit.")
        return

    if int(choice) == 0:
        print("Exiting script.")
        return

    # Terminate chosen process
    process = top_processes[int(choice) - 1][0]
    terminate_process(process)


# Run the process manager
run_process_manager()
