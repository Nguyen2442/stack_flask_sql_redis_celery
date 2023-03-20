from app.core.app_celery.celery_app import celery
from app.core.database.redis import redis_client
import csv
import time
# def create_hash_data_employee_in_redis(data):
#     name = f'sync_information_employeee__{data.get("id")}__{data.get("email")}'
#     mapping = _dumps_dict_for_hash_map(data)
#     print(mapping)
#     await redis_client.hset(name=name, mapping=mapping)
#     return mapping




@celery.task(bind=True)
def generate_large_file(self):
    # Generate the large file
    # with open('large_file.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for i in range(1000000):
    #         writer.writerow(['Row ' + str(i), 'Value ' + str(i)])
    #         time.sleep(0.001)
    with open('large_file.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(10):
            writer.writerow(['Row ' + str(i), 'Value ' + str(i)])
            #time.sleep(0.001)

    self.update_state(state='SUCCESS')
    #print(task_id)
    #redis_client.set(task_id, 'SUCCESS')
    return True
