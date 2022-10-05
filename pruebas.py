from collections import Counter
import operator


letras = ['e', 'a', 'o', 'l', 's', 'n', 'd', 'r', 'u', 'i', 't', 'c', 'p', 'm', 'y' ,'q', 'b', 'h', 'g', 'f', 'v', 'j', 'ñ', 'z', 'x', 'k', 'w']
text="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"

letters = Counter(text)
letras_ordenadas = sorted(letters.items(), key=operator.itemgetter(1), reverse=True)


print(text)
print(letters)
print(letras_ordenadas[2])
i=1;
cont= 0;
sololetras= [];
letrasPorcentajes= [];
porcentajes= [];
while i<len(letras_ordenadas):
	if letras_ordenadas[i][0].isalpha():
		cont = cont+letras_ordenadas[i][1];
		sololetras.append(letras_ordenadas[i])
	i= i+1;	
print(cont);
print(sololetras);

i= 0;
while i<len(sololetras):
	porcentajes.append((sololetras[i][1]*100)/cont);
	letrasPorcentajes.append(sololetras[i][0]);
	
	
	
	i= i+1;
i=0;	

print(letrasPorcentajes);

while i<len(porcentajes):

		print(porcentajes[i],letrasPorcentajes[i],letras[i]);
		i= i+1;
while True:
	text=text.replace(input("letra a sustituir: "), input("por: "))
	
	print()
	print(text)
	print()
	while i<len(porcentajes):

		print(porcentajes[i],letrasPorcentajes[i],letras[i]);
		i= i+1;
