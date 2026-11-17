import os
import urllib


DEFAULT_BASE_COMMAND = 'rachis'

# The base command in rendered usage examples (`qiime`, `rachis`, or `mosh`)
def _get_base_command():
    return os.environ.get('Q2DOC_BASE_COMMAND', DEFAULT_BASE_COMMAND)


def _build_url(data_dir, fn):
    # The URL must be absolute: readers copy it into the wget, Python and R
    # examples, and view.qiime2.org fetches it. On Read the Docs,
    # READTHEDOCS_CANONICAL_URL is the absolute address of the version being
    # built (Read the Docs calls it the version's "canonical base URL"): the
    # project's domain plus /<language>/<version>/, e.g.
    # https://amplicon-docs.qiime2.org/en/stable/, and on a pull-request
    # preview the preview's own address, e.g.
    # https://amplicon-docs--39.org.readthedocs.build/en/39/.
    # BASE_URL is only a path (e.g. /en/stable, the form mystmd uses; a
    # Read the Docs build may set it for the site theme), so it comes second.
    baseurl = (os.environ.get('READTHEDOCS_CANONICAL_URL')
               or os.environ.get('BASE_URL'))
    if not baseurl:
        # prevent myst from treating it as a local ref (and clobbering the url)
        baseurl = '/'
    if not baseurl.endswith('/'):
        baseurl += '/'

    parts = list(urllib.parse.urlparse(baseurl))
    parts[2] += '/'.join([str(data_dir), str(fn)])
    url = urllib.parse.urlunparse(parts)
    return url
