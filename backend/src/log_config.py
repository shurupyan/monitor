LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'correlation_id': {
            '()': 'asgi_correlation_id.CorrelationIdFilter',
            'uuid_length': 32,
        },
    },
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(correlation_id)s] '
                      'logger=%(name)s - module=%(module)s - func=%(funcName)s(): %(message)s '
        },
        'access': {
            'format': '[%(asctime)s] [%(levelname)s] [%(correlation_id)s] %(message)s'
        }
    },
    'handlers': {
        'http': {
            'level': 'DEBUG',
            'formatter': 'access',
            'class': 'logging.StreamHandler',
            'filters': ['correlation_id'],
            'stream': 'ext://sys.stdout'
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'filters': ['correlation_id'],
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filters': ['correlation_id'],
            'filename': 'speedtest_monitor_be.log',
            'maxBytes': 1024,
            'backupCount': 3
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'uvicorn.access': {
            'level': 'DEBUG',
            'handlers': ['http'],
            'propagate': False
        },
        'uvicorn.error': {
            'propagate': True
        }
    }
}
