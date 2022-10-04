from django_line_notification.line_notify import Line

token = 'IVEPjq212HjciMhN1YICj3iD3mf3E6sXNffpiW88HTw'
line = Line(token)
line.send_msg('foobar')