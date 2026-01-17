def sync_cache(db_records, cache_records):
    cache_map = { rec['id']:rec for rec in cache_records}

    db_ids = set()

    for rec in db_records:
        rec_id = rec['id']
        if rec_id not in cache_map:
            cache_map[rec_id] = rec
        else:
            if cache_map[rec_id]['timestamp'] < rec['timestamp']:
                cache_map[rec_id] = rec
        db_ids.add(rec_id)

    cache_map = {
        rec_id:rec
        for rec_id,rec in cache_map.items()
        if rec_id in db_ids
    }

    return list(cache_map.values())
