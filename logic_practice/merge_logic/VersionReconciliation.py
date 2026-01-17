from typing import Optional


def reconcile_versions(records):
    rec_map = {}

    for rec in records:
        rec_id = rec['id']

        if rec_id not in rec_map:
            rec_map[rec_id] = rec
        else:
            # Optional
            # if (rec_map[rec_id]['version'], rec_map[rec_id]['timestamp'])
            #  < (rec['version'], rec['timestamp']):
            #     rec_map[rec_id] = rec

            rec_ver = rec['version']
            if rec_map[rec_id]['version'] < rec_ver:
                rec_map[rec_id] = rec
            elif rec_map[rec_id]['version'] == rec_ver:
                rec_ts = rec['timestamp']
                if rec_map[rec_id]['timestamp'] < rec_ts:
                    rec_map[rec_id] = rec
    
    return list(rec_map.values())