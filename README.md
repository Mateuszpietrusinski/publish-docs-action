# Publush VSF docs

This action publish VSF docs to VSF Cloud

## Inputs

### `user-id`

**Required** User ID

### `api-key`

**Required** API key

### `name`

**Required** Documentation name

### `tag`

**Required** Docker image tag

### `image`

**Required** Docker image full url (with registry)

### `path`

**Required** Documentation path

### `port`

**Required** Documentation port

### `has-base-path`

**Required** Documentation base path

### `farmer-namespace-name`

**Required** Documentation farmer-namespace-name e.g. docs-europe-west1-gcp-storefrontcloud-io

## Outputs

### `response`

Publish action (Farmer API call) response code

## Example usage

```
uses: vuestorefront/publish-docs-action@main
with:
  user-id: "${{ secrets.DOCS_CLOUD_USERNAME }}"
  api-key: "${{ secrets.DOCS_CLOUD_PASSWORD }}"
  name: 'docs-v2-bigcommerce'
  tag: "${{ steps.get_version.outputs.VERSION }}"
  image: "registry.storefrontcloud.io/docs-storefrontcloud-io/v2-bigcommerce"
  path: "/bigcommerce"
  port: "80"
  has-base-path: false
  farmer-namespace-name: docs-europe-west1-gcp-storefrontcloud-io
```
