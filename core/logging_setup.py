import logging

def setup_logging(level: str = "INFO"):
    level = getattr(logging, level.upper(), logging.INFO)
    root = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)
    root.setLevel(level)
    logging.getLogger("aiosqlite").setLevel(logging.WARNING)
