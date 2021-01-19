from base.selenium_driver import SeleniumDriver


class table_page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locartors

    input_field = "lname"
    button = "button"
    first_col = "cell-0"
    second_col = "cell-1"


    def enterNum(self, num):
        self.sendKeys(num, self.input_field, locatorType="id")

    def click_button(self):
        self.elementClick(self.button,locatorType="tag")

    def clear_fields(self):
        inputF = self.getElement(locator= self.input_field)
        inputF.clear()

    def find_column(self, locator):
        return  self.getElements(locator, locatorType= "class")

    def getValues(self, column):
        list_num = []
        for num in column:
            list_num.append(int(num.text))


        ukupno_sum = sum(list_num)
        print("Ukupna suma")
        print(ukupno_sum)

        return ukupno_sum

    def prepare(self, num = 0):
        self.clear_fields()
        self.getElement("id")
        self.enterNum(num)
        self.click_button()






