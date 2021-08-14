#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID", 1328368 cast=int)
    API_HASH = config("API_HASH", "94efff3c213dfd4f1c89d4f7da3e6387")
    BOT_TOKEN = config("BOT_TOKEN", "1642847266:AAF3hly8KeDISoTXe8ZE7skrndZO0bHAQ1U")
    OWNER = config("OWNER_ID", default=817541612, cast=int)
    LOG = config("LOG_CHANNEL", "-1001275564772" cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
