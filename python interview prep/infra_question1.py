def parse_timestamp(csv):
    timestampMarker = 3
    empty_box = []


    for i in csv:
        
        if csv[timestampMarker] != 3:
            timestampMarker += 1
        else:
            empty_box.append(csv[timestampMarker])

        

