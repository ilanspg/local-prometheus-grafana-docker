#!/usr/bin/env python3

import os
import argparse


parser = argparse.ArgumentParser(description='Install local prometheus & Grafana for Outbrain DevOps test')
parser.add_argument('--pversion', type=str, help='Version number for Prometheus')
parser.add_argument('--pretention', type=int, help='Retention in hours')
parser.add_argument('--gversion', type=str, help='Version number for Grafana')

args = parser.parse_args()

# Main Function
print('Creating docker volume for Prometheus...')
os.system('docker volume create prometheus_data')

print('Creating docker volume for Grafana...')
os.system('docker volume create grafana_data')

if args.pversion.startswith("1"):
    print('Starting Prometheus container (version 1.x.x)...')
    command = f"docker run -d -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml -v prometheus_data:/prometheus prom/prometheus:v{args.pversion} -config.file '/etc/prometheus/prometheus.yml' -storage.local.retention {args.pretention}h"
    os.system(command)

else:
    print('Starting Prometheus container (version 2.x.x)...')
    command = f"docker run -d -p 9090:9090 -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml -v prometheus_data:/prometheus prom/prometheus:v{args.pversion} --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.retention.time={args.pretention}h"
    os.system(command)

print('Starting Grafana container...')
command = f"docker run -d -p 3000:3000 -v grafana_data:/var/lib/grafana -v $PWD/grafana.db:/var/lib/grafana/grafana.db grafana/grafana:{args.gversion}"
os.system(command)