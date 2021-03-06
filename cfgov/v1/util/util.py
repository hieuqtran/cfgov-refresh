from time import time

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import resolve
from django.http import Http404, HttpResponseRedirect
from wagtail.wagtailcore.blocks.stream_block import StreamValue


def get_unique_id(prefix='', suffix=''):
    index = hex(int(time() * 10000000))[2:]
    return prefix + str(index) + suffix


# These messages are manually mirrored on the
# Javascript side in error-messages-config.js

ERROR_MESSAGES = {
    'CHECKBOX_ERRORS': {
        'required': 'Please select at least one of the "%s" options.'
    },
    'DATE_ERRORS': {
        'invalid': 'You have entered an invalid date.',
    }
}


def instanceOfBrowseOrFilterablePages(page):
    from ..models import BrowsePage, BrowseFilterablePage
    pages = (BrowsePage, BrowseFilterablePage)
    return isinstance(page, pages)


# For use by Browse type pages to get the secondary navigation items
# TODO: Move into BrowsePage class once BrowseFilterablePage has been merged
# into BrowsePage
def get_secondary_nav_items(request, current_page):
    # If the parent page of the current page is a BrowsePage or a
    # BrowseFilterablePage, then use that as the top-level page for the
    # purposes of the navigation sidebar. Otherwise, treat the current page
    # as top-level.
    parent = current_page.get_parent().specific
    if instanceOfBrowseOrFilterablePages(parent):
        page = parent
    else:
        page = current_page

    # If there's no appropriate page version (e.g. not published for a sharing
    # request), then return no sidebar at all.
    if not page:
        return [], False

    # Handle the Newsroom page specially.
    # TODO: Remove this ASAP once Press Resources gets its own Wagtail page
    if page.slug == 'newsroom':
        return [
            {
                'title': page.title,
                'slug': page.slug,
                'url': page.relative_url(request.site),
                'children': [
                    {
                        'title': 'Press Resources',
                        'slug': 'press-resources',
                        'url': '/newsroom/press-resources/',
                    }
                ],
                'active': True,
                'expanded': True,
            }
        ], True
    # END TODO

    if page.secondary_nav_exclude_sibling_pages:
        pages = [page]
    else:
        pages = filter(
            lambda p: instanceOfBrowseOrFilterablePages(p.specific),
            page.get_appropriate_siblings(request.site.hostname)
        )

    nav_items = []
    for sibling in pages:
        if page.id == sibling.id:
            sibling = page
        else:
            sibling = sibling

        item_selected = current_page.pk == sibling.pk

        item = {
            'title': sibling.title,
            'slug': sibling.slug,
            'url': sibling.relative_url(request.site),
            'children': [],
            'active': item_selected,
            'expanded': item_selected,
        }

        visible_children = filter(
            lambda c: (
                instanceOfBrowseOrFilterablePages(c) and
                (c.live)
            ),
            sibling.get_children().specific()
        )

        for child in visible_children:
            child_selected = current_page.pk == child.pk

            if child_selected:
                item['expanded'] = True

            item['children'].append({
                'title': child.title,
                'slug': child.slug,
                'url': child.relative_url(request.site),
                'active': child_selected,
            })

        nav_items.append(item)

    # Return a boolean about whether or not the current page has Browse
    # children
    has_children = any(
        page.relative_url(request.site) == item['url'] and item['children']
        for item in nav_items
    )

    return nav_items, has_children


def valid_destination_for_request(request, url):

    view, args, kwargs = resolve(url)
    kwargs['request'] = request
    try:
        response = view(*args, **kwargs)
    except (Http404, TypeError):
        return False

    if isinstance(response, HttpResponseRedirect):
        # this indicates a permissions problem
        # (there may be a better way)
        if REDIRECT_FIELD_NAME + '=' in response.url:
            return False

    return True


def all_valid_destinations_for_request(request):
    possible_destinations = (
        ('Wagtail', '/admin/'),
        ('Django admin', '/django-admin/')
    )
    valid_destinations = [pair for pair in possible_destinations
                          if valid_destination_for_request(request, pair[1])]

    return valid_destinations


def get_streamfields(page):
    """
    Retrieves the stream values on a page from its Streamfield
    """
    blocks_dict = {}
    for key, value in vars(page).items():
        if isinstance(value, StreamValue):
            blocks_dict.update({key: value})
    return blocks_dict
