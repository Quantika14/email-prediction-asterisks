from intelxapi import intelx
import m.key as KEY
import shutil

intelx = intelx(KEY.intelx)

def get_pastes(target):
    results = intelx.search(target, buckets=['pastes'], maxresults=2000)
    record_count = len(results['records'])
    print(f"|----[INFO][>] Found {record_count} records for {target} in bucket 'pastes'")
    
    files = []

    if record_count > 0:
        for i in range(0,record_count +1):
            filename = "../pastes/filepaste-"+str(i)+".txt"
            print("|----[INFO][>] Downloading paste in" + filename)
            intelx.FILE_READ(results['records'][i]['systemid'], 0, results['records'][i]['bucket'], filename)
            files.append(filename)
        return files
    else:
        return None

def get_leaks(target):
    results = intelx.search(target, buckets=['leaks.public','leaks.private'], maxresults=2000)
    record_count = len(results['records'])
    print(f"|----[INFO][>] Found {record_count} records for {target} in bucket 'leaks'")

    files = []    

    if record_count > 0:
        for i in range(0,record_count+1):
            filename = "../pastes/fileleak-"+str(i)+".txt"
            print("|----[INFO][>] Downloading leak in " + filename)
            intelx.FILE_READ(results['records'][i]['systemid'], 0, results['records'][i]['bucket'], "file-"+str(i)+".txt")
            files.append(filename)
        return files
    else:
        return None

def get_darknet(target):
    results = intelx.search(target, buckets=['darknet'], maxresults=2000)
    record_count = len(results['records'])
    print(f"|----[INFO][>] Found {record_count} records for {target} in bucket 'darknet'")

    files = []

    if record_count > 0:
        for i in range(0,record_count+1):
            filename = "../pastes/filedarknet-"+str(i)+".txt"
            print("|----[INFO][>] Downloading link in darknet in " + filename)
            intelx.FILE_READ(results['records'][i]['systemid'], 0, results['records'][i]['bucket'], "file-"+str(i)+".txt")
            files.append(filename)
        return files
    else:
        return None

def attack(target):

    results = intelx.search(target)
    record_count = len(results['records'])
    files = []
    for i in range(0,record_count):
        filename = target + "-" + str(i) + ".txt"
        intelx.FILE_READ(results['records'][i]['systemid'], 0, results['records'][i]['bucket'], filename)
        files.append(filename)
    return files