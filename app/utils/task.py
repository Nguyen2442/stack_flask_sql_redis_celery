def check_task_status(task_id):
    task_result = AsyncResult(task_id)
    if task_result.successful():
        # task completed successfully
        result = task_result.result
        return result
    elif task_result.failed():
        # task failed
        exc = task_result.result
        raise exc
    else:
        # task still running
        return None