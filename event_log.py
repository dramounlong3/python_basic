# b.py
import logging

class Event_log:
    def __init__(self):
        # 定义 TRACE 级别和辅助函数
        TRACE_LEVEL_NUM = 5
        logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")

        def trace(self, message, *args, **kwargs):
            if self.isEnabledFor(TRACE_LEVEL_NUM):
                self._log(TRACE_LEVEL_NUM, message, args, **kwargs)

        logging.Logger.trace = trace

        # 设置 logging 配置，只输出到控制台
        logging.basicConfig(level=TRACE_LEVEL_NUM, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        

    def log_message(self, level, message):
        # 定义日志级别映射字典
        level_methods = {
            'TRACE': logging.getLogger().trace,
            'DEBUG': logging.debug,
            'INFO': logging.info,
            'WARNING': logging.warning,
            'ERROR': logging.error,
            'CRITICAL': logging.critical,
        }

        # 根据传入的日志级别调用相应的 logging 方法
        log_method = level_methods.get(level.upper(), logging.info)
        log_method(message)
        
        # 如果级别大于等于 INFO，则调用 sys_log 方法
        if logging.getLevelName(level.upper()) >= logging.getLevelName('INFO'):
            self.sys_log(level, message)
        

    def sys_log(self, level, message):
        # 这里是将相关信息写入数据库的逻辑
        # 你需要根据你的实际需求编写这部分代码
        # 下面的代码只是一个示例
        
        # 假设这里是将信息写入数据库的代码
        print(f"System log: Level - {level}, Message - {message}")
