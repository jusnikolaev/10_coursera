import requests
from lxml import html
from bs4 import BeautifulSoup
import json

def get_courses_content():
    url = 'https://www.coursera.org/sitemap~www~courses.xml'
    courses_body = requests.get(url=url)
    if courses_body.ok:
        return courses_body.content
    else:
        return None


def get_courses_list(courses_body, courses_num):
    courses_list = html.fromstring(courses_body)
    courses_url_list = courses_list.xpath('//loc/text()')
    return courses_url_list[:courses_num]


def get_course_info(course_slug):
    list_courses_json = []
    for course in course_slug:
        course_json = {}
        get_html = requests.get(course)
        html_page = get_html.text
        soup = BeautifulSoup(html_page, 'html.parser')
        for course_name in soup.find_all('h2', class_='headline-4-text course-title'):
            course_json['name'] = course_name.text
        for course_language in soup.find_all('div', class_='rc-Language'):
            course_json['language'] = course_language.text
        for course_start_date in soup.find_all('div', class_='startdate rc-StartDateString caption-text'):
            course_json['start_date'] = course_start_date.text
        for course_rating in soup.find_all('div', class_='ratings-text bt3-visible-xs'):
            course_json['rating'] = course_rating.text
        course_json['duration'] = len(soup.find_all('div', class_='week'))
        list_courses_json.append(course_json)
    print(list_courses_json)
    return list_courses_json





def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    courses_content = get_courses_content()
    if courses_content:
        courses_list = get_courses_list(courses_content, 2)
        get_course_info(courses_list)
