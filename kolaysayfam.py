#!/usr/bin/python3 
# -*- coding: utf-8 -*-
from gi.repository import Gtk 
import datetime
import re
import os
import gi

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
acaba="86400"
entry7koru=""
resim=""
resmineni="100"
label5 = builder.get_object("label5")
button3 = builder.get_object("button3")
button5 = builder.get_object("button5")
messagedialog1 = builder.get_object("messagedialog1")
messagedialog2 = builder.get_object("messagedialog2")
toolbar1 = builder.get_object("toolbar1")
toolbar2 = builder.get_object("toolbar2")
button11 = builder.get_object("button11")
button12 = builder.get_object("button12")



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
	

icerik="""<!DOCTYPE html>
<html>
<head>
<meta name="generator" content="Kolaysayfam 0.38" >
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="date" content="{}" >
<meta name="description" content="{}">
<meta name="keywords" content="{}">
<meta http-equiv="expires" content="{}">
<meta http-equiv="content-style-type" content="text/css">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="content-language" content="tr">
<meta name="robots" content="all">
<meta name="robots" content="index,follow">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<link rel="icon" href="favicon.png" type="image/x-icon" />
<title>{}</title>
<style>* {{margin:0;padding:0;}}
a {{text-decoration:underline;color:#2A3436;}}
body {{background:{};font-family:{};font-size:{};margin:10px;color:{};background-image:url({});text-align:{};}}
span{{font-size:{}px}}
p{{margin-top: 2px;}}
br{{line-height:1px;}}
</style>
</head>
<body>
<h3><span>{}</span></h3>
<p>{}</p>
<Img src="{}" wIdth="{}%" alt="">
</body>
</html>
"""

def dosyaya_yazdir():
	renk1=colorbutton1.get_color().to_string()
	renk2=colorbutton2.get_color().to_string()	
	bgcolor=renk1[0]+renk1[1]+renk1[2]+renk1[5]+renk1[6]+renk1[9]+renk1[10]
	fontcolor=renk2[0]+renk2[1]+renk2[2]+renk2[5]+renk2[6]+renk2[9]+renk2[10]
	aa = datetime.datetime.today()
	tarih = aa.strftime("%d.%m.%Y-%H:%M:%S")
	tanim=entry5.get_text()	
	keywords=entry4.get_text()
	title1 = entry1.get_text()
	yazibaslik = entry3.get_text()
	textbuffer = textview1.get_buffer()
	listem = textbuffer.get_property("text")
	yazi1 =  listem.replace("\n","<br>")
	sayfaadi = entry6.get_text()
	sb1=spinbutton1.get_text()
	cbt2=comboboxtext2.get_active_text()
	cbt3=comboboxtext3.get_active_text()
	hizalama=textview1.get_justification().value_name
	if hizalama.endswith("LEFT"):
		hiza = "left"
	elif hizalama.endswith("RIGHT"):
		hiza = "right"
	elif hizalama.endswith("CENTER"):
		hiza = "center" 
	dosya=open(sayfaadi+".html", "w")
	formatli = icerik.format(tarih,tanim,keywords,acaba,title1,bgcolor,cbt2,cbt3,fontcolor,entry7koru,hiza,sb1,yazibaslik,yazi1,resim,resmineni)
	print(formatli, file=dosya)
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
	aa = datetime.datetime.today()
	tarih = aa.strftime("%d%m%Y_%H%M%S")
	tanim=entry5.get_text()	
	keywords=entry4.get_text()
	title1 = entry1.get_text()
	sayfaadi = entry6.get_text()	
	yazibaslik = entry3.get_text()	
	textbuffer = textview1.get_buffer()
	yazi1 = textbuffer.get_property("text")
	ab=tarih+".ksa"
	sb1=spinbutton1.get_text()
	cbt2=comboboxtext2.get_active_text()
	cbt3=comboboxtext3.get_active_text()
	hizalama=textview1.get_justification().value_name	
	kayit = open(ab, "w")
	kaydedilen = title1+"\n"+yazibaslik+"\n"+hizalama+"\n"+keywords+"\n"+tanim+"\n"+entry7koru+"\n"+acaba+"\n"+str(red)+' '+str(green)+' '+str(blue)+"\n"+str(red2)+' '+str(green2)+' '+str(blue2)+"\n"+sb1+"\n"+cbt2+"\n"+cbt3+"\n"+resim+"\n"+resmineni+"\n"+sayfaadi+"\n"+yazi1
	print(kaydedilen, file=kayit)
	kayit.close()	
	label2.set_text(ab+" isimli şablonunuz kaydedilmiştir.")
	return 0
	
def dosyaac2(asd):
	kayit = open(asd, "r")	
	entry_1 = kayit.readline().strip()
	entry_3 = kayit.readline().strip()
	hizalama= kayit.readline().strip()
	entry_4 = kayit.readline().strip()
	entry_5 = kayit.readline().strip()
	global entry7koru
	entry7koru = kayit.readline().strip()
	global acaba, resim, resmineni
	acaba = kayit.readline().strip()
	red,green,blue = kayit.readline().split()
	red2,green2,blue2 = kayit.readline().split()
	sb1 = kayit.readline().strip()
	cbt2 = kayit.readline().strip()
	cbt3 = kayit.readline().strip()
	resim=kayit.readline().strip()
	resmineni=kayit.readline().strip()
	sayfaadi = kayit.readline().strip()
	listem=kayit.readlines()
	textview_1=""
	i=0
	while i < len(listem) :
		textview_2 = listem[i]
		textview_1 = textview_1+textview_2
		i=i+1	
	entry5.set_text(entry_5)
	entry4.set_text(entry_4)
	entry1.set_text(entry_1)
	entry3.set_text(entry_3)
	textview1.get_buffer().set_text(textview_1)
	entry6.set_text(sayfaadi)
	bgcolor_1 = gi.overrides.Gdk.Color(int(red),int(green),int(blue))
	fontcolor_1 = gi.overrides.Gdk.Color(int(red2),int(green2),int(blue2))	
	colorbutton1.set_color(bgcolor_1)	
	colorbutton2.set_color(fontcolor_1)
	spinbutton1.set_text(sb1)
	comboboxtext2.set_active_id(cbt2)
	comboboxtext3.set_active_id(cbt3)	
	renk22 = colorbutton1.get_color()
	textview1.modify_bg(0,renk22)
	renk33 = colorbutton2.get_color()
	textview1.modify_fg(0,renk33)
	if hizalama=="GTK_JUSTIFY_LEFT":
		textview1.set_justification(Gtk.Justification.LEFT)
		radio_justifyleft.set_active(1)
		print(dir(radio_justifyleft))
	elif hizalama=="GTK_JUSTIFY_RIGHT":
		textview1.set_justification(Gtk.Justification.RIGHT)
		radio_justifyright.set_active(1)		
	elif hizalama=="GTK_JUSTIFY_CENTER":
		textview1.set_justification(Gtk.Justification.CENTER)
		radio_justifycenter.set_active(1)
	kayit.close()
	return 0

def tamam1(sa):
	entry2=builder.get_object("entry2")
	entry7=builder.get_object("entry7")
	global acaba
	acaba=entry2.get_text()
	global entry7koru
	entry7koru=entry7.get_text()
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
		cbt2=comboboxtext2.get_active_text()
		tb = textview1.get_buffer()
		#tb.set_property("font",cbt2)
		#print(dir(tb))
		print (cbt2)
		#print(dir(textview1))
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
		entry2.set_text(acaba)
		entry7.set_text(entry7koru)
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
		global resim, resmineni		
		resim = filechooser2.get_filename()
		resmineni= spinbutton2.get_text()
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
