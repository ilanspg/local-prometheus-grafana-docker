# DevOps Test

Python script that accepts the following 3 parameters:

    Prometheus version
    Prometheus Retention in hours
    Grafana version.

The script will spin up a monitoring environment which will include the following components:
- Prometheus server inside a container of the given prometheus version with the specified storage retention and with a job which will scrape it's own prometheus metrics.
- Grafana container with given version which is connected to prometheus server as a datasource and holds a predefined dashboard which visualize two Prometheus server metrics (please choose any metric you want).

- All components are docker components.
- One executable file (or one command)for entire process
- Both Prometheus UI and Grafana should be accessible from browser.
- Prometheus version 1.x.x and 2.x.x work both.

## How to use:

file monitor.py should be executed with the following attributes:
```
--help : see help instructions
--pversion : set Prometheus version
--pretention : set retention in hours
--gversion : set Grafana version
```

Example execution command:
```
./monitor.py --pversion 2.16.0 --pretention 180 --gversion 6.6.2
```

The scraped metrics are of Prometheus itself, scraping system metrics require node-exporter (not included here).
