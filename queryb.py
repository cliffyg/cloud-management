import boto.sdb
import datetime
import tools

def run(args):
    conn = args[0]
    station = args[1]
    date = args[2]
    totalVolume = 0
    dom = conn.get_domain(station)
    query = 'SELECT volume FROM `' + dom.name + '` WHERE starttime like "' + date + '%"'
    print "Querying " + dom.name + " to get the sum of volumes"
    volumes = dom.select(query)
    for v in volumes:
        if v['volume'] != "":
            totalVolume += int(v['volume'])
    return totalVolume
	
