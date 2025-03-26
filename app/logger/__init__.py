from app.logger.logger import getLogger

# Create default logger instance
logger = getLogger()

# Export key functions
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
exception = logger.exception
