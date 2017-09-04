# -*- coding:utf8 -*-
class HtmlOutput(object):
    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        file_out = open('out.html', 'w', encoding="utf-8")
        file_out.write('<html>')
        file_out.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        file_out.write('<body>')
        file_out.write('<table border="1">')
        for item in self.data:
            file_out.write('<tr>')
            file_out.write("<td>%s</td>" % item['title'])
            file_out.write("<td>%s</td>" % item['summary'])
            file_out.write('</tr>')

        file_out.write('</table>')
        file_out.write('</body>')
        file_out.write('</html>')
