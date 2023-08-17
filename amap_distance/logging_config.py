# -*- coding:utf-8 -*-
import datetime
import logging

logger = logging.getLogger()
# 设置此logger的最低日志级别，以后添加的Handler级别若是低于这个设置，则以这个设置为最低限制
logger.setLevel(logging.INFO)

# 建立一个FileHandler，将日志输出到文件
log_file = '/tmp/log/sys_%s.log' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
file_handler = logging.FileHandler(log_file)
# 设置此Handler的最低日志级别
file_handler.setLevel(logging.INFO)
# 设置此Handler的日志输出字符串格式
file_handler.setFormatter(logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'))

# 建立一个StreamHandler，将日志输出到Stream，默认输出到sys.stderr
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'))
stream_handler.setLevel(logging.INFO)

# 将不一样的Handler添加到logger中，日志就会同时输出到不一样的Handler控制的输出中
# 注意若是此logger在以前使用basicConfig进行基础配置，由于basicConfig会自动建立一个Handler，因此此logger将会有3个Handler
# 会将日志同时输出到3个Handler控制的输出中
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
