import fpdf



class ElectricRadiatorDeclarationLayout(fpdf.FPDF):

	def __init__(self):
		super().__init__(orientation='P',unit='mm',format='A4')

	def document_header(self):
		#logo Zehnder
		self.image('Layout/Zehnder.png', 145, -12)
		# font
		self.add_font('MyFont_1', '', 'C:/Windows/Fonts/arialbd.ttf', uni=True)
		self.set_font('MyFont_1', 'U', 14)
		#margin
		self.set_left_margin(30)
		self.set_right_margin(20)
		self.set_top_margin(22.5)
		#Title
		self.cell(0, 30, self.line1, ln=1, align='L')
		#line break
		self.ln(12)

	def document_content(self, name, family, CE_type):
		# font
		self.add_font('MyFont_2', '', 'C:/Windows/Fonts/arial.ttf', uni=True)
		self.set_font('MyFont_2', '', 12)
		#content
		self.cell(65,  6, self.line2, align='L')
		self.multi_cell(100, 6,'Zehnder Group Bolesławiec Sp. Z o. o.' + '\n' + 'ul. Modłowa 5' + '\n'+  'PL 59-700 Bolesławiec' + '\n\n' , align='L')
		self.cell(65, 6, self.line3,ln=2, align='L')
		self.cell(65, 6, self.line4,align='L')
		self.multi_cell(100, 6,'Zehnder Group Bolesławiec Sp. Z o. o.' + '\n' + 'ul. Modłowa 5' + '\n'+  'PL 59-700 Bolesławiec' + '\n\n', align='L')
		self.cell(65,6, self.line5)
		self.cell(100, 6, family, ln=1, align='L')
		self.cell(65,6, self.line6)
		self.cell(100, 6, name)
		#line break
		self.ln(20)

		self.cell(0,10, self.line7, ln=2)
		#choose proper norm based on CE type
		norms = self._choose_norm(CE_type)

		self.multi_cell(0, 6,self.line8 +  norms + self.line9 + "       -  EN 55014-1:2018, EN 55014-2:2016,\n       -  IEC 61000-3-2:2018, IEC 61000-3-3:2013", align='L')
		self.set_y(-95)
		self.cell(0,6,self.line10)

	def document_footer(self,today):
		#const line
		self.set_y(-45)
		# font
		self.set_font('MyFont_2', '', 10)
		#signature
		self.image('Layout/Sign.png', 135, 230)
		self.cell(80,5, 'Bolesławiec, ' + today, ln=0, align='L')
		self.multi_cell(80,5, 45*'.' + "\n" + 'Piotr Kościsz' + " " * 10 + "\n" + 'Head of PBO' + " " * 10, align='R')

	@staticmethod
	def _choose_norm(CE_type):
		'''This function return proper norms collection depend on radiator type
		Possible Types:
		-A 		- Electric accesory
		-A+C 	- Towel Dryers
		-A+B+C  - Towel radiator
		- +D 	- RF cominication'''
		type_A = ("       -  EN 60335-1:2012/AC:2014\n")
		type_B = ("       -  EN 60335-2-30:2012\n")
		type_C = ("       -  EN 60335-2-43:2003 + A1:2006 + A2:2008\n")
		type_D = ("       -  ")

		norms_output = ""

		for i in range(0,len(CE_type)):

			if CE_type[i].upper() == 'A':
				norms_output += type_A

			elif CE_type[i].upper() == 'B':
				norms_output += type_B

			elif CE_type[i].upper() == 'C':
				norms_output += type_C

		return norms_output


class LayoutElectric_EN(ElectricRadiatorDeclarationLayout):

	def __init__(self):
		super().__init__()
		self.line1 = 'Declaration of conformity for CE marking'
		self.line2 = 'The manufacturer:'
		self.line3 = "confirms, that the radiator is"
		self.line4 = 'produced in'
		self.line5 = 'The type'
		self.line6 = 'that includes model code'
		self.line7 = 'is conform to following standards:'
		self.line8 = "          Electrical safaty(LVD):\n"
		self.line9 = "          Electromagnetic Compability (EMC):\n"
		self.line10 = "according to the EU regulations LVD 2014/35/EU and EMC 2014/30/EU."

class LayoutElectric_DE(ElectricRadiatorDeclarationLayout):

	def __init__(self):
		super().__init__()
		self.line1 = 'Konformitätserklärung für die CE Kennzeichnung'
		self.line2 = 'Der Hersteller:'
		self.line3 = 'bestätigt, dass der Heizkörper ist'
		self.line4 = 'produziert in'
		self.line5 = 'Der Typ'
		self.line6 = 'inklusiv der Modelle'
		self.line7 = 'ist konform zu folgenden Normen:'
		self.line8 = '          Elektrische Sicherheit (LVD):\n'
		self.line9 = '          Elektromagnetische Verträglichkeit (EMC):\n'
		self.line10 = 'gemäss den EU Verordnungen LVD 2014/35/EU und EMC 2014/30/EU.'

class LayoutElectric_FR(ElectricRadiatorDeclarationLayout):

	def __init__(self):
		super().__init__()
		self.line1 = 'Déclaration de conformité pour le marquage CE'
		self.line2 = 'Le fabricant:'
		self.line3 = 'confirme, que le radiateur est'
		self.line4 = 'produit à'
		self.line5 = 'Le type'
		self.line6 = 'y compris les modèles'
		self.line7 = 'est conforme aux normes suivantes:'
		self.line8 = '          Sécurité électrique (LVD):\n'
		self.line9 = '          Compatibilité électromagnétique (CEM)\n'
		self.line10 = "conformément aux règlements de l'UE LVD 2014/35/UE et CEM 2014/30/UE."

class LayoutElectric_IT(ElectricRadiatorDeclarationLayout):

	def __init__(self):
		super().__init__()
		self.line1 = 'Dichiarazione di conformità per la marcatura CE'
		self.line2 = 'Il produttore:'
		self.line3 = 'conferma, che il radiatore è'
		self.line4 = 'prodotto in'
		self.line5 = 'Tipo'
		self.line6 = 'compresi i codici modelli'
		self.line7 = 'è conforme alle seguenti norme:'
		self.line8 = '          Sicurezza elettrica (LVD):\n'
		self.line9 = '          Compatibilità elettromagnetica (EMC):\n'
		self.line10 = 'secondo i regolamenti UE LVD 2014/35/UE e EMC 2014/30/UE.'

class LayoutElectric_PL(ElectricRadiatorDeclarationLayout):

	def __init__(self):
		super().__init__()
		self.line1 = 'Deklaracja zgodności dla oznakowania CE'
		self.line2 = 'Producent:'
		self.line3 = 'potwierdza, że grzejnik'
		self.line4 = 'produkowany w'
		self.line5 = 'Typ'
		self.line6 = 'w tym modele'
		self.line7 = 'jest zgodny z następującymi normami:'
		self.line8 = '          Bezpieczeństwo elektryczne (LVD):\n'
		self.line9 = '          Kompatybilność elektromagnetyczna (EMC):\n'
		self.line10 = 'zgodnie z przepisami UE LVD 2014/35/UE i EMC 2014/30/UE.'


''' switch a laguage of declaration by returning diffrent class name'''
def language_switcher(argument):

	switcher= {
	 'EN':LayoutElectric_EN,
	 'DE':LayoutElectric_DE,
	 'FR':LayoutElectric_FR,
	 'PL':LayoutElectric_PL,
	 'IT':LayoutElectric_IT,
	}

	language = switcher.get(argument)
	return language()




