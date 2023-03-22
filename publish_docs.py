#!/usr/bin/env python3

import sys
import getopt
import json
import requests

from pathlib import Path


def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")


def get_docs_farmer_url(farmer_namespace_name):
    return 'https://farmer.storefrontcloud.io/instance/' + farmer_namespace_name


def get_docs_headers(user_id, api_key):
    return {
        'content-type': 'application/json',
        'x-user-id': user_id,
        'x-api-key': api_key
    }


def merge_additional_applications(current, to_merge):
    merged = []
    new_item = True

    for additional_app in current:
        if additional_app['name'] == to_merge['name']:
            additional_app = to_merge
            new_item = False

        merged.append(additional_app)

    if new_item == True:
        merged.append(to_merge)

    return merged


def get_additional_apps(user_id, api_key, instance_name):
    response = requests.get(get_docs_farmer_url(farmer_namespace_name), headers=get_docs_headers(user_id, api_key))
    instance = response.json()

    if 'instance' in instance and 'additional_apps' in instance['instance'] and 'apps' in instance['instance']['additional_apps']:
        return instance['instance']['additional_apps']['apps']

    return False


def patch_additional_apps(user_id, api_key, payload):
    response = requests.patch(get_docs_farmer_url(), data=json.dumps(payload), headers=get_docs_headers(user_id, api_key))

    return response


def publish_docs(user_id, api_key, name, tag, image, path, port, has_base_path, farmer_namespace_name):
    additional_apps = get_additional_apps(user_id, api_key, farmer_namespace_name)

    if not additional_apps:
        raise Exception("Additional application not configured")

    to_merge = {
        "name": name,
        "tag": tag,
        "image": image,
        "path": path,
        "port": port,
        "has_base_path": str2bool(has_base_path)
    }

    merged_additional_applications = merge_additional_applications(additional_apps, to_merge)
    payload = {'additional_apps': {'apps': merged_additional_applications}}

    response = patch_additional_apps(user_id, api_key, payload, farmer_namespace_name)

    return response


def help():
    return 'publish_docs.py -u user-id -a api-key -n name -t tag -i image -p path -r port -s has-base-path -f farmer-namespace-name'


def main(argv):
    """Main function"""
    try:
        opts, args = getopt.getopt(argv,"hu:a:n:t:i:p:r:s:f:")
    except getopt.GetoptError:
        print(help())
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help())
            sys.exit()
        else:
            if opt in ("-u"):
                user_id = arg
            if opt in ("-a"):
                api_key = arg
            if opt in ("-n"):
                name = arg
            if opt in ("-t"):
                tag = arg
            if opt in ("-i"):
                image = arg
            if opt in ("-p"):
                path = arg
            if opt in ("-r"):
                port = arg
            if opt in ("-s"):
                has_base_path = arg
            if opt in ("-f"):
                farmer_namespace_name = arg

    response = publish_docs(user_id, api_key, name, tag, image, path, port, has_base_path, farmer_namespace_name)
    print("response::" + str(response.status_code))


if __name__ == "__main__":
    main(sys.argv[1:])
