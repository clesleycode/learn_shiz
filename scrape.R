library(pdftools)

eval <- pdf_text("eval.pdf")
for (i in eval) { 
	print(strsplit(i,"\n"))
	}
