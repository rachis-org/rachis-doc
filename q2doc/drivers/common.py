import os
import urllib


DEFAULT_BASE_COMMAND = 'rachis'

# The base command in rendered usage examples (`qiime`, `rachis`, or `mosh`)
def _get_base_command():
    return os.environ.get('Q2DOC_BASE_COMMAND', DEFAULT_BASE_COMMAND)


def _build_url(data_dir, fn):
    baseurl = os.environ.get('BASE_URL')
    if baseurl is None:
        baseurl = os.environ.get('READTHEDOCS_CANONICAL_URL')
    if baseurl is None:
        # prevent myst from treating it as a local ref (and clobbering the url)
        baseurl = '/'

    parts = list(urllib.parse.urlparse(baseurl))
    parts[2] += '/'.join([str(data_dir), str(fn)])
    url = urllib.parse.urlunparse(parts)
    return url
