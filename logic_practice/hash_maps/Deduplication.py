def deduplicate_records(records):
    rec_map = {}
    
    for rec in records:
        rec_id = rec['id']

        if rec_id not in rec_map:
            rec_map[rec_id] = rec
        else:
            rec_ts = rec['updated_at']
            if rec_ts > rec_map[rec_id]['updated_at']:
                rec_map[rec_id] = rec
    return list(rec_map.values())

if __name__ == '__main__':
    print(deduplicate_records([
{"id": 1, "payload": "A", "updated_at": 100},
{"id": 1, "payload": "B", "updated_at": 150},
{"id": 2, "payload": "X", "updated_at": 200},
{"id": 2, "payload": "Y", "updated_at": 180},
{"id": 3, "payload": "Z", "updated_at": 300}
]))




# records = [
# {"id": 1, "payload": "A", "updated_at": 100},
# {"id": 1, "payload": "B", "updated_at": 150},
# {"id": 2, "payload": "X", "updated_at": 200},
# {"id": 2, "payload": "Y", "updated_at": 180},
# {"id": 3, "payload": "Z", "updated_at": 300}
# ]
# Expected Output (one valid answer)
# [
# {"id": 1, "payload": "B", "updated_at": 150},
# {"id": 2, "payload": "X", "updated_at": 200},
# {"id": 3, "payload": "Z", "updated_at": 300}
# ]