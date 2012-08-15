import qstat
from ConfigParser import ConfigParser
import time
import os.path
# http://werkzeug.pocoo.org/docs/tutorial/#step-0-a-basic-wsgi-introduction
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
# http://jinja.pocoo.org/docs/api/
from jinja2 import Environment, FileSystemLoader



cfg = ConfigParser()
cfg.read("frodo.properties")
host = cfg.get('web','host')
port = cfg.getint('web','port')
dev = cfg.getboolean('web','development')    
env = Environment(loader=FileSystemLoader('./templates'), auto_reload=dev)

@Request.application
def application(request):
    now = time.asctime()
    fields,records = qstat.parse_qstat1(qstat.exec_qstat())
    summary = qstat.summarize1(fields,records)
    template = env.get_template("qstat.html")
    html = template.render(time=now, summary=summary, fields=fields, records=records)
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    run_simple(host, port, application, static_files = {'/static':  os.path.join(os.path.dirname(__file__), 'static')}, use_debugger=dev, use_reloader=dev, extra_files=['frodo.properties','qstat.py'])
