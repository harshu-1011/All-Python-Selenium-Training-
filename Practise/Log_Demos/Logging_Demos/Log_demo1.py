import logging


class DemoLogging1:
    def add_number(self,a,b):
        return a + b

    def multi_number(self,a,b):
        return a * b

dl=DemoLogging1()
add_num=dl.add_number(2,5)
logging.warning("The Addition of 2 and 5 : {}".format(add_num))
mul_num=dl.multi_number(5,2)
logging.warning("The Multiplication of 5 and 2 : {}".format(mul_num))

"""logging.info("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.error("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.critical("The Multiplication of 5 and 2 : {}".format(mul_num))
logging.debug("The Multiplication of 5 and 2 : {}".format(mul_num))"""