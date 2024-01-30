import logging
logging.basicConfig(level=logging.DEBUG,filename='..\\demo1log.log' ,filemode="w")

class DemoLogging2:
    def add_number(self,a,b):
        return a + b

    def multi_number(self,a,b):
        return a * b

dl=DemoLogging2()
add_num=dl.add_number(2,5)
mul_num=dl.multi_number(5,2)
logging.debug("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.info("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.warning("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.error("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.critical("The Multiplication of 5 and 2 : {}".format(mul_num))
