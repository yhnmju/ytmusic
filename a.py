#!/usr/bin/python3
import subprocess
import argparse
import os
import csv
import re
import sys
import errno
#args = []

def main():
    parser = argparse.ArgumentParser("a")
    parser.add_argument('--conf', required=True)
    args = parser.parse_args()
    if not os.path.exists(args.conf):
        raise Exception('File does not exist: %s'%(args.conf))

    (m, s) = parse_config(args.conf)
    sanity_check(m, s)
    pull(m, s)
    

def parse_config(filename):
    meta = {}
    song = {}
    with open(filename, newline='') as config:
        reader = csv.reader(config)
        for row in reader:
            if re.match(r'^Song', row[0]):
                song[row[0]] = { 'url':row[2], 'title':row[1] }
            else:
                meta[row[0]] = row[1]
    return (meta, song)


def sanity_check(meta, songs):
    # Dictionary 'req' is required metadata
    req = [ 'Artist', 'Album' ]
    missing = [ ]
    # for each key in req dictionary
    for i in req:
        # check if it exists in the album meta data
        if i not in meta:
            missing.append(i)
    if missing:
        l = ','.join(str(e) for e in missing)
        raise Exception("Error: Required album info is missing: %s"%(l))
            
def make_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def pull(meta, songs):
    dir=meta['Artist'] + '/' + meta['Album'] + '/'
    if not os.path.isdir(dir):
        make_dir(dir)
    for s in songs:
        x = s.replace('Song_','')
        filename = dir + x + " - " + songs[s]['title'] + '.ogg'
        dl(filename, songs[s]['url'])
            
def dl(filename, url):
    youtube='/usr/bin/youtube-dl'
    youtube_args=["--extract-audio", "--audio-format", "vorbis", "--audio-quality", '0', '--no-mtime', "-o", filename, url]
    aa = [ youtube ]
    aa.extend(youtube_args)
    print("Downloading %s to %s"%(url, filename))
    proc = subprocess.run(aa, stdout=subprocess.PIPE)


main()
