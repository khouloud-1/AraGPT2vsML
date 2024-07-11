<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:dt="uuid:C2F41010-65B3-11d1-A29F-00AA00C14882"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List href="index_files/filelist.xml">
<link rel=themeData href="index_files/themedata.thmx">
<link rel=colorSchemeMapping href="index_files/colorschememapping.xml">
</head>

<body lang=EN-US link="#0563C1" vlink="#954F72" style='tab-interval:.5in;
word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><span style='font-size:40.0pt;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>HATC: fine-tuned AraGPT2 vs ML algo</span></b></p>


<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>By:
<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;line-height:normal;layout-grid-mode:
char;mso-layout-grid-align:none'><b><span style='font-family:"Times New Roman",serif;
mso-fareast-font-family:"Times New Roman";mso-font-kerning:0pt;mso-ligatures:
none;mso-fareast-language:EN-GB'>Djelloul BOUCHIHA<sup>1</sup>, Abdelghani
BOUZIANE<sup>1</sup>, Noureddine DOUMI<sup>2</sup>, and Benamar HAMZAOUI<sup>1</sup><o:p></o:p></span></b></p>

<p class=MsoNormal style='margin-bottom:0in;tab-stops:center 226.75pt left 5.0in'><i
style='mso-bidi-font-style:normal'><sup><span style='font-size:10.0pt;
line-height:107%;font-family:"Times New Roman",serif;mso-ascii-theme-font:major-bidi;
mso-hansi-theme-font:major-bidi;mso-bidi-theme-font:major-bidi;mso-font-kerning:
0pt;mso-ligatures:none;mso-fareast-language:EN-GB'>1</span></sup></i><i
style='mso-bidi-font-style:normal'><span style='font-size:10.0pt;line-height:
107%;font-family:"Times New Roman",serif;mso-ascii-theme-font:major-bidi;
mso-hansi-theme-font:major-bidi;mso-bidi-theme-font:major-bidi;mso-font-kerning:
0pt;mso-ligatures:none;mso-fareast-language:EN-GB'> University center of Naama
&amp; EEDIS lab., Algeria<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-bottom:0in'><i style='mso-bidi-font-style:
normal'><sup><span style='font-size:10.0pt;line-height:107%;font-family:"Times New Roman",serif;
mso-ascii-theme-font:major-bidi;mso-hansi-theme-font:major-bidi;mso-bidi-theme-font:
major-bidi;mso-font-kerning:0pt;mso-ligatures:none;mso-fareast-language:EN-GB'>2</span></sup></i><i
style='mso-bidi-font-style:normal'><span style='font-size:10.0pt;line-height:
107%;font-family:"Times New Roman",serif;mso-ascii-theme-font:major-bidi;
mso-hansi-theme-font:major-bidi;mso-bidi-theme-font:major-bidi;mso-font-kerning:
0pt;mso-ligatures:none;mso-fareast-language:EN-GB'> University of Saida,
Algeria<o:p></o:p></span></i></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>This
page allows you to run two hierarchical Arabic text classifiers:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><i><u><span style='font-size:12.0pt;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>1. Fine-tuned AraGPT2: You need to download
the following files<o:p></o:p></span></u></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><a href="fine-tuning_AraGPT2.py"><span style='mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>fine-tuning_AraGPT2.py</span></a><span
style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><a href="WiHArD_GPT.csv"><span style='mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>WiHArD_GPT.csv</span></a><span
style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><i><u><span style='font-size:12.0pt;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>2. Machine learning algorithm: You need to
download the following files <o:p></o:p></span></u></i></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><a href="Doc2Vec-DecisionTreeModel.py"><span style='mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>Doc2Vec-DecisionTreeModel.py</span></a><span
style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><a href="arabic-stop-words.txt"><span style='mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>arabic-stop-words.txt</span></a><span
style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><a href="WiHArD.hierarchy.xml"><span style='mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>WiHArD.hierarchy.xml</span></a><span
style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><a href="WiHArD.csv"><span style='mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>WiHArD.csv</span></a><span style='mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><span style='font-size:14.0pt;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Before running the two classifiers, Install
Necessary Libraries<o:p></o:p></span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;mso-font-kerning:0pt;mso-ligatures:
none'>Ensure you have the transformers and torch libraries installed, along
with any other necessary libraries:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-family:"Arial",sans-serif;mso-ascii-theme-font:minor-bidi;
mso-hansi-theme-font:minor-bidi;mso-bidi-theme-font:minor-bidi'>pip install
transformers torch pandas scikit-learn<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><span style='font-size:14.0pt;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Eventual error message<o:p></o:p></span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>If
you encounter the following message:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span class=SpellE><span style='font-family:"Arial",sans-serif;
mso-ascii-theme-font:minor-bidi;mso-hansi-theme-font:minor-bidi;mso-bidi-theme-font:
minor-bidi'>ImportError</span></span><span style='font-family:"Arial",sans-serif;
mso-ascii-theme-font:minor-bidi;mso-hansi-theme-font:minor-bidi;mso-bidi-theme-font:
minor-bidi'>: Using the `Trainer` with `<span class=SpellE>PyTorch</span>`
requires `accelerate&gt;=0.20.1`: <o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>Please
run `</span><span style='font-family:"Arial",sans-serif;mso-ascii-theme-font:
minor-bidi;mso-hansi-theme-font:minor-bidi;mso-bidi-theme-font:minor-bidi'>pip
install transformers[torch]</span><span style='mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>` or `</span><span style='font-family:"Arial",sans-serif;
mso-ascii-theme-font:minor-bidi;mso-hansi-theme-font:minor-bidi;mso-bidi-theme-font:
minor-bidi'>pip install accelerate -U</span><span style='mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin'>`<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><span style='font-size:14.0pt;mso-bidi-font-family:Calibri;
mso-bidi-theme-font:minor-latin'>Contact<o:p></o:p></span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'>For
help, don’t hesitate to contact me: <a href="mailto:bouchiha@cuniv-naama.dz">bouchiha@cuniv-naama.dz</a>
<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin'><o:p>&nbsp;</o:p></span></p>

</div>

</body>

</html>
