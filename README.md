# Outbrain Test

You can read more about the position here.
We really appreciate your willingness to accept the home assignment.

As Outbrain engineering groups are heavy users of Prometheus, we would like to provide developers  a full monitoring environment  on their local laptops which will help them to develop their code and see how their service behaving before going to production.
For that we would like you to develop a tool which will spin up a prometheus environment with Grafana for that purpose.

Please write a tool in the language of your choice that will take the following 3 parameters:

    Prometheus version
    Prometheus Retention in hours
    Grafana version.

The script will spin up a monitoring environment which will include the following components:

    Prometheus server inside a container of the given prometheus version with the specified storage retention and with a job which will scrape it's own prometheus metrics.
    Grafana container with given version which is connected to prometheus server as a datasource and holds a predefined dashboard which visualize two Prometheus server metrics (please choose any metric you want).

    All components have to be a docker components.
    The tool has to be one executable file (or one command)
    Both Prometheus UI and Grafana should be accessible from browser.
    Please make sure prometheus version 1.x.x and 2.x.x work both.



# Solution
file monitor.py should be executed with the following attributes:
--help : see help instructions
--pversion : set Prometheus version
--pretention : set retention in hours
--gversion : set Grafana version

Example execution command:
./monitor.py --pversion 2.16.0 --pretention 180 --gversion 6.6.2

The scraped metrics are of Prometheus itself, i thought about scraping system metrics but that required node-exporter and I think this wasn't your intention.
