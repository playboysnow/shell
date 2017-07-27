# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect
import urllib,requests,sys
from bs4 import BeautifulSoup
import logging
reload(sys)
sys.setdefaultencoding('gb2312')

app=Flask(__name__)

@app.route('/')

def index():
#	app.logger.info('this is a string')
#	app.logger.debug('A value for debugging')
#	app.logger.warning('A warning occurred (%d apples)', 42)
#	app.logger.error('An error occurred')
	return render_template('index1.html')

@app.route('/index')
def page():
	return render_template('index-color.html')

@app.route('/search/')

def search():
#	app.logger.info('this is a string')
#	app.logger.debug('A value for debugging') 
#	app.logger.warning('A warning occurred (%d apples)', 42)
#	app.logger.error('An error occurred')

	key=request.args.get('keyword')
	key1=key.encode('gb2312')
	url_code=urllib.quote(key1)
	url="http://so.loldytt.com/search.asp?keyword="+url_code
	print str(key1),str(url_code),str(url)
	return redirect(url)
'''	html = urllib.urlopen(url)
	bsObj = BeautifulSoup(html,'html.parser')
	return  ''<html>
<body>
<h1>''+ bsObj  +''</h1>
</body>
</html>'''



#	response=requests.get(url)
#	fpath="./templates/%s.html" %s key
'''	fpath="templates/cc.html"
	file=open(fpath,'w')
	file.write(str(bsObj))
	sleep(10)
	file.close()
	return render_template('cc.html')	'''
#	return str(bsObj)
'''	return ''<html>
<body>
<h1>url</h1>
</body>
</html>''
'''	
if __name__=='__main__':
#	handler = logging.FileHandler(r'../logs/flask2.log', encoding='UTF-8')
#	handler.setLevel(logging.DEBUG)
#	logging_format = logging.Formatter(
#        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
#	handler.setFormatter(logging_format)
#	app.logger.addHandler(handler)
	app.run(host='0.0.0.0',port=5001,debug=True)
