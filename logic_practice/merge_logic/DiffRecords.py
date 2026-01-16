def diff_records(old_records, new_records):

    added = []
    updated = []
    deleted = []
    
    record_map = {record['id']: record for record in old_records}

    for r in new_records:
        r_id = r['id']
        if r_id not in record_map:
            added.append(r)
        else: 
            if r['timestamp'] > record_map[r_id]['timestamp']:
                updated.append(r)
            record_map.pop(r_id)
    
    for r in record_map.values():
        deleted.append(r)

    print(added)
    print(updated)
    print(deleted)

if __name__ == '__main__':
    diff_records([
    {"id": 1, "name": "Alice", "timestamp": 100},
    {"id": 2, "name": "Bob", "timestamp": 200},
    {"id": 3, "name": "Charlie", "timestamp": 300}
],[
    {"id": 2, "name": "Bob", "timestamp": 250},
    {"id": 3, "name": "Charlie", "timestamp": 300},
    {"id": 4, "name": "Daisy", "timestamp": 400}
])

