#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DZ2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#Задание
#Создайте три модели Django: клиент, товар и заказ.
#
#Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
#

#
#Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе.