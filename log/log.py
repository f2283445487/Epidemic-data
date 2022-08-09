import logging

def init_logger(name):
    logger = logging.getLogger(name)
    logger.handlers.clear()
    formatter = logging.Formatter('%(asctime)s : %(message)s', "%Y-%m-%d %H:%M:%S")
    fileHandler = logging.FileHandler("api_auto.LOG", mode='a')
    fileHandler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    return logger

#
# def api_log(func):
#     def log(self,*args,**kwargs):
#         func(self,*args,**kwargs)
#         init_logger(self.route).info("请求url:{}---请求体json:{}----返回码{}".format(self.url,self.data,self.res))
#         return
#     return log
