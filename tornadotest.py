# import tornado.ioloop
# import tornado.web
# import json
# couse={
#     '001':'python',
#     '002':'introduction of AI',
#     '003':'software engineering',
# }
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('Hello,World')
#         self.render('index.html')
# class CourseHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write(json.dumps(couse))
#
#
# def make_app():
#     return tornado.web.Application([
#         (r'/',MainHandler),
#         (r'/couse',CourseHandler),
#     ]
#     )
# if __name__ =='__main__':
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
# import fastapi
from fastapi import  FastAPI
app=FastAPI()

@app.get('/')
def read_root():
    return {'hello':'world'}

@app.get('/items/{item_id}')
def read_item(item_id:int,q:str =None):
    return {'item_id':item_id,'q':q}

