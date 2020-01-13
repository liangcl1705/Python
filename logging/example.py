#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging.config

"""
    description: The example of logging.
    author: LiangCL
    since: 2020/1/13
"""

logging.config.fileConfig('conf/logging.ini')
logger = logging.getLogger(__name__)


def main() -> None:
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.fatal('fatal')


if __name__ == '__main__':
    main()
