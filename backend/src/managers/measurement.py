from datetime import datetime
from db import database, get_or_create_ts_key
import logging


class MeasurementManager:

    @staticmethod
    def get_measurements(body):
        # filter = {'type': 'Measurement'}
        # q = database.ts().mget().select()
        # if user['role'] == RoleType.complainer:
        #     q = q.where(complaint.c.complainer_id == user['id'])
        # elif user['role'] == RoleType.approver:
        #     q = q.where(complaint.c.status == State.pending)
        # return await database.fetch_all(q)
        pass

    @staticmethod
    async def add_measurements(measurement_data):
        logging.debug('add_measurements func started')

        meas = measurement_data.dict()
        server = meas.pop("server")
        client = meas.pop("client")
        client_labels = {
            "ip": client["ip"],
            "coord": ';'.join([client["lat"], client["lon"]]),
            "isp": client["isp"],
            "country": client["country"]
        }
        download_labels = client_labels.copy()
        download_labels.update({'type': 'download'})
        upload_labels = client_labels.copy()
        upload_labels.update({'type': 'upload'})
        ping_labels = client_labels.copy()
        ping_labels.update({'type': 'ping'})
        download_key = await get_or_create_ts_key(labels=download_labels)
        upload_key = await get_or_create_ts_key(labels=upload_labels)
        ping_key = await get_or_create_ts_key(labels=ping_labels)

        logging.debug(client_labels)
        logging.debug(download_key)
        logging.debug(download_labels)
        logging.debug(upload_key)
        logging.debug(upload_labels)
        logging.debug(ping_key)
        logging.debug(ping_labels)

        dt = datetime.fromisoformat(measurement_data.timestamp)
        logging.debug(f'Datetime: {dt}')
        ts = int(dt.timestamp()*1000)
        res = await database.ts().madd(
            [
                (download_key, ts, measurement_data.download),
                (upload_key, ts, measurement_data.upload),
                (ping_key, ts, measurement_data.ping),
            ]
        )
        logging.debug(f'Insert type: {type(res)}')
        if type(res) == list:
            ins_res = [str(result) for result in res]
        else:
            ins_res = res
        logging.debug(f'Insert result: {str(ins_res)}')

        filters = ['='.join(label) for label in client_labels.items()]
        logging.debug(f'Filters: {str(filters)}')
        res = await database.ts().mget(filters=filters, select_labels=['type'])
        logging.debug(f'Insert result: {str(res)}')
        return {
            'data': {
                'latest': res,
                'last_insert': ins_res
            }
        }
