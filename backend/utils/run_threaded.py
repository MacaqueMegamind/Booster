import threading


def run_threaded_function(function, *args):
    """
    Run function in a separate thread
    :param function: function to run
    :param args: arguments for function
    """
    thread = threading.Thread(target=function, args=args)
    thread.start()
    return thread
