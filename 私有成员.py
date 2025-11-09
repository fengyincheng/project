class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启中")
        else:
            print("5g is closing,4g online......")

    def call_by_5g(self):
        self.__check_5g()
        print("you are chatting.......")
phone = Phone()

phone.call_by_5g()