#!/usr/bin/python3 
# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gdk, Pango
import datetime
import re
import os
import gi
from string import Template



builder = Gtk.Builder()
builder.add_from_file("kolaysayfam.glade")
window = builder.get_object("window1")
window2 = builder.get_object("window2")
entry1 = builder.get_object("entry1")
textview1 = builder.get_object("textview1")
entry3 = builder.get_object("entry3")
label2 = builder.get_object("label2")
entry4 = builder.get_object("entry4")
entry5 = builder.get_object("entry5")
entry6 = builder.get_object("entry6")	
colorbutton1 = builder.get_object("colorbutton1")
colorbutton2 = builder.get_object("colorbutton2")
dialog = builder.get_object("aboutdialog1")
filechooser = builder.get_object("filechooserdialog1")
filechooser2 = builder.get_object("filechooserdialog2")
spinbutton1 = builder.get_object("spinbutton1")
spinbutton2 = builder.get_object("spinbutton2")
comboboxtext2 = builder.get_object("comboboxtext2")
comboboxtext3 = builder.get_object("comboboxtext3")
expires="86400"
resimyuzde="100"
label5 = builder.get_object("label5")
button3 = builder.get_object("button3")
button5 = builder.get_object("button5")
messagedialog1 = builder.get_object("messagedialog1")
messagedialog2 = builder.get_object("messagedialog2")
toolbar1 = builder.get_object("toolbar1")
toolbar2 = builder.get_object("toolbar2")
button11 = builder.get_object("button11")
button12 = builder.get_object("button12")
togglebutton1 = builder.get_object("togglebutton1")
aa = datetime.datetime.today()
tarih = aa.strftime("%Y-%m-%dT%H:%M:%S+0200")

textsondurum=textview1.get_buffer()
tag_bold = textsondurum.create_tag("bold",weight=Pango.Weight.BOLD)
tag_normal = textsondurum.create_tag("normal",weight=Pango.Weight.NORMAL)
tag_italic = textsondurum.create_tag("italic",style=Pango.Style.ITALIC)
tag_underline = textsondurum.create_tag("underline",underline=Pango.Underline.SINGLE)
tag_found = textsondurum.create_tag("found",background="yellow")


def on_justify_toggled(widget,justification):
	textview1.set_justification(justification)	
	
#def on_button_clicked(widget, tag):
#		bounds = textview1.textbuffer.get_selection_bounds()
#		if len(bounds) != 0:
#			start, end = bounds
#			textview1.textbuffer.apply_tag(tag, start, end)

radio_justifyleft = Gtk.RadioToolButton()
radio_justifyleft.set_stock_id(Gtk.STOCK_JUSTIFY_LEFT)
radio_justifycenter = Gtk.RadioToolButton.new_with_stock_from_widget(radio_justifyleft, Gtk.STOCK_JUSTIFY_CENTER)
radio_justifyright = Gtk.RadioToolButton.new_with_stock_from_widget(radio_justifyleft, Gtk.STOCK_JUSTIFY_RIGHT)
toolbar1.insert(radio_justifyleft,0)
toolbar1.insert(radio_justifyright,1)
toolbar2.insert(radio_justifycenter,0)
radio_justifyleft.connect("toggled", on_justify_toggled,Gtk.Justification.LEFT)
radio_justifycenter.connect("toggled", on_justify_toggled,Gtk.Justification.CENTER)
radio_justifyright.connect("toggled", on_justify_toggled,Gtk.Justification.RIGHT)
	






icerik=Template("""<!DOCTYPE html>
<html>
<head>
<meta name="generator" content="Kolaysayfam 0.40" >
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="date" content="$tarih" >
<meta name="description" content="$description">
<meta name="keywords" content="$keywords">
<meta http-equiv="expires" content="$expires">
<meta http-equiv="content-style-type" content="text/css">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="content-language" content="tr">
<meta name="robots" content="all">
<meta name="robots" content="index,follow">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<link rel="icon" href="favicon.png" type="image/x-icon" />
<title>$title</title>
<style>* {{margin:0;padding:0;}}
a {text-decoration:underline;color:#2A3436;}
body {background:$bgcolor22;font-family:$yazi1font;font-weight:$kalinlik;font-size:$yazi1size;margin:10px;color:$fontcolor22;background-image:url($template);text-align:$hiza;}
span{font-size:$yazi1basliksize}
p{margin-top: 2px;}
br{line-height:1px;}
</style>
</head>
<body>
<h3><span>$yazi1baslik</span></h3>
<p>$textview_1</p>
<Img src="$resim" wIdth="$resimyuzde%" alt="">
</body>
</html>
"""
)




def dosyaac2(asd):
	kayit = open(asd, "r")	
	global title,yazi1baslik,hiza,description,keywords,template,expires,bgcolor22,fontcolor22,yazi1basliksize,yazi1font,yazi1size,resim,resimyuzde,sayfaadi,kalinlik1,textview_1 
	title,yazi1baslik,hiza,description,keywords,template,expires,bgcolor22,fontcolor22 \
	,yazi1basliksize,yazi1font,yazi1size,resim,resimyuzde,sayfaadi,kalinlik1,textview_1  \
	= "","","","","","","","","","","","","","","","",""

	title = kayit.readline().strip()
	yazi1baslik = kayit.readline().strip()
	hizalama= kayit.readline().strip()
	description = kayit.readline().strip()
	keywords = kayit.readline().strip()
	template= kayit.readline().strip()
	expires = kayit.readline().strip()
	red,green,blue = kayit.readline().split()
	red2,green2,blue2 = kayit.readline().split()
	bgcolor_1 = gi.overrides.Gdk.Color(int(red),int(green),int(blue))
	fontcolor_1 = gi.overrides.Gdk.Color(int(red2),int(green2),int(blue2))	
	bgcolor11=gi.overrides.Gdk.Color.to_string(bgcolor_1)
	fontcolor11=gi.overrides.Gdk.Color.to_string(fontcolor_1)
	bgcolor22=bgcolor11[0]+bgcolor11[1]+bgcolor11[2]+bgcolor11[5]+bgcolor11[6]+bgcolor11[9]+bgcolor11[10]
	fontcolor22=fontcolor11[0]+fontcolor11[1]+fontcolor11[2]+fontcolor11[5]+fontcolor11[6]+fontcolor11[9]+fontcolor11[10]
	colorbutton1.set_color(bgcolor_1)	
	colorbutton2.set_color(fontcolor_1)
	sb1 = kayit.readline().strip()
	yazi1basliksize = sb1+"pt"		
	yazi1font = kayit.readline().strip()
	yazi1size = kayit.readline().strip()	
	yazi1size = yazi1size.replace("x","t")
	resim=kayit.readline().strip()
	resimyuzde=kayit.readline().strip()	
	sayfaadi = kayit.readline().strip()
	kalinlik1= kayit.readline().strip()	
	if kalinlik1 == "bold" :
		kalinlik1=1
	else:
		kalinlik1=0	

	print(sayfaadi)	
	
	listem=kayit.readlines()
	i=0
	while i < len(listem) :
		textview_2 = listem[i]
		textview_1 = textview_1+textview_2
		i=i+1	
				
	entry5.set_text(keywords)
	entry4.set_text(description)
	entry1.set_text(title)
	entry3.set_text(yazi1baslik)
	textview1.get_buffer().set_text(textview_1)
	entry6.set_text(sayfaadi)
	spinbutton1.set_text(sb1)
	comboboxtext2.set_active_id(yazi1font)
	comboboxtext3.set_active_id(yazi1size)	
	renk22 = colorbutton1.get_color()
	textview1.modify_bg(0,renk22)
	renk33 = colorbutton2.get_color()
	textview1.modify_fg(0,renk33)
	if hizalama=="GTK_JUSTIFY_LEFT":
		textview1.set_justification(Gtk.Justification.LEFT)
		radio_justifyleft.set_active(1)
	elif hizalama=="GTK_JUSTIFY_RIGHT":
		textview1.set_justification(Gtk.Justification.RIGHT)
		radio_justifyright.set_active(1)		
	elif hizalama=="GTK_JUSTIFY_CENTER":
		textview1.set_justification(Gtk.Justification.CENTER)
		radio_justifycenter.set_active(1)
	hizalama=textview1.get_justification().value_name
	if hizalama.endswith("LEFT"):
		hiza = "left"
	elif hizalama.endswith("RIGHT"):
		hiza = "right"
	elif hizalama.endswith("CENTER"):
		hiza = "center" 
	global d	
	togglebutton1.set_active(kalinlik1)	
	d = dict(tarih=tarih,title=title,yazi1baslik=yazi1baslik,hiza=hiza,description=description,keywords=keywords, \
	template=template,expires=expires,bgcolor22=bgcolor22,fontcolor22=fontcolor22, \
	yazi1basliksize=yazi1basliksize,yazi1font=yazi1font,yazi1size=yazi1size,resim=resim,resimyuzde=resimyuzde, \
	sayfaadi=sayfaadi,kalinlik=kalinlik1,textview_1=textview_1)
	textview_1=""	
	kayit.close()
	return 0


def dosyaya_yazdir():
	renk1=colorbutton1.get_color().to_string()
	renk2=colorbutton2.get_color().to_string()	
	bgcolor=renk1[0]+renk1[1]+renk1[2]+renk1[5]+renk1[6]+renk1[9]+renk1[10]
	fontcolor=renk2[0]+renk2[1]+renk2[2]+renk2[5]+renk2[6]+renk2[9]+renk2[10]
	tanim=entry5.get_text()	
	keywords=entry4.get_text()
	title1 = entry1.get_text()
	yazibaslik = entry3.get_text()
	textbuffer = textview1.get_buffer()
	listem = textbuffer.get_property("text")
	yazi1 =  listem.replace("\n","<br>")
	sayfaadi = entry6.get_text()
	sb1=spinbutton1.get_text()
	sb1=sb1+"pt"
	yazi1font=comboboxtext2.get_active_text()
	yazi1size=comboboxtext3.get_active_text()
	hizalama=textview1.get_justification().value_name
	kalinlik=str(togglebutton1.get_active())
	if kalinlik == "True" :
		kalinlik="bold"
	else :
		kalinlik="normal"	
	if hizalama.endswith("LEFT"):
		hiza = "left"
	elif hizalama.endswith("RIGHT"):
		hiza = "right"
	elif hizalama.endswith("CENTER"):
		hiza = "center" 
	dosya=open(sayfaadi+".html", "w")
	d = dict(tarih=tarih,title=title1,yazi1baslik=yazi1baslik,hiza=hiza,description=description,keywords=keywords, \
	template=template,expires=expires,bgcolor22=bgcolor,fontcolor22=fontcolor, \
	yazi1basliksize=sb1,yazi1font=yazi1font,yazi1size=yazi1size,resim=resim,resimyuzde=resimyuzde, \
	sayfaadi=sayfaadi,kalinlik=kalinlik,textview_1=yazi1)
	print(icerik.safe_substitute(d), file=dosya)
	dosya.close()
	label2.set_text("Web sayfanız kullanıma hazırdır: "+sayfaadi+".html "+tarih)
	return 0

def bilgilerial():
	renk1=colorbutton1.get_color()
	red=renk1.red
	green=renk1.green
	blue=renk1.blue
	renk2=colorbutton2.get_color()
	red2=renk2.red
	green2=renk2.green
	blue2=renk2.blue
	tarih1 = aa.strftime("%d%m%Y_%H%M%S")
	tanim=entry5.get_text()	
	keywords=entry4.get_text()
	title1 = entry1.get_text()
	sayfaadi = entry6.get_text()	
	yazibaslik = entry3.get_text()	
	textbuffer = textview1.get_buffer()
	yazi1 = textbuffer.get_property("text")
	ab=tarih1+".ksa"
	sb1=spinbutton1.get_text()
	yazi1font=comboboxtext2.get_active_text()
	yazi1size=comboboxtext3.get_active_text()
	hizalama=textview1.get_justification().value_name	
	kalinlik=str(togglebutton1.get_active())
	if kalinlik == "True" :
		kalinlik="bold"
	else :
		kalinlik="normal"
	kayit2 = open(ab, "w")
	kaydedilen = title1+"\n"+yazibaslik+"\n"+hizalama+"\n"+keywords+"\n"+tanim+"\n"+template+"\n"+expires+"\n"+str(red)+' '+str(green)+' '+str(blue)+"\n"+str(red2)+' '+str(green2)+' '+str(blue2)+"\n"+sb1+"\n"+yazi1font+"\n"+yazi1size+"\n"+resim+"\n"+resimyuzde+"\n"+sayfaadi+"\n"+kalinlik+"\n"+yazi1
	print(kaydedilen, file=kayit2)
	kayit2.close()	
	label2.set_text(ab+" isimli şablonunuz kaydedilmiştir.")
	return 0
	


def tamam1(sa):
	entry2=builder.get_object("entry2")
	entry7=builder.get_object("entry7")
	global expires
	expires=entry2.get_text()
	global template
	template=entry7.get_text()
	w77.hide()

	
class Handler:
	def yazdir(self, button):
		dosyaya_yazdir()
	def cikis(self,action,ek3):
		Gtk.main_quit()
	def hakkinda(self,imagemenuitem,eventbutton):
		dialog.run()
		dialog.hide()
	def kaydet(self,action,ek3):
		bilgilerial()
	def dosyaac(self,action):		
		af = filechooser.get_filename()
		if af.endswith(".ksa"):
			dosyaac2(af)
			filechooser.hide()
			label2.set_text(af+" açılmıştır")
		else:
			filechooser.hide()
			label2.set_text("LÜTFEN BU PROGRAM ARACILIĞI İLE KAYDETTİĞİNİZ KSA UZANTILI BİR DOSYA SEÇİNİZ")
			if label5.get_text()=="Lütfen bu program aracılığı ile kaydettiğiniz ksa uzantılı bir dosya seçiniz":			
				messagedialog2.show()
	def dosyaac1(self,action,ek3):
		label5.set_text("Lütfen bu program aracılığı ile kaydettiğiniz ksa uzantılı bir dosya seçiniz")
		filechooser.show()
		button3.connect("clicked",self.dosyaac)		
	def iptal(self,action):
		filechooser.hide()		
	def cikis4(self,action):
		messagedialog1.hide()
	def cikis6(self,action):
		messagedialog2.hide()			
	def templateac(self,action):
		label5.set_text("Lütfen jpg uzatınlı bir dosya seçiniz")
		filechooser.show()
		button3.connect("clicked",self.templateac2)		
	def templateac2(self,action):
		global af2		
		af2 = filechooser.get_filename()
		if af2.endswith(".jpg"):			
			filechooser.hide()
			entry7.set_text(af2)
			label2.set_text(af2+" arkaplan görüntüsü (template) olarak kaydedilmiştir")
		else:
			filechooser.hide()
			label2.set_text("LÜTFEN JPG UZANTILI BİR DOSYA SEÇİNİZ")
			if label5.get_text()=="Lütfen jpg uzatınlı bir dosya seçiniz":
				messagedialog1.show()
	def renktakibi(self,action):
		renk22 = action.get_color()
		textview1.modify_bg(0,renk22)
	def renktakibi2(self,action):
		renk33 = action.get_color()
		textview1.modify_fg(0,renk33)
	def texttipi(self,action):
		yazi1font=comboboxtext2.get_active_text()
		yazi1fontbuyukluk=comboboxtext3.get_active_text()
		yazi1fontbuyukluk=yazi1fontbuyukluk.replace("t","x")
		kisalt57=yazi1font+" "+yazi1fontbuyukluk
		fonttanim = Pango.FontDescription(kisalt57)
		textview1.modify_font(fonttanim)
		if togglebutton1.get_active() == True :
			fonttanimkalin = Pango.FontDescription("Bold")
			textview1.modify_font(fonttanimkalin)
		else :
			fonttanimnormal = Pango.FontDescription("Normal")
			textview1.modify_font(fonttanimnormal)	
	def fontdegis(self,abcv):
		yazi1font=comboboxtext2.get_active_text()
		yazi1fontbuyukluk=comboboxtext3.get_active_text()
		yazi1fontbuyukluk=yazi1fontbuyukluk.replace("t","x")
		kisalt57=yazi1font+" "+yazi1fontbuyukluk
		fonttanim = Pango.FontDescription(kisalt57)
		textview1.modify_font(fonttanim)
		if togglebutton1.get_active() == True :
			fonttanimkalin = Pango.FontDescription("Bold")
			textview1.modify_font(fonttanimkalin)
		else :
			fonttanimnormal = Pango.FontDescription("Normal")
			textview1.modify_font(fonttanimnormal)
	def fontkalinlastir(self,abcv):
		if abcv.get_active() == True :
			fonttanimkalin = Pango.FontDescription("Bold")
			textview1.modify_font(fonttanimkalin)
		else :
			fonttanimnormal = Pango.FontDescription("Normal")
			textview1.modify_font(fonttanimnormal)						
	def window2ac(self,imagemenuitem):
		w22=builder.add_objects_from_file("kolaysayfam.glade", ("window2","entry2","button4","button7","entry7","button8"))
		global w77
		w77=builder.get_object("window2")
		entry2=builder.get_object("entry2")
		global entry7
		entry7=builder.get_object("entry7")
		button4 = builder.get_object("button4")
		button7 = builder.get_object("button7")
		button8 = builder.get_object("button8")
		entry2.set_text(expires)
		entry7.set_text(template)
		w77.show()
		button7.connect("clicked",self.templateac)
		button4.connect("clicked",tamam1)
		button8.connect("clicked",self.window2sakla)		
	def window2sakla(self,action):
		w77.destroy()
	def iptal2(self,action):
		filechooser2.hide()
	def resimekle(self,action):
		filechooser2.show()
		button11.connect("clicked",self.iptal2)		
		button12.connect("clicked",self.resimekle2)
	def resimekle2(self,action):
		global resim, resimyuzde		
		resim = filechooser2.get_filename()
		resimyuzde= spinbutton2.get_text()
		if resim.endswith(".jpg"):			
			filechooser2.hide()
			label2.set_text(resim+" geçici olarak hafızaya kaydedilmiştir")
		else:
			filechooser2.hide()
			label2.set_text("LÜTFEN JPG UZANTILI BİR DOSYA SEÇİNİZ")
			messagedialog1.show()
		
		
		
builder.connect_signals(Handler())
window.show_all()
Gtk.main()

