import logging
import os

class FileLogger:
    def __init__(self, log_file: str = "app.log", level: int = logging.INFO):
        self.logger = logging.getLogger("YouTubeSummarizer")
        self.logger.setLevel(level)
        
        # Avoid adding duplicate handlers if the logger already has one
        if not self.logger.handlers:
            # File handler
            fh = logging.FileHandler(log_file)
            fh.setLevel(level)
            # Console handler for errors
            ch = logging.StreamHandler()
            ch.setLevel(logging.ERROR)
            
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
    
    def info(self, msg: str):
        self.logger.info(msg)
    
    def error(self, msg: str):
        self.logger.error(msg)
    
    def debug(self, msg: str):
        self.logger.debug(msg)
    
    def warning(self, msg: str):
        self.logger.warning(msg)
