import os
numero = "e5ed313192776744b9b93b1320b5e268";
u= '1';
con= 0;
archivo="";
datos="";
es = 1;
#bucle del 1-9
while es==1 and con<9:
	os.system('md5sum imagen'+u+'.jpg> nano');
	archivo = open("/home/mario/miRepo/imagen/nano","r");
	datos= archivo.read(32);
	if datos==numero:
		es=0;
	
	u=chr(ord(u)+1);
	con= con+1;
u= '0';
d = '1';
#bucle comprbando el 10-46
while es==1 and con<46:
	os.system('md5sum imagen'+d+u+'.jpg> nano');
	archivo = open("/home/mario/miRepo/imagen/nano","r");
	datos= archivo.read(32);
	if datos==numero:
		es=0;
	if u=='9':
		u= '0';
		d= chr(ord(d)+1);
	else: 
		u=chr(ord(u)+1);
		
	con= con+1;

print(datos);
print(con);
