# Objective:
# 1. Write function that read binary file and return data
# 2.Measure time required
import logging
import time

# Create logger
logging.basicConfig(filename="problem.log", level=logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    '''
    Return the content of the file in the path and measure time required.
    '''
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        print("The path of the file is not existed!")
        raise Exception("File not found")
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("time required for {file} = {time}".format(file=path, time=dt))


read_file_timed("FileToRead.txt")
# read_file_timed("read_file\\File.txt")

# Level of Logging
# 1. Debug
# 2. info
# 3. warning
# 4.error
# 5. critical

