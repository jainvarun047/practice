def apply_deltas(base_records, delta_updates):
    record_map = {rec['id']: rec for rec in base_records}

    for delta in delta_updates:
        rec_id = delta['id']

        if rec_id not in record_map:
            continue

        if delta['timestamp'] > record_map[rec_id]['timestamp']:
            for field, value in delta['changes'].items():
                record_map[rec_id][field] = value
            record_map[rec_id]['timestamp'] = delta['timestamp']

    return list(record_map.values())