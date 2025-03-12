from django.urls import resolve
from .templatetags.gsmp_tags import get_main_menu

def breadcrumb_processor(request):
    """  Breadcrumb მენიუს დინამიურად """
    breadcrumbs = []
    path = request.path  # იღებს მიმდინარე URL-ს
    match = resolve(path)  # აბრუნებს view-ს ინფორმაციას

    # მენიუს ძებნა
    def find_breadcrumbs(menu, parent=None):
        for item in menu:
            if item['url_name'] == match.view_name:
                breadcrumbs.append({"title": item['title'], "url": item['url_name']})
                if parent:
                    breadcrumbs.insert(0, {"title": parent['title'], "url": parent['url_name']})
                return True  # იპოვა და დააბრუნა

            if 'submenu' in item:
                if find_breadcrumbs(item['submenu'], item):
                    return True

        return False  # ვერ იპოვა

    # მთავარ მენიუში ძებნა
    main_menu = get_main_menu()



    find_breadcrumbs(main_menu)

    return {'breadcrumbs': breadcrumbs}
