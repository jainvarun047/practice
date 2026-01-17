def merge_records(records_a, records_b):
    res = {record['id']: record for record in records_a}

    for record in records_b:
        rec_id = record['id']
        if rec_id not in res:
            res[rec_id] = record
        else:
            if record['timestamp'] > res[rec_id]['timestamp']:
                res[rec_id] = record

    return res.values()
    