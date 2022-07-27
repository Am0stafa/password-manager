    with open('password.json', 'r') as f:
        data = json.load(f)# read the old data
        data.update(newData)# update the old data
            