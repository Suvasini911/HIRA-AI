current_job = None


def set_job(job):
    global current_job
    current_job = job


def get_job():
    return current_job