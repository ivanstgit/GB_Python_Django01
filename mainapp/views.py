import json
from datetime import datetime

from django.views.generic import TemplateView


#
class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)

        # Create your own data
        news_dict = {}
        with open("mainapp/news.json", "r", encoding="utf-8") as news_file:
            news_dict = json.load(news_file)

        # Read page number and adjust
        items_per_page = 5
        pages_count = 1 + len(news_dict.keys()) // items_per_page
        if self.request.GET.get("page"):
            page_num = int(self.request.GET.get("page"))
        else:
            page_num = 1

        if page_num > pages_count:
            page_num = pages_count

        # Calculate slices for current page
        news_from_index = (page_num - 1) * items_per_page
        news_to_index = page_num * items_per_page - 1
        if len(news_dict) <= news_to_index:
            news_to_index = len(news_dict)

        news_list = list(news_dict.values())[news_from_index:news_to_index:1]
        for item in news_list:
            item["datetime"] = datetime.strptime(item.get("datetime"), "%Y-%m-%dT%H:%M:%S.%f")

        context["news_list"] = news_list
        context["page_num"] = page_num
        context["pages_range"] = range(1, pages_count + 1)
        context["items_per_page"] = items_per_page

        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
