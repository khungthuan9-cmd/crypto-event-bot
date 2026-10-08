# -*- coding: utf-8 -*-
import logging
import sys

def setup_logger():
    logger = logging.getLogger("Crypto5MinBot")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-7s | %(message)s', datefmt='%H:%M:%S'))
        logger.addHandler(handler)
    return logger

logger = setup_logger()
