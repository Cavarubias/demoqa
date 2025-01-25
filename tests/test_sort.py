from pages.tables import Tables


def test_table_sort(browser):
    web_tables_page = Tables(browser)
    web_tables_page.visit()
    columns_class = 'rt-th rt-resizable-header -sort-asc -cursor-pointer' or 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    web_tables_page.column_title_first_name.click()
    assert web_tables_page.column_title_first_name.get_dom_attribute('class') == columns_class
    web_tables_page.column_title_last_name.click()
    assert web_tables_page.column_title_last_name.get_dom_attribute('class') == columns_class
    web_tables_page.column_title_age.click()
    assert web_tables_page.column_title_age.get_dom_attribute('class') == columns_class
    web_tables_page.column_title_email.click()
    assert web_tables_page.column_title_email.get_dom_attribute('class') == columns_class
    web_tables_page.column_title_salary.click()
    assert web_tables_page.column_title_salary.get_dom_attribute('class') == columns_class
    web_tables_page.column_title_department.click()
    assert web_tables_page.column_title_department.get_dom_attribute('class') == columns_class
    web_tables_page.column_title_action.click()
    assert web_tables_page.column_title_action.get_dom_attribute('class') == columns_class


