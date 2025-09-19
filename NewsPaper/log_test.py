import logging

logger = logging.getLogger('django')
logger.debug("DEBUG сообщение (для консоли, если DEBUG=True)")
logger.info("INFO сообщение (для general.log, если DEBUG=False)")
logger.warning("WARNING сообщение (для консоли + general.log)")
logger.error("ERROR сообщение (для консоли + errors.log + почта)")
logger.critical("CRITICAL сообщение (для консоли + errors.log + почта)")

# Специальные логгеры
req_logger = logging.getLogger('django.request')
req_logger.error("Ошибка в django.request (errors.log + email)")

sec_logger = logging.getLogger('django.security')
sec_logger.warning("Проблема безопасности (security.log)")
