from docling.document_converter import DocumentConverter

#resource provided by Dauphin county for local resources. this PDF is also reflected on this page in a web format.
#https://harrisburgpa.gov/community/community_resources.php
source = "./2024-where-to-go-when-you-need-help-2024.pdf"  # file path or URL

converter = DocumentConverter()
#If you are getting errors for running out of memory, adding a pagerange should help with the issue
doc = converter.convert(source,page_range=(1, 10)).document
#Save result to file
with open('ocr_result.txt', 'w', encoding='utf-8') as f:
    f.write(doc.export_to_markdown())
