import logging
from logging.handlers import RotatingFileHandler
import os

log_level_dict = {
    "notset": logging.NOTSET,
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}


def setup_log(log_level='info'):
    log_level = log_level_dict.get(log_level, None)
    if log_level is None:
        log_level = logging.INFO
    # 设置日志的记录等级
    logging.basicConfig(level=log_level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    workspace = os.path.dirname(__file__)
    log_dir = os.path.join(workspace, "logs")
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    file_log_handler = RotatingFileHandler(os.path.join(log_dir, 'log'),
                                           maxBytes=1024 * 1024 * 100,
                                           backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter(
        '%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


if __name__ == '__main__':
    setup_log()
    logging.warning("haha")
