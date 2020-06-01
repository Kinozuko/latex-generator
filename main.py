from pylatex import Document, Section, FootnoteText, LineBreak, LargeText, SmallText, LongTable, MultiColumn, MediumText, Tabular
from pylatex.utils import bold, escape_latex
from pylatex.position import Center, VerticalSpace, HorizontalSpace
from pylatex.base_classes import Command, Options
from pylatex.package import Package
from datetime import datetime
from lorem.text import TextLorem

def obtain_pagesize(table_info_size):
	from math import floor, sqrt

	return "11in" if table_info_size <= 2 else str(11+floor(sqrt(table_info_size-2)))+"in"

lorem = lambda x : TextLorem(srange=(x,x)).sentence()

if __name__ == '__main__':
	
	geometry_options = {
		"margin" : "0.5in",
		"paperwidth":"11in"
	}

	doc = Document(
		indent=False,
		documentclass="article",
		document_options="a4paper,landscape",
		geometry_options=geometry_options,
		page_numbers=False
	)

	doc.packages.append(Package("array"))

	# Header
	with doc.create(Center()) as centered:
		centered.append(FootnoteText(bold(lorem(4))))
		centered.append(FootnoteText(lorem(12)))
		centered.append(LineBreak())
		centered.append(FootnoteText(lorem(19)))
		centered.append(LineBreak())
		centered.append(FootnoteText(lorem(17)))
		centered.append(LineBreak())
		centered.append(FootnoteText(lorem(17)))
	
		centered.append(LineBreak())
		centered.append(LineBreak())

		centered.append(MediumText(bold(lorem(5))))

	# Title
	doc.append(HorizontalSpace("250pt"))

	with doc.create(Tabular(table_spec="|l r|",row_height=1.8)) as data_table:
		data_table.add_hline()
		data_table.add_row([MediumText(bold(lorem(3))),MediumText(bold("XXXXXXXXXXXXXX"))])
		data_table.add_hline()

	
	doc.append(HorizontalSpace("160pt"))

	with doc.create(Tabular(table_spec="|c|",row_height=1.8)) as date_table:
		date_table.add_hline()
		date_table.add_row((FootnoteText(lorem(1)),))
		date_table.add_hline()
		date_table.add_row((SmallText(bold(str(datetime.now())[0:10])),))
		date_table.add_hline()


	doc.append(LineBreak())
	doc.append(LineBreak())
	doc.append(LineBreak())

	# Name - Register - Period

	with doc.create(Tabular(table_spec="|m{100cm}|")) as name_table:
		name_table.add_hline()
		name_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(8))),))
		name_table.add_hline()
		name_table.add_row((MultiColumn(1,align="|c|",data=SmallText(bold(lorem(3)))),))
		name_table.add_hline()

	doc.append(HorizontalSpace("50pt"))

	with doc.create(Tabular(table_spec="|m{100cm}|")) as register_table:
		register_table.add_hline()
		register_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(9))),))
		register_table.add_hline()
		register_table.add_row((MultiColumn(1,align="|c|",data=SmallText(bold("X-XXXXXXXX-X"))),))
		register_table.add_hline()
 	
	doc.append(HorizontalSpace("56pt"))
	
	with doc.create(Tabular(table_spec="|m{100cm}|")) as period_table:
		period_table.add_hline()
		period_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(2))),))
		period_table.add_hline()
		period_table.add_row((MultiColumn(1,align="|c|",data=SmallText(bold(lorem(2)+"XXXX"))),))
		period_table.add_hline()

	

	doc.append(LineBreak())
	doc.append(LineBreak())
	doc.append(LineBreak())

	# Direcction

	with doc.create(Tabular(table_spec="m{27.71cm}")) as direction_table:
		direction_table.add_hline()
		direction_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(4))),))
		direction_table.add_hline()
		direction_table.add_row((MultiColumn(1,align="|c|",data=SmallText(lorem(5))),))
		direction_table.add_hline()
		direction_table.add_empty_row()


	doc.append(LineBreak())
	# Name - Register (2)

	with doc.create(Tabular(table_spec="|m{100cm}|")) as name_table:
		name_table.add_hline()
		name_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(8))),))
		name_table.add_hline()
		name_table.add_row((MultiColumn(1,align="|c|",data=SmallText(bold(lorem(2)))),))
		name_table.add_hline()

	doc.append(HorizontalSpace("227pt"))

	with doc.create(Tabular(table_spec="|m{100cm}|")) as register_table:
		register_table.add_hline()
		register_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(9))),))
		register_table.add_hline()
		register_table.add_row((MultiColumn(1,align="|c|",data=SmallText(bold("X-XXXXXXXX-X"))),))
		register_table.add_hline()

	

	doc.append(LineBreak())
	doc.append(LineBreak())
	doc.append(LineBreak())

	with doc.create(Tabular(table_spec="m{27.71cm}")) as direction_table:
		direction_table.add_hline()
		direction_table.add_row((MultiColumn(1,align="|c|",data=FootnoteText(lorem(5))),))
		direction_table.add_hline()
		direction_table.add_row((MultiColumn(1,align="|c|",data=SmallText(lorem(6))),))
		direction_table.add_hline()
		direction_table.add_empty_row()

	#Info table

	with doc.create(LongTable(table_spec="|m{1cm}|m{1.7cm}|m{1.6cm}|m{1.9cm}|m{1.8cm}|m{1.8cm}|m{1.5cm}|m{1.6cm}|m{1.8cm}|m{1.6cm}|m{1.6cm}|m{1.2cm}|m{1.4cm}|m{1.4cm}|")) as info_table:
		info_table.add_hline()
		info_table.add_row(
			FootnoteText(lorem(1)),
			FootnoteText(lorem(3)),
			FootnoteText(lorem(3)),
			FootnoteText(lorem(4)),
			FootnoteText(lorem(3)),
			FootnoteText(lorem(3)),
			FootnoteText(lorem(3)),
			FootnoteText(lorem(3)),
			FootnoteText(lorem(4)),
			FootnoteText(lorem(4)),
			FootnoteText(lorem(2)),
			FootnoteText(lorem(2)),
			FootnoteText(lorem(2)),
			FootnoteText(bold(lorem(1)))
		)		
		
		info_table.add_hline()

		for i in range(15):
			info_table.add_row(
				i+1,
				str(datetime.now())[0:10],
				"xxxxxxxx",
				"xxxxxx",
				lorem(1),
				lorem(1),
				lorem(1),
				lorem(1),
				"x.xxx,xx",
				"x.xx",
				"x.xxx,xx",
				"xx.x",
				"xxx.x",
				bold("xx.xx")
			)
			info_table.add_hline()

		total_row = (
			MultiColumn(8,align="|r|",data=lorem(1)),
			"x.xxx,xx",
			"x.xx",
			"xxxx.xx",
			MultiColumn(2,align="c|",data="xxx,xx"),
			bold("xx.xx")
		)
		info_table.add_row(total_row)
		info_table.add_hline()
	#foter

	with doc.create(Center()) as centered:
		centered.append(FootnoteText(lorem(20)))
		centered.append(LineBreak())
		centered.append(FootnoteText(lorem(15)))
	
		centered.append(LineBreak())

	#Firmas

	doc.append(HorizontalSpace("75pt"))
	
	with doc.create(Tabular(table_spec="|m{4cm} m{5cm}|")) as firm:
		firm.add_hline()
		firm.add_row((MultiColumn(2,align="|c|",data=lorem(3)),))
		for i in range(4):
			firm.add_empty_row()
		firm.add_row((MultiColumn(2,align="|c|",data="xx/xx/xxxx"),))
		firm.add_hline()


	doc.append(HorizontalSpace("125pt"))

	with doc.create(Tabular(table_spec="|m{4cm} m{5cm}|")) as firm:
		firm.add_hline()
		firm.add_row((MultiColumn(2,align="|c|",data=lorem(3)),))
		for i in range(5):
			firm.add_empty_row()
		firm.add_hline()

	doc.append(LineBreak())
	doc.append(LineBreak())
	doc.append(HorizontalSpace("140pt"))
	doc.append(lorem(3))
	doc.append(HorizontalSpace("300pt"))
	doc.append(lorem(3))

	doc.generate_pdf('doc/full',clean_tex=False,compiler='pdflatex')
