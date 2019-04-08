import math

def generate_paging_link(
        link: str, current_page: int, total_item_count: int, per_page: int) -> str:
    total_page_count = int(math.ceil(total_item_count / float(per_page)))
    # https://api.pollination.cloud/<model-id>/faces?page=2&per_page=50
    base = '<{}?page=%d&per_page={}>; rel="%s"'.format(link, per_page)
    # create all the links and then overwrite them if needed
    first = base % (1, 'first')
    lst = base % (total_page_count, 'last')
    prev = base % (current_page - 1, 'prev')
    nxt = base % (current_page + 1, 'next')
    if current_page == 1:
        # this is the first page
        links = ','.join([nxt, lst])
    elif current_page == total_page_count:
        # this is the last page
        links = ','.join([first, prev])
    else:
        links = ','.join([first, prev, nxt, lst])

    return links