import unittest
import json

from functools import wraps

from publish_docs import merge_additionall_applications

def additional_application_provider(f):
    @wraps(f)
    def inner_func(self, *args, **kwargs):
        dataset = (
            (
                [
                    {
                      "image": "registry.vuestorefront.cloud/docs-storefrontcloud-io/cloud",
                      "name": "cloud-v2",
                      "path": "/cloud-v2",
                      "port": "80",
                      "tag": "da7b37f956d88e8c4baa3d1bd8f46a534cc99b8c"
                    },
                    {
                      "image": "registry.storefrontcloud.io/docs-storefrontcloud-io/v2-bloomreach-search",
                      "name": "docs-v2-bloomreach-search",
                      "path": "/bloomreach-search",
                      "port": "80",
                      "tag": "1.0.1642077571"
                    }
                ],
                [
                    {
                      "image": "registry.vuestorefront.cloud/docs-storefrontcloud-io/cloud",
                      "name": "cloud-v2",
                      "path": "/cloud-v2",
                      "port": "80",
                      "tag": "da7b37f956d88e8c4baa3d1bd8f46a534cc99b8c"
                    },
                    {
                      "image": "registry.storefrontcloud.io/docs-storefrontcloud-io/v2-bloomreach-search",
                      "name": "docs-v2-bloomreach-search",
                      "path": "/bloomreach-search",
                      "port": "80",
                      "tag": "1.0.1656789123"
                    }
                ]
            ),
            (
                [
                    {
                      "image": "registry.vuestorefront.cloud/docs-storefrontcloud-io/cloud",
                      "name": "cloud-v2",
                      "path": "/cloud-v2",
                      "port": "80",
                      "tag": "da7b37f956d88e8c4baa3d1bd8f46a534cc99b8c"
                    }
                ],
                [
                    {
                      "image": "registry.vuestorefront.cloud/docs-storefrontcloud-io/cloud",
                      "name": "cloud-v2",
                      "path": "/cloud-v2",
                      "port": "80",
                      "tag": "da7b37f956d88e8c4baa3d1bd8f46a534cc99b8c"
                    },
                    {
                      "image": "registry.storefrontcloud.io/docs-storefrontcloud-io/v2-bloomreach-search",
                      "name": "docs-v2-bloomreach-search",
                      "path": "/bloomreach-search",
                      "port": "80",
                      "tag": "1.0.1656789123"
                    }
                ]
            )
        )
        for data in dataset:
            f(self, data[0], data[1])

    return inner_func


class TestCreate(unittest.TestCase):
    @additional_application_provider
    def test_mering_additionall_applications(self, current, expected):
        """Test if additional_apps are merged"""

        to_merge = {
            "image": "registry.storefrontcloud.io/docs-storefrontcloud-io/v2-bloomreach-search",
            "name": "docs-v2-bloomreach-search",
            "path": "/bloomreach-search",
            "port": "80",
            "tag": "1.0.1656789123"
        }

        merged = merge_additionall_applications(current, to_merge)

        self.assertListEqual(merged, expected)