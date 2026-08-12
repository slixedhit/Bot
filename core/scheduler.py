"""Scheduler using APScheduler for persistent background jobs."""
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
import logging

scheduler = AsyncIOScheduler()
logger = logging.getLogger("bot.scheduler")


def schedule_reminder(run_at, func, *args, **kwargs):
    trigger = DateTrigger(run_at)
    job = scheduler.add_job(func, trigger, args=args, kwargs=kwargs)
    logger.info(f"Scheduled job {job.id} at {run_at}")
    return job
