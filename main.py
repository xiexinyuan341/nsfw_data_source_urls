from image_downloader.task_generator import TaskGenerator
from logger_setter import setup_log

if __name__ == '__main__':
    setup_log("debug")
    task_generator = TaskGenerator('./raw_data')
    tasks = task_generator.generate_task()
    # TODO  multi_threading process
    # each Crawler use one thread.
    pass