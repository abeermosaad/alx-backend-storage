#!/usr/bin/env python3
""" Improve 12-log_stats.py """
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """ Print the number of documents in nginx_collection """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def print_nginx_request_ips(nginx_collection):
    """ Print the top 10 IPs """
    print('IPs:')
    ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print('\t{}: {}'.format(ip.get('_id'), ip.get('count')))


def run():
    """ Print the stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)
    print_nginx_request_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
