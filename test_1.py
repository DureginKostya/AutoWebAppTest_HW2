import time

import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(site_negative, result_xpath):
    rsl = site_negative.find_element('xpath', result_xpath).text
    assert rsl == '401'


def test_step2(site_positive, result_login):
    rsl = site_positive.find_element('xpath', result_login).text
    assert rsl == 'Blog'


def test_step3(site_positive, button_created, new_title, new_description,
               new_content, new_date, button_save, created_new_title):
    site_positive.created_post('xpath', button_created, new_title, new_description, new_content, new_date,
                               button_save, testdata['title_new_post'], testdata['description_new_post'],
                               testdata['content_new_post'], testdata['date_created'])
    time.sleep(3)
    rsl = site_positive.find_element('xpath', created_new_title).text
    assert rsl == testdata['title_new_post']
