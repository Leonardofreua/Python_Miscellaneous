#!/usr/bin/python
# -*- coding : utf-8 -*-


"""
The Chain of Responsibility design pattern is one of the twenty-three well-known GoF design patterns
that describe common solutions to recurring design problems when designing flexible and
reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

*What problems can the Chain of Responsibility design pattern solve?

- Coupling the sender of a request to its receiver should be avoided.
- It should be possible that more than one receiver can handle a request.

Implementing a request directly within the class that sends the request is inflexible because
it couples the class to a particular receiver and makes it impossible to support multiple receivers.

*What solution does the Chain of Responsibility design pattern describe?

- Define a chain of receiver objects having the responsibility, depending on run-time conditions, t
  o either handle a request or forward it to the next receiver on the chain (if any).

Reference: https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
"""


class ReportFormat(object):
    PDF = 0
    TEXT = 1


class Report(object):

    def __init__(self, format_):
        self.title = "Monthly Report"
        self.text = ['Things are going', 'really, really well.']
        self.format_ = format_


class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        self.nextHandler.handle(request)


class PDFHandler(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.PDF:
            self.output_report(request.title, request.text)
        else:
            super(PDFHandler, self).handle(request)

    def output_report(self, title, text):
        print('<html>')
        print('<head>')
        print('<title> %s </title>' % title)
        print('</head>')
        print('<body>')

        for line in text:
            print('<p> %s </p>' % line)

        print('</body>')
        print('</html>')


class TextHandler(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.TEXT:
            self.output_report(request.title, request.text)
        else:
            super(TextHandler, self).handle(request)

    def output_report(self, title, text):
        print(5 * '*' + title + 5 * '*')

        for line in text:
            print(line)


class ErrorHandler(Handler):

    def handle(self, request):
        print("Invalid request")


if __name__ == '__main__':
    report = Report(ReportFormat.TEXT)
    pdf_handler = PDFHandler()
    text_handler = TextHandler()

    pdf_handler.nextHandler = text_handler
    text_handler.nextHandler = ErrorHandler()

    pdf_handler.handle(report)

# ---- OUTPUT: ---- :
#
# *****Monthly Report*****
# Things are going
# really, really well.
