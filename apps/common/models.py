import time


def get_uploaded_file_path(instance, filename):
    """
    Function that determines file path for specified file

    :param instance: instance of db object for which file is being saved
    :param filename: name of file
    :return: path to file
    """
    # Seconds since epoch
    current_time = str(round(time.time(), 0)).split('.')[0]

    return 'images/{}_{}'.format(current_time, filename)
