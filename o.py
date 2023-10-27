from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self, report_data):
        pass

class PdfExporter(ReportExporter):
    def export(self, report_data):
        pass

class CsvExporter(ReportExporter):
    def export(self, report_data):
        pass

class HtmlExporter(ReportExporter):
    def export(self, report_data):
        pass