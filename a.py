#!/usr/bin/python3
import subprocess
import argparse
import os
import csv
import re
#args = []

def main():
    parser = argparse.ArgumentParser("a")
    parser.add_argument('--conf', required=True)
    args = parser.parse_args()
#    try:
#    f = open(args.conf)
#    f.close()

    (m, s) = parse_config(args.conf)
    sanity_check(m, s)
    #pull(m, s)
    

def parse_config(filename):
    meta = {}
    song = {}
    with open(filename, newline='') as config:
        reader = csv.reader(config)
        for row in reader:
            if re.match(r'^Song', row[0]):
                song[row[0]] = row[1]
            else:
                meta[row[0]] = row[1]
    return (meta, song)


def sanity_check(meta, songs):
    req = [ 'Artist', 'Album', 'o' ]
    for i in req:
        #print("\ti is %s and keys are %s"%(i, ))
        print("\ti is %s and keys are %s"%(i, meta.keys()))
        

    

#def pull(meta, song):
    
    

#parser = argparse.ArgumentParser("a")
#parser.add_argument('--conf')
#args = parser.parse_args()

main()
#sanity_check()
proc = []


#url=['https://www.youtube.com/watch?v=NAdlZ2F-fs8']

#youtube='/usr/bin/youtube-dl'
#youtube_args=["--extract-audio", "--audio-format", "vorbis", "--audio-quality", '0', '--no-mtime', "-o", "02 - My Song.ogg"]
#aa = [ youtube ]
#aa.extend(youtube_args)
#aa.extend(url)

#print("aa is %s"%(aa))

#proc = subprocess.run(aa, stdout=subprocess.PIPE)
