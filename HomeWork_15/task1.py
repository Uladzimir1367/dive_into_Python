'''
Задание 1. Логирование с использованием нескольких файлов
 Напишите скрипт, который логирует разные типы сообщений в разные файлы.
 Логи уровня DEBUG иINFOдолжнысохраняться вdebug_info.log, а логи уровня
 WARNINGивыше—вwarnings_errors.log.
 Подсказка № 1
 Создайте логгеры с разными уровнями логирования. Используйте
 logger.setLevel() для установки минимального уровня логирования, который будет
 обрабатываться логгером.
 Подсказка № 2
 Используйте logging.FileHandler для записи логов в файлы. Установите FileHandler
 для записи сообщений в указанные файлы и укажите уровень логирования для
 каждого обработчика с помощью метода setLevel().
 Подсказка № 3
 Настройте формат сообщений с помощью logging.Formatter. Создайте объект
 Formatter для настройки формата сообщений. Примените его к обработчикам с
 помощью метода setFormatter().
 Подсказка № 4
 Добавьте обработчики к логгеру с помощью addHandler(). После настройки
 обработчиков, добавьте их к логгеру с помощью метода addHandler().
'''

import logging

# Создаем логгер
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Создаем обработчики
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)

warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)

# Создаем форматтеры и добавляем их к обработчикам
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Примеры логирования
logger.debug('Это сообщение уровня DEBUG')
logger.info('Это сообщение уровня INFO')
logger.warning('Это сообщение уровня WARNING')
logger.error('Это сообщение уровня ERROR')
logger.critical('Это сообщение уровня CRITICAL')

# Этот скрипт создаст два файла: debug_info.log для сообщений уровня DEBUG и INFO, и warnings_errors.log для сообщений уровня WARNING и выше. 