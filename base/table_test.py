from selenium import webdriver
import os
import unittest
from pages.page_table import table_page


class Test(unittest.TestCase):

    def test_assert(self):

        baseUrl = "file:///C:/Users/damja/Desktop/Test/test.html"
        #settings for firefox
        #driver = webdriver.Firefox(executable_path="\\libs\\geckodriver.exe")

        #settings for chrome
        driverLocation = "..\\libs\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.get(baseUrl)
        page = table_page(driver)
        list_num = [5, 6 , 7 , 8, 9, 10]
        msgs = []

        for num in list_num:
            page.prepare(num)
            first_col_sum = page.getValues(page.find_column(page.first_col))

            if first_col_sum < 0:
                msgs.append("Suma nije veca od 0 za " + str(num) )

            second_col_sum  = page.getValues(page.find_column(page.second_col))

            if second_col_sum % 2 == 0 and second_col_sum > 50:
                msgs.append("Suma druge kolone nije deljiva sa 2 i veca od 50 za broj " + str(num) )

        assert len(msgs) == 0, ", ".join(msgs)

        driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)



# tt = Tabletest()
# tt.table_testing()

